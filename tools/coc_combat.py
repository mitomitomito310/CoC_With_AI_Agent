#!/usr/bin/env python3
"""Pure Quick-Start combat ordering, contests, injury, and healing helpers."""
from __future__ import annotations

import math


def initiative(participants:list[dict])->list[dict]:
 """Order by effective DEX; preserve input order where the source has no tie rule."""
 ordered=[]
 for index,p in enumerate(participants):
  if not isinstance(p.get('dex'),int) or p['dex'] < 0:
   raise ValueError('participant DEX must be a non-negative integer')
  effective=p['dex'] + (50 if p.get('readied_firearm') else 0)
  ordered.append({**p,'effective_dex':effective,'_input_order':index})
 ordered.sort(key=lambda p:(-p['effective_dex'],p['_input_order']))
 for p in ordered: p.pop('_input_order')
 return ordered


def melee_contest(attacker_level:str,defender_level:str,defense:str)->dict:
 rank={'failure':0,'regular':1,'hard':2,'extreme':3}
 if attacker_level not in rank or defender_level not in rank:
  raise ValueError('invalid success level')
 if defense not in {'dodge','fight_back'}:
  raise ValueError('defense must be dodge or fight_back')
 if defense=='dodge': hit=rank[attacker_level] > rank[defender_level]
 else: hit=rank[attacker_level] >= rank[defender_level] and rank[attacker_level] > 0
 return {'attacker_hits':hit,'winner':'attacker' if hit else 'defender',
         'tie_rule':'defender' if defense=='dodge' else 'attacker',
         'ledger_ids':['RUL-CMB-02'],'source_pages':[17,18]}


def melee_modifier(*, prior_defenses:int=0, build_difference:int=0,
                   maneuver:bool=False)->dict:
 if prior_defenses < 0: raise ValueError('prior_defenses cannot be negative')
 if maneuver and build_difference >= 3:
  return {'modifier':0,'no_effect':True,'reason':'defender_three_or_more_build_larger'}
 penalty=min(2,max(0,build_difference)) if maneuver else 0
 bonus=1 if prior_defenses >= 1 else 0
 return {'modifier':bonus-penalty,'no_effect':False,
         'reason':'outnumbered_bonus' if bonus and not penalty else 'maneuver_build_adjustment' if penalty else 'none'}


def firearm_modifier(*, shots:int=1, point_blank:bool=False,
                     target_dives_for_cover:bool=False)->dict:
 if shots < 1 or shots > 3: raise ValueError('Quick-Start helper supports 1..3 handgun shots')
 modifier=(1 if point_blank else 0) + (-1 if shots >= 2 else 0) + (-1 if target_dives_for_cover else 0)
 return {'modifier':max(-1,min(1,modifier)),'raw_modifier':modifier,
         'target_forfeits_next_attack':target_dives_for_cover,
         'ledger_ids':['RUL-CMB-04'],'source_pages':[18]}


def healing(*, kind:str, current_hp:int, maximum_hp:int, roll:int|None=None,
            same_day:bool=True, hours_since_injury:int=0, dying:bool=False,
            stabilized:bool=False, con_level:str|None=None)->dict:
 if not 0 <= current_hp <= maximum_hp: raise ValueError('invalid HP')
 if kind=='first_aid':
  eligible=hours_since_injury <= 1
  amount=1 if eligible else 0
  return {'eligible':eligible,'difficulty':'regular','hours_required':0,
          'hp':min(maximum_hp,current_hp+amount),'restored':amount,
          'stabilized':dying and eligible,'major_wound_removed':False,
          'ledger_ids':['RUL-HEAL-02'],'source_pages':[11,19]}
 if kind=='medicine':
  if dying and not stabilized:
   return {'eligible':False,'reason':'dying_requires_first_aid_stabilization','restored':0,'hp':current_hp}
  if roll not in {1,2,3}: raise ValueError('Medicine requires a recorded D3 result')
  return {'eligible':True,'difficulty':'regular' if same_day else 'hard','hours_required':1,
          'hp':min(maximum_hp,current_hp+roll),'restored':min(roll,maximum_hp-current_hp),
          'stabilized':stabilized,'major_wound_removed':False,
          'ledger_ids':['RUL-HEAL-02'],'source_pages':[11,19]}
 if kind=='natural':
  if con_level not in {'regular','extreme','failure'}: raise ValueError('natural healing requires CON level')
  dice=2 if con_level=='extreme' else 1 if con_level=='regular' else 0
  if dice and (roll is None or not dice <= roll <= 3*dice): raise ValueError('invalid recorded healing roll')
  amount=roll or 0
  return {'eligible':True,'difficulty':'regular','interval_days':7,'hp':min(maximum_hp,current_hp+amount),
          'restored':min(amount,maximum_hp-current_hp),'major_wound_removed':con_level=='extreme',
          'ledger_ids':['RUL-HEAL-01'],'source_pages':[19]}
 raise ValueError('unknown healing kind')
