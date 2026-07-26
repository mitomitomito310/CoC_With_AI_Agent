#!/usr/bin/env python3
"""Pure Quick-Start resolution calculations; never mutates scenario state."""
from __future__ import annotations
import argparse,json,math,sys,uuid
from datetime import datetime,timezone
from pathlib import Path

if __package__ in (None, ""):
 sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tools.coc_dice import select

def thresholds(skill:int)->dict:
 if not 0<=skill<=100: raise ValueError('skill must be 0..100')
 return {'regular':skill,'hard':math.floor(skill/2),'extreme':math.floor(skill/5)}
def success_level(roll:int,skill:int)->str:
 t=thresholds(skill)
 if roll<=t['extreme']: return 'extreme'
 if roll<=t['hard']: return 'hard'
 if roll<=t['regular']: return 'regular'
 return 'failure'
def resolves(level:str,difficulty:str)->bool:
 order={'failure':0,'regular':1,'hard':2,'extreme':3}; return order[level]>=order[difficulty]
def resolution(*,skill:int,difficulty:str,ones:int,tens:list[int],modifier:int=0,source='physical',goal='',scenario_id=None,
               pre_state_refs:list[str]|None=None,state_deltas:list[dict]|None=None)->dict:
 dice=select(ones,tens,modifier); level=success_level(dice['selected'],skill); ok=resolves(level,difficulty)
 return {'resolution_id':'res-'+uuid.uuid4().hex[:12],'profile':'coc7e_quick_start_2016_ja','scenario_id':scenario_id,'capability_status':'verified','ledger_ids':['RUL-RES-02'] + (['RUL-MOD-01'] if modifier else []),'source_pages':[14,15] if modifier else [14],'goal':goal,'pre_state_refs':pre_state_refs or [],'roll':{'source':source,'ones':ones,'tens_candidates':tens,'candidates':dice['candidates'],'selected':dice['selected'],'modifier':modifier},'thresholds':thresholds(skill),'selected_branch':f'{level}_{"success" if ok else "failure"}','state_deltas':state_deltas or [],'unresolved_source':None,'applied':False,'created_at':datetime.now(timezone.utc).isoformat().replace('+00:00','Z')}
def opposed(a:dict,b:dict)->str:
 rank={'failure':0,'regular':1,'hard':2,'extreme':3}
 if rank[a['level']] != rank[b['level']]: return 'a' if rank[a['level']]>rank[b['level']] else 'b'
 if a['skill'] != b['skill']: return 'a' if a['skill']>b['skill'] else 'b'
 if a['roll'] != b['roll']: return 'a' if a['roll']<b['roll'] else 'b'
 return 'tie'

def push_eligibility(*, combat:bool, method_changed:bool, consequence_recorded:bool,
                     attempts:int=0, keeper_approved:bool=False)->dict:
 """Return the auditable Quick-Start push gate without making a Keeper decision."""
 reasons=[]
 if combat: reasons.append('combat_roll_cannot_be_pushed')
 if attempts: reasons.append('push_already_used')
 if not method_changed: reasons.append('method_not_materially_changed')
 if not consequence_recorded: reasons.append('escalated_consequence_not_recorded')
 if not keeper_approved: reasons.append('keeper_approval_required')
 return {
  'eligible':not reasons,
  'reasons':reasons,
  'ledger_ids':['RUL-PSH-01','RUL-PSH-02'],
  'source_pages':[14,16],
 }

def authority_gate(*, generic_profile:str, scenario_id:str|None=None,
                   scenario_profile:str|None=None, conflict_resolved:bool=False,
                   reversible_ruling:bool=False)->dict:
 """Stop irreversible effects when profile and scenario authority conflict."""
 conflict=bool(scenario_profile and scenario_profile != generic_profile)
 permitted=not conflict or conflict_resolved or reversible_ruling
 return {
  'authority': 'scenario_local' if scenario_profile and scenario_id else 'generic',
  'scenario_id':scenario_id,
  'conflict':conflict,
  'irreversible_change_permitted':permitted and not reversible_ruling,
  'reversible_ruling_permitted':permitted,
  'status':'resolved' if conflict_resolved else 'reversible_ruling' if reversible_ruling else 'blocked' if conflict else 'clear',
  'ledger_ids':['RUL-SCN-01','RUL-SCN-02','RUL-SCN-03'] if scenario_profile else ['RUL-RES-02'],
 }
def damage(current:int,maximum:int,amount:int,already_major=False)->dict:
 if min(current,maximum,amount)<0: raise ValueError('HP values cannot be negative')
 hp=max(0,current-amount); major=amount>=math.ceil(maximum/2); immediate=amount>maximum
 return {'hp':hp,'major_wound':already_major or major,'con_check':major and not immediate,'dead':immediate,'dying':hp==0 and (already_major or major) and not immediate,'unconscious':hp==0 and not (already_major or major) and not immediate}
def main():
 p=argparse.ArgumentParser(); p.add_argument('--skill',type=int,required=True); p.add_argument('--difficulty',choices=['regular','hard','extreme'],default='regular'); p.add_argument('--ones',type=int,required=True); p.add_argument('--tens',type=int,nargs='+',required=True); p.add_argument('--modifier',type=int,choices=[-1,0,1],default=0); p.add_argument('--source',choices=['script','physical'],default='physical'); p.add_argument('--goal',default=''); a=p.parse_args(); print(json.dumps(resolution(**vars(a)),ensure_ascii=False,indent=2))
if __name__=='__main__': main()
