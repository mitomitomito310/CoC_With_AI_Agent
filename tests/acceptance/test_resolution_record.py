from tools.coc_resolve import resolution
from tools.coc_validate import validate_resolution
import json

def test_physical_dice_resolution_record(tmp_path):
 r=resolution(skill=60,difficulty='hard',ones=0,tens=[3],source='physical',goal='調査'); p=tmp_path/'r.json'; p.write_text(json.dumps(r)); assert validate_resolution(p)==[]; assert r['roll']['selected']==30; assert r['selected_branch']=='hard_success'
def test_script_and_physical_share_contract():
 a=resolution(skill=60,difficulty='regular',ones=0,tens=[6],source='script'); b=resolution(skill=60,difficulty='regular',ones=0,tens=[6],source='physical'); assert a.keys()==b.keys(); assert a['roll'].keys()==b['roll'].keys()
