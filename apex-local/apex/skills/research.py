import requests

def webSearch(query,limit=5):
 r=requests.get('https://www.google.com/search',params={'q':query},headers={'User-Agent':'APEX Local'},timeout=15);return {'status':r.status_code,'query':query,'note':'Raw search retrieval; production adapters should use an approved search provider.'}
def summarize(text): return {'summary':text[:4000]}
