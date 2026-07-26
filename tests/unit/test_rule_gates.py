from tools.coc_resolve import authority_gate, push_eligibility


def test_ac_rul_06_push_gate():
 allowed=push_eligibility(combat=False,method_changed=True,consequence_recorded=True,keeper_approved=True)
 assert allowed['eligible']
 assert not push_eligibility(combat=True,method_changed=True,consequence_recorded=True,keeper_approved=True)['eligible']
 assert not push_eligibility(combat=False,method_changed=False,consequence_recorded=True,keeper_approved=True)['eligible']
 assert not push_eligibility(combat=False,method_changed=True,consequence_recorded=True,keeper_approved=True,attempts=1)['eligible']


def test_ac_rul_16_authority_conflict_stops_irreversible_change():
 blocked=authority_gate(generic_profile='quick-start',scenario_id='case',scenario_profile='local-exception')
 assert blocked['conflict'] and not blocked['irreversible_change_permitted']
 assert authority_gate(generic_profile='quick-start',scenario_id='case',scenario_profile='local-exception',conflict_resolved=True)['irreversible_change_permitted']
 reversible=authority_gate(generic_profile='quick-start',scenario_id='case',scenario_profile='local-exception',reversible_ruling=True)
 assert reversible['reversible_ruling_permitted'] and not reversible['irreversible_change_permitted']
