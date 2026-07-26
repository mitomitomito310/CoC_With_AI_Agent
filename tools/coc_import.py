#!/usr/bin/env python3
"""Create a spoiler-safe scenario workspace while preserving source bytes."""
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import sys
from datetime import datetime,timezone
from pathlib import Path

if __package__ in (None, ""):
 sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from tools.coc_validate import validate_scenario


def _safe_id(value:str)->str:
 import re
 if not re.fullmatch(r'[a-z0-9][a-z0-9_-]{2,63}',value): raise ValueError('invalid scenario_id')
 return value


def import_scenario(*,source:Path,root:Path,scenario_id:str,title:str,
                    location:str,participants:list[str],npcs:list[str]|None=None,
                    rules_profile:str='coc7e_quick_start_2016_ja',now:str|None=None)->Path:
 """Import text/Markdown only. Content interpretation remains a Keeper task."""
 _safe_id(scenario_id)
 source=source.resolve()
 if not source.is_file() or source.suffix.lower() not in {'.md','.txt'}:
  raise ValueError('source must be an existing Markdown or text file')
 if not participants: raise ValueError('opening requires participants')
 workspace=root/scenario_id
 if workspace.exists(): raise FileExistsError(f'scenario workspace already exists: {workspace}')
 (workspace/'source').mkdir(parents=True)
 (workspace/'keeper'/'rules').mkdir(parents=True)
 (workspace/'keeper'/'indexes').mkdir(parents=True)
 (workspace/'public'/'handouts').mkdir(parents=True)
 (workspace/'session'/'events').mkdir(parents=True)
 (workspace/'session'/'resolutions').mkdir(parents=True)
 (workspace/'session'/'checkpoints').mkdir(parents=True)
 target=workspace/'source'/source.name
 shutil.copyfile(source,target)
 target.chmod(0o444)
 digest=hashlib.sha256(target.read_bytes()).hexdigest()
 media='text/markdown' if source.suffix.lower()=='.md' else 'text/plain'
 timestamp=now or datetime.now(timezone.utc).isoformat().replace('+00:00','Z')
 actors=[{'id':p,'role':'player'} for p in participants]
 for npc in npcs or []:
  if npc not in participants: actors.append({'id':npc,'role':'npc'})
 doc={'schema_version':'1.0','scenario_id':scenario_id,'title':title,'rules_profile':rules_profile,
      'status':'ready','status_reason':'source preserved; Keeper indexes pending enrichment',
      'blocking_issues':[],'source':[{'path':f'source/{source.name}','sha256':digest,'media_type':media,'immutable':True}],
      'opening':{'scene_id':'opening','location':location,'participants':participants},'actors':actors,
      'secrecy':{'classified':True,'public_import_report':'ready'},'current_scene_id':None,
      'last_checkpoint_id':None,'state_version':0,'updated_at':timestamp}
 scenario_path=workspace/'scenario.json'; scenario_path.write_text(json.dumps(doc,ensure_ascii=False,indent=2)+'\n')
 errors=validate_scenario(scenario_path)
 if errors:
  shutil.rmtree(workspace); raise ValueError('; '.join(errors))
 (workspace/'keeper'/'indexes'/'manifest.json').write_text(json.dumps({
  'scenario_id':scenario_id,'source_sha256':digest,'truths':[],'clues':[],'npc_secrets':[],
  'classification_status':'keeper_review_required'},ensure_ascii=False,indent=2)+'\n')
 (workspace/'keeper'/'rules'/'scenario_local.json').write_text(json.dumps({
  'namespace':f'scenario:{scenario_id}','scenario_id':scenario_id,'rules':[]},ensure_ascii=False,indent=2)+'\n')
 (workspace/'session'/'current.json').write_text(json.dumps({
  'scenario_id':scenario_id,'state_version':0,'last_checkpoint_id':None,
  'public':{'scene_id':None,'location':None},'keeper':{},'npcs':{}},ensure_ascii=False,indent=2)+'\n')
 return workspace


def import_handout(*,workspace:Path,source:Path,handout_id:str)->dict:
 """Keep the immutable handout source distinct from its release projection."""
 if '/' in handout_id or not handout_id: raise ValueError('invalid handout_id')
 source=source.resolve(); target_dir=workspace/'source'/'handouts'; target_dir.mkdir(parents=True,exist_ok=True)
 target=target_dir/source.name
 if target.exists(): raise FileExistsError(target)
 shutil.copyfile(source,target); target.chmod(0o444)
 return {'handout_id':handout_id,'source_path':str(target.relative_to(workspace)),
         'sha256':hashlib.sha256(target.read_bytes()).hexdigest(),'release_state':'unreleased',
         'released_path':None}


def main():
 p=argparse.ArgumentParser(); p.add_argument('source',type=Path); p.add_argument('--root',type=Path,default=Path('scenarios'))
 p.add_argument('--scenario-id',required=True); p.add_argument('--title',required=True); p.add_argument('--location',required=True)
 p.add_argument('--participant',action='append',required=True); p.add_argument('--npc',action='append',default=[])
 a=p.parse_args(); path=import_scenario(source=a.source,root=a.root,scenario_id=a.scenario_id,title=a.title,
  location=a.location,participants=a.participant,npcs=a.npc); print(path)


if __name__=='__main__': main()
