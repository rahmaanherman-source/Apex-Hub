def test_imports():
 import apex.config, apex.orchestrator, apex.main
 assert apex.main.app.title=='APEX Local'

def test_approval_gate():
 from apex.orchestrator import Orchestrator
 o=Orchestrator(); r=o.execute_skill('stripe','createCheckoutSession',{'amount_cents':100,'product_name':'test'})
 assert r['status']=='approval_required'
