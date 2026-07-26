import pytest
from tools.coc_state import transition
BASE={'status':'ready','opening':{'scene_id':'opening'},'blocking_issues':[]}
def test_lifecycle():
 active=transition(BASE,'active','begin',now='2026-07-26T00:00:00Z'); assert active['current_scene_id']=='opening'
 paused=transition(active,'paused','stop',now='2026-07-26T01:00:00Z'); assert paused['status']=='paused'
 assert transition(paused,'active','resume')['status']=='active'
def test_invalid_transition():
 with pytest.raises(ValueError): transition(BASE,'completed','skip')
def test_blocked_cannot_be_ready():
 with pytest.raises(ValueError): transition({'status':'preparing','blocking_issues':['missing']},'ready','bad')
