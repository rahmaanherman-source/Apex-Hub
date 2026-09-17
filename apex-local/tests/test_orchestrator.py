def test_imports():
 import apex.config, apex.orchestrator, apex.main
 assert apex.main.app.title == 'APEX Local'

def test_approval_gate():
 from apex.orchestrator import Orchestrator
 o=Orchestrator(); r=o.execute_skill('stripe','createCheckoutSession',{'amount_cents':100,'product_name':'test'})
 assert r['status']=='approval_required'

def test_local_route_stays_local():
 from apex.orchestrator import Orchestrator
 o=Orchestrator()
 assert o.route('coding') == 'local.coding'
 assert o.route('general') == 'local.default'

def test_cloud_route_is_explicit():
 from apex.orchestrator import Orchestrator
 o=Orchestrator()
 assert o.route('image_generation') == 'cloud.leonardo'
 assert o.models['routing']['fallback_to_cloud'] is False
