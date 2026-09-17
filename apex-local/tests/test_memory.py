def test_models_config():
 from apex.config import load_yaml
 m=load_yaml('models.yaml');assert m['local']['default']=='qwen2.5-coder:7b';assert m['routing']['fallback_to_cloud'] is False

def test_memory(tmp_path):
 from apex.memory.engine import Memory
 m=Memory(tmp_path/'memory.sqlite3');m.add('APEX test');assert m.search('APEX')
