from tools.coc_resolve import resolution


def test_ac_rul_14_capability_and_replay_provenance():
 profile={'capabilities':{'full_creation':'core_rule_check_required','core_resolution':'verified'}}
 assert profile['capabilities']['full_creation']=='core_rule_check_required'
 record=resolution(skill=60,difficulty='hard',ones=4,tens=[2,4],modifier=1,
                   source='physical',goal='open door',scenario_id='safe_case')
 assert record['profile']=='coc7e_quick_start_2016_ja'
 assert record['ledger_ids']==['RUL-RES-02','RUL-MOD-01']
 assert record['source_pages']==[14,15]
 assert record['roll']=={'source':'physical','ones':4,'tens_candidates':[2,4],
                         'candidates':[24,44],'selected':24,'modifier':1}
 assert record['thresholds']=={'regular':60,'hard':30,'extreme':12}
 assert record['selected_branch']=='hard_success' and not record['applied']
