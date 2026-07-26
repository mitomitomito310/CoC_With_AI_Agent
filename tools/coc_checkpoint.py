#!/usr/bin/env python3
"""Atomically commit pending state changes to checkpoint/current files."""
from __future__ import annotations
import argparse,json,os,tempfile,uuid
from datetime import datetime,timezone
from pathlib import Path

def atomic_write(path:Path,data:dict):
 path.parent.mkdir(parents=True,exist_ok=True); fd,tmp=tempfile.mkstemp(dir=path.parent,prefix='.tmp-',text=True)
 try:
  with os.fdopen(fd,'w') as f: json.dump(data,f,ensure_ascii=False,indent=2); f.write('\n'); f.flush(); os.fsync(f.fileno())
  os.replace(tmp,path)
 finally:
  if os.path.exists(tmp): os.unlink(tmp)
def commit(current:dict,pending:dict,scenario_id:str,scene_id:str)->tuple[dict,dict]:
 base=pending.get('base_version'); actual=current.get('state_version',0)
 if base!=actual: raise ValueError(f'stale pending version: {base} != {actual}')
 changes=pending.get('changes',[])
 if not changes: raise ValueError('empty checkpoint')
 state=json.loads(json.dumps(current))
 for c in changes:
  keys=c['path'].strip('/').split('/'); node=state
  for k in keys[:-1]: node=node.setdefault(k,{})
  if node.get(keys[-1]) != c.get('before'): raise ValueError(f'pre-state mismatch: {c["path"]}')
  node[keys[-1]]=c.get('after')
 state['state_version']=actual+1
 cp={'checkpoint_id':'cp-'+uuid.uuid4().hex[:12],'scenario_id':scenario_id,'scene_id':scene_id,'base_version':actual,'state_version':actual+1,'status':'committed','event_ids':pending.get('event_ids',[]),'resolution_ids':pending.get('resolution_ids',[]),'changes':changes,'created_at':datetime.now(timezone.utc).isoformat().replace('+00:00','Z')}
 state['last_checkpoint_id']=cp['checkpoint_id']; return state,cp
def main():
 p=argparse.ArgumentParser(); p.add_argument('current'); p.add_argument('pending'); p.add_argument('checkpoint'); p.add_argument('--scenario-id',required=True); p.add_argument('--scene-id',required=True); a=p.parse_args(); cur=Path(a.current); state,cp=commit(json.loads(cur.read_text()),json.loads(Path(a.pending).read_text()),a.scenario_id,a.scene_id); atomic_write(Path(a.checkpoint),cp); atomic_write(cur,state); print(cp['checkpoint_id'])
if __name__=='__main__': main()
