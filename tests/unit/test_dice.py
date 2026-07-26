from tools.coc_dice import select,value
from tools.coc_resolve import thresholds,success_level,opposed,damage

def test_d100_zero_is_100(): assert value(0,0)==100

def test_bonus_penalty_ac_rul_05():
 assert select(4,[2,4],1)['selected']==24
 assert select(4,[2,4],-1)['selected']==44
 assert select(4,[2],0)['selected']==24

def test_threshold_boundaries_ac_rul_04():
 assert thresholds(60)=={'regular':60,'hard':30,'extreme':12}
 assert [success_level(x,60) for x in [60,30,12,31,13]]==['regular','hard','extreme','regular','hard']

def test_opposed_ac_rul_07():
 assert opposed({'level':'hard','skill':50,'roll':25},{'level':'regular','skill':80,'roll':60})=='a'
 assert opposed({'level':'hard','skill':50,'roll':25},{'level':'hard','skill':80,'roll':40})=='b'
 assert opposed({'level':'regular','skill':50,'roll':42},{'level':'regular','skill':50,'roll':37})=='b'

def test_damage_ac_rul_09():
 assert damage(12,12,6)['major_wound']
 assert damage(12,12,13)['dead']
 assert damage(4,12,4,True)['dying']
 assert damage(4,12,4,False)['unconscious']
