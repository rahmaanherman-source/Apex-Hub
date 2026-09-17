import os
from pathlib import Path
import yaml
from dotenv import load_dotenv
ROOT=Path(__file__).resolve().parent.parent
CONFIG_DIR=ROOT/'config'; SECRETS_DIR=ROOT/'secrets'; LOGS_DIR=ROOT/'logs'
load_dotenv(SECRETS_DIR/'.env')
def load_yaml(name):
    with open(CONFIG_DIR/name,encoding='utf-8') as f:return yaml.safe_load(f)
def env(key,default=''):return os.getenv(key,default)
