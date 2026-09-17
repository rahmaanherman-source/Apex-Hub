from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from apex.orchestrator import Orchestrator
from apex.models.local import list_models
app=FastAPI(title='APEX Local',version='1.0.0'); orch=Orchestrator()
class Prompt(BaseModel): prompt:str; task_type:str='general'
class SkillCall(BaseModel): skill:str; operation:str; params:dict={}; approved:bool=False
@app.get('/')
def root():return {'status':'ok','models':list_models()}
@app.get('/health')
def health():return {'ok':True,'models':list_models()}
@app.post('/run')
def run(p:Prompt):
    try:return {'output':orch.run(p.prompt,p.task_type)}
    except Exception as e:raise HTTPException(500,str(e))
@app.post('/skill')
def skill(s:SkillCall):
    try:return orch.execute_skill(s.skill,s.operation,s.params,s.approved)
    except Exception as e:raise HTTPException(400,str(e))
