import pytest
from tools.coc_checkpoint import commit

def test_atomic_projection():
 current={'state_version':2,'public':{'location':'hall'},'last_checkpoint_id':'cp-old'}
 pending={'base_version':2,'event_ids':['e1'],'resolution_ids':['r1'],'changes':[{'path':'/public/location','before':'hall','after':'gallery','visibility':'public'}]}
 state,cp=commit(current,pending,'s','scene'); assert state['public']['location']=='gallery'; assert state['state_version']==3; assert cp['base_version']==2

def test_stale_rejected():
 with pytest.raises(ValueError): commit({'state_version':2},{'base_version':1,'changes':[{}]},'s','x')
