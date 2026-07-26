import hashlib
import json

import pytest

from tools.coc_checkpoint import commit
from tools.coc_import import import_handout, import_scenario
from tools.coc_resume import projections, write_projections
from tools.coc_validate import validate_scenario


def test_ac_rul_13_15_import_preserves_namespaces_and_handout(tmp_path):
 original=tmp_path/'authored.md'; original.write_text('# Secret scenario\nThe culprit is X.\n')
 root=tmp_path/'scenarios'
 workspace=import_scenario(source=original,root=root,scenario_id='safe_case',title='Safe Case',
  location='Entrance',participants=['investigator'],npcs=['guide'],now='2026-07-26T00:00:00Z')
 assert validate_scenario(workspace/'scenario.json')==[]
 copied=workspace/'source'/'authored.md'
 assert copied.read_bytes()==original.read_bytes()
 scenario=json.loads((workspace/'scenario.json').read_text())
 assert scenario['source'][0]['sha256']==hashlib.sha256(original.read_bytes()).hexdigest()
 local=json.loads((workspace/'keeper'/'rules'/'scenario_local.json').read_text())
 assert local['namespace']=='scenario:safe_case' and local['scenario_id']=='safe_case'
 assert local['rules']==[]  # Examples and prose are never promoted automatically.

 handout=tmp_path/'letter.txt'; handout.write_text('Private letter')
 record=import_handout(workspace=workspace,source=handout,handout_id='letter')
 assert record['release_state']=='unreleased' and record['released_path'] is None
 assert (workspace/record['source_path']).read_bytes()==handout.read_bytes()
 with pytest.raises(FileExistsError):
  import_scenario(source=original,root=root,scenario_id='safe_case',title='Again',location='x',participants=['p'])


def test_ac_sta_03_checkpoint_to_separated_resume(tmp_path):
 current={'scenario_id':'safe_case','state_version':0,'last_checkpoint_id':None,
          'public':{'scene_id':'opening','location':'Entrance'},
          'keeper':{'culprit':'X'},'npcs':{'guide':{'facts':['saw mud']},'guard':{'facts':[]}}}
 pending={'base_version':0,'event_ids':['evt-1'],'resolution_ids':[],
          'changes':[{'path':'/public/location','before':'Entrance','after':'Hall','visibility':'public'}]}
 state,checkpoint=commit(current,pending,'safe_case','hall')
 current_path=tmp_path/'current.json'; current_path.write_text(json.dumps(state))
 paths=write_projections(current_path,tmp_path/'resume')
 assert len(paths)==4
 views=projections(state)
 assert 'keeper' not in views['public'] and 'npcs' not in views['public']
 assert views['npcs']['guide']['knowledge']=={'facts':['saw mud']}
 assert 'guard' not in views['npcs']['guide']
 assert views['keeper']['keeper']['culprit']=='X'
 assert checkpoint['state_version']==views['public']['state_version']==1


def test_checkpoint_rejects_boundary_and_path_errors():
 current={'state_version':0,'public':{'x':1}}
 with pytest.raises(ValueError,match='npc_id'):
  commit(current,{'base_version':0,'changes':[{'path':'/public/x','before':1,'after':2,'visibility':'npc'}]},'s','x')
 with pytest.raises(ValueError,match='missing parent'):
  commit(current,{'base_version':0,'changes':[{'path':'/missing/x','before':None,'after':2,'visibility':'public'}]},'s','x')
