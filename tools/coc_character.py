#!/usr/bin/env python3
"""Quick-Start investigator calculations and creation-contract validation."""
from __future__ import annotations

import math

CHARACTERISTICS={'STR','CON','SIZ','DEX','APP','INT','POW','EDU'}
QUICK_START_VALUES=[40,50,50,50,60,60,70,80]


def derived(attributes:dict[str,int])->dict:
 missing=CHARACTERISTICS-attributes.keys()
 if missing: raise ValueError(f'missing characteristics: {sorted(missing)}')
 strength_size=attributes['STR']+attributes['SIZ']
 bands=[(64,'-2',-2),(84,'-1',-1),(124,'0',0),(164,'1D4',1),(204,'1D6',2)]
 damage_bonus=build=None
 for maximum,db,b in bands:
  if strength_size <= maximum: damage_bonus,build=db,b; break
 capability='verified' if strength_size <= 204 and strength_size >= 2 else 'core_rule_check_required'
 return {'max_hp':math.floor((attributes['CON']+attributes['SIZ'])/10),'mov':8,
         'initial_san':attributes['POW'],'max_mp':math.floor(attributes['POW']/5),
         'damage_bonus':damage_bonus,'build':build,'damage_build_capability':capability,
         'ledger_ids':['RUL-DRV-01','RUL-DRV-03'],'source_pages':[8,9]}


def validate_quick_start(attributes:dict[str,int],occupation_values:list[int],
                         personal_skill_increases:list[int],mythos_increased:bool=False)->list[str]:
 errors=[]
 if set(attributes)!=CHARACTERISTICS: errors.append('exactly eight named characteristics are required')
 elif sorted(attributes.values())!=QUICK_START_VALUES: errors.append('characteristic allocation must use the Quick-Start array once each')
 if sorted(occupation_values)!=sorted([70,60,60,50,50,50,40,40,40]):
  errors.append('occupation and Credit Rating values must use the fixed nine-value allocation')
 if personal_skill_increases != [20,20,20,20]: errors.append('four personal-interest skills must each add 20')
 if mythos_increased: errors.append('Cthulhu Mythos cannot receive Quick-Start creation points')
 return errors


def improvement(*,current:int,check_roll:int,increase_roll:int|None=None)->dict:
 if not 0 <= current <= 100 or not 1 <= check_roll <= 100: raise ValueError('invalid improvement input')
 eligible=check_roll > current
 if eligible and (increase_roll is None or not 1 <= increase_roll <= 10):
  raise ValueError('successful improvement requires a recorded 1D10')
 increase=increase_roll or 0 if eligible else 0
 return {'eligible':eligible,'before':current,'increase':increase,'after':min(100,current+increase),
         'mark_cleared':True,'ledger_ids':['RUL-SKL-04'],'source_pages':[10,19,20]}
