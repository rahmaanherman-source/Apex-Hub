import tkinter as tk
from tkinter import messagebox
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent; ENV=ROOT/'secrets'/'.env'
FIELDS=[('GOOGLE_AI_STUDIO_KEY','Google AI Studio'),('LEONARDO_API_KEY','Leonardo'),('MINIMAX_API_KEY','MiniMax'),('SHOPIFY_ADMIN_TOKEN','Shopify Admin Token'),('SHOPIFY_STORE_DOMAIN','Shopify Store Domain'),('STRIPE_SECRET_KEY','Stripe Secret Key')]
def load():
 d={}
 if ENV.exists():
  for line in ENV.read_text().splitlines():
   if '=' in line and not line.lstrip().startswith('#'):
    k,v=line.split('=',1);d[k]=v
 return d
def save(vals):
 ENV.parent.mkdir(parents=True,exist_ok=True); ENV.write_text('# APEX Local Secrets\n'+'\n'.join(f'{k}={vals.get(k,"")}' for k,_ in FIELDS)+'\n');
class Vault:
 def __init__(self,r):
  r.title('APEX Vault');r.geometry('640x420');self.entries={};cur=load()
  tk.Label(r,text='APEX VAULT',font=('Segoe UI',18,'bold')).pack(pady=12)
  f=tk.Frame(r);f.pack(padx=20,fill='both',expand=True)
  for i,(k,label) in enumerate(FIELDS):
   tk.Label(f,text=label).grid(row=i,column=0,sticky='w',pady=5);e=tk.Entry(f,width=48,show='*');e.insert(0,cur.get(k,''));e.grid(row=i,column=1,padx=8,pady=5);self.entries[k]=e
  tk.Button(r,text='Save',command=self.save).pack(pady=10)
 def save(self):save({k:e.get().strip() for k,e in self.entries.items()});messagebox.showinfo('APEX Vault','Secrets saved locally.')
if __name__=='__main__':
 r=tk.Tk();Vault(r);r.mainloop()
