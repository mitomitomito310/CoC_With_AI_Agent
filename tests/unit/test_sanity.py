import pytest

from tools.coc_sanity import bout, intelligence_branch, reality_check, sanity_check


def test_ac_rul_11_san_loss_and_int_order():
 success=sanity_check(current_san=60,roll=60,success_loss=0,failure_loss='1D6')
 assert success['loss']==0 and success['san_after']==60
 failure=sanity_check(current_san=60,roll=61,success_loss=0,failure_loss='1D6',loss_roll=5)
 assert failure['san_after']==55 and failure['temporary_insanity_check_required']
 enters=intelligence_branch(loss=5,intelligence=70,roll=70,duration_hours=8)
 assert enters['temporary_insanity'] and enters['duration_hours']==8
 avoids=intelligence_branch(loss=5,intelligence=70,roll=71)
 assert not avoids['temporary_insanity'] and avoids['failure_effect']=='no_temporary_insanity_only'


def test_ac_rul_12_bout_and_reality_gate():
 state=bout(selection=4,duration_rounds=7,kind='phobia')
 assert state['all_actions_modifier']==-1 and state['duration_rounds']==7
 assert reality_check(current_san=55,roll=55)['delusion_pierced']
 failed=reality_check(current_san=55,roll=56)
 assert failed['capability_status']=='core_rule_check_required'
 assert not failed['irreversible_change_permitted']
 with pytest.raises(ValueError): bout(selection=11,duration_rounds=1)
