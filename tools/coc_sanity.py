#!/usr/bin/env python3
"""Pure calculations for the SAN and temporary-insanity Quick-Start scope."""
from __future__ import annotations


def parse_loss(value:int|str, recorded_roll:int|None=None)->int:
 if isinstance(value,int):
  if value < 0: raise ValueError('SAN loss cannot be negative')
  return value
 text=value.upper().strip()
 if 'D' not in text: return parse_loss(int(text))
 count_text,sides_text=text.split('D',1); count=int(count_text or '1'); sides=int(sides_text)
 if recorded_roll is None or not count <= recorded_roll <= count*sides:
  raise ValueError('loss dice require an in-range recorded total')
 return recorded_roll


def sanity_check(*, current_san:int, roll:int, success_loss:int|str,
                 failure_loss:int|str, loss_roll:int|None=None)->dict:
 if not 0 <= current_san <= 99 or not 1 <= roll <= 100: raise ValueError('invalid SAN or D100')
 succeeded=roll <= current_san
 expression=success_loss if succeeded else failure_loss
 loss=parse_loss(expression,loss_roll)
 after=max(0,current_san-loss)
 return {'succeeded':succeeded,'selected_loss':str(expression),'loss':loss,
         'san_before':current_san,'san_after':after,'temporary_insanity_check_required':loss >= 5,
         'ledger_ids':['RUL-SAN-01','RUL-SAN-02'] if loss >= 5 else ['RUL-SAN-01'],'source_pages':[16]}


def intelligence_branch(*, loss:int, intelligence:int, roll:int,
                        duration_hours:int|None=None)->dict:
 if loss < 5: return {'required':False,'temporary_insanity':False}
 if not 0 <= intelligence <= 100 or not 1 <= roll <= 100: raise ValueError('invalid INT check')
 enters=roll <= intelligence
 if enters and (duration_hours is None or not 1 <= duration_hours <= 10):
  raise ValueError('temporary insanity requires a recorded 1D10 hour duration')
 return {'required':True,'succeeded':enters,'temporary_insanity':enters,
         'duration_hours':duration_hours if enters else None,
         'failure_effect':'no_temporary_insanity_only' if not enters else None,
         'ledger_ids':['RUL-SAN-02'],'source_pages':[16]}


def bout(*, selection:int, duration_rounds:int, kind:str|None=None)->dict:
 if not 1 <= selection <= 10 or not 1 <= duration_rounds <= 10: raise ValueError('bout rolls must be 1..10')
 if kind not in {None,'phobia','mania','other'}: raise ValueError('invalid bout kind')
 return {'selection':selection,'duration_rounds':duration_rounds,'kind':kind,
         'all_actions_modifier':-1 if kind in {'phobia','mania'} else 0,
         'ledger_ids':['RUL-INS-01'],'source_pages':[16,17]}


def reality_check(*, current_san:int, roll:int)->dict:
 if not 0 <= current_san <= 99 or not 1 <= roll <= 100: raise ValueError('invalid SAN check')
 success=roll <= current_san
 return {'success':success,'delusion_pierced':success,
         'capability_status':'verified' if success else 'core_rule_check_required',
         'unresolved_source':None if success else 'complete SAN/Keeper source required for added failure effect',
         'irreversible_change_permitted':success,
         'ledger_ids':['RUL-INS-02','RUL-SCOPE-01'],'source_pages':[16]}
