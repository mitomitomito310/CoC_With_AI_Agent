#!/usr/bin/env python3
"""Dependency-free validation for repository contracts and scenario integrity."""
from __future__ import annotations
import argparse,hashlib,json,re
from datetime import datetime
from pathlib import Path

def err(condition,msg,errors):
 if not condition: errors.append(msg)
def validate_scenario(path:Path)->list[str]:
 d=json.loads(path.read_text()); e=[]
 required={'schema_version','scenario_id','title','rules_profile','status','source','opening','actors','secrecy','state_version','updated_at'}
 err(required<=d.keys(),f'missing fields: {sorted(required-d.keys())}',e)
 err(d.get('status') in {'importing','preparing','blocked','ready','active','paused','completed','archived'},'invalid status',e)
 err(bool(re.fullmatch(r'[a-z0-9][a-z0-9_-]{2,63}',d.get('scenario_id',''))),'invalid scenario_id',e)
 try: datetime.fromisoformat(d.get('updated_at','').replace('Z','+00:00'))
 except ValueError: e.append('invalid updated_at')
 for src in d.get('source',[]):
  err(src.get('immutable') is True,'source must be immutable',e); rel=src.get('path','')
  actual=(path.parent/rel); err(actual.is_file(),f'missing source: {rel}',e)
  if actual.is_file(): err(hashlib.sha256(actual.read_bytes()).hexdigest()==src.get('sha256'),f'checksum mismatch: {rel}',e)
 if d.get('status') in {'ready','active','paused','completed'}: err(not d.get('blocking_issues'), 'ready/active scenario has blocking issues',e)
 return e
def validate_resolution(path:Path)->list[str]:
 d=json.loads(path.read_text()); e=[]; req={'resolution_id','profile','capability_status','ledger_ids','source_pages','goal','pre_state_refs','roll','thresholds','selected_branch','state_deltas','applied','created_at'}
 err(req<=d.keys(),f'missing fields: {sorted(req-d.keys())}',e); err(bool(d.get('ledger_ids')),'ledger_ids required',e); err(bool(d.get('source_pages')),'source_pages required',e)
 if d.get('capability_status')=='scenario_local': err(bool(d.get('scenario_id')),'scenario_local requires scenario_id',e)
 return e
def main():
 p=argparse.ArgumentParser(); p.add_argument('kind',choices=['scenario','resolution']); p.add_argument('path'); a=p.parse_args(); errors=(validate_scenario if a.kind=='scenario' else validate_resolution)(Path(a.path)); print(json.dumps({'valid':not errors,'errors':errors},ensure_ascii=False)); raise SystemExit(bool(errors))
if __name__=='__main__': main()
