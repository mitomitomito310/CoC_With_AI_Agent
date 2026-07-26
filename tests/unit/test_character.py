from tools.coc_character import derived, improvement, validate_quick_start


ATTR={'STR':40,'CON':50,'SIZ':50,'DEX':50,'APP':60,'INT':60,'POW':70,'EDU':80}


def test_quick_start_creation_and_derived_provenance():
 assert validate_quick_start(ATTR,[70,60,60,50,50,50,40,40,40],[20,20,20,20])==[]
 values=derived(ATTR)
 assert values['max_hp']==10 and values['initial_san']==70 and values['max_mp']==14
 assert values['damage_bonus']=='0' and values['build']==0
 assert values['ledger_ids']==['RUL-DRV-01','RUL-DRV-03']


def test_creation_rejects_wrong_array_and_mythos_points():
 bad={**ATTR,'STR':50}
 errors=validate_quick_start(bad,[70,60,60,50,50,50,40,40,40],[20]*4,True)
 assert len(errors)==2


def test_skill_improvement_is_replayable():
 result=improvement(current=60,check_roll=61,increase_roll=7)
 assert result['after']==67 and result['mark_cleared']
 assert not improvement(current=60,check_roll=60)['eligible']
