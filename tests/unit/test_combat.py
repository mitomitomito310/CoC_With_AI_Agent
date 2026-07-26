import pytest

from tools.coc_combat import firearm_modifier, healing, initiative, melee_contest, melee_modifier


def test_ac_rul_08_combat_order_ties_and_outnumbering():
 ordered=initiative([
  {'id':'fast','dex':70},{'id':'gun','dex':50,'readied_firearm':True},{'id':'slow','dex':45}
 ])
 assert [(x['id'],x['effective_dex']) for x in ordered]==[('gun',100),('fast',70),('slow',45)]
 assert not melee_contest('hard','hard','dodge')['attacker_hits']
 assert melee_contest('hard','hard','fight_back')['attacker_hits']
 assert melee_modifier(prior_defenses=1)['modifier']==1


def test_firearm_branches_are_explicit():
 assert firearm_modifier(shots=2)['modifier']==-1
 dive=firearm_modifier(target_dives_for_cover=True)
 assert dive['modifier']==-1 and dive['target_forfeits_next_attack']
 assert firearm_modifier(point_blank=True)['modifier']==1
 with pytest.raises(ValueError): firearm_modifier(shots=4)


def test_ac_rul_10_healing():
 assert healing(kind='first_aid',current_hp=0,maximum_hp=12,dying=True,hours_since_injury=1)=={
  'eligible':True,'difficulty':'regular','hours_required':0,'hp':1,'restored':1,
  'stabilized':True,'major_wound_removed':False,'ledger_ids':['RUL-HEAL-02'],'source_pages':[11,19]}
 blocked=healing(kind='medicine',current_hp=0,maximum_hp=12,roll=3,dying=True,stabilized=False)
 assert not blocked['eligible']
 assert healing(kind='medicine',current_hp=5,maximum_hp=12,roll=3,same_day=False)['difficulty']=='hard'
 assert healing(kind='natural',current_hp=5,maximum_hp=12,roll=2,con_level='regular')['restored']==2
 extreme=healing(kind='natural',current_hp=5,maximum_hp=12,roll=6,con_level='extreme')
 assert extreme['restored']==6 and extreme['major_wound_removed']
