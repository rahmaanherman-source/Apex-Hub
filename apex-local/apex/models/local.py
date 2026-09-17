from ollama import generate, chat, list as ollama_list

def run(prompt, model='qwen2.5-coder:7b'):
    r=generate(model=model,prompt=prompt)
    return r.get('response','')
def chat_run(messages, model='qwen2.5-coder:7b'):
    r=chat(model=model,messages=messages)
    return r.get('message',{}).get('content','')
def list_models():
    try:return [m.get('name','') for m in ollama_list().get('models',[])]
    except Exception:return []
