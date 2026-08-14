import { useMemo, useState } from 'react';
import { CheckCircle2, Circle, FileCheck2, ShieldAlert } from 'lucide-react';

type Status = 'UNVERIFIED' | 'EVIDENCE_RECORDED' | 'VERIFIED' | 'BLOCKED';

type Task = { id: number; level: string; title: string; proof: string };

const tasks: Task[] = [
  ['FOUNDATION','Enable required GCP APIs'],['FOUNDATION','Create Vertex AI service account'],['FOUNDATION','Set up private VPC'],['FOUNDATION','Configure Cloud NAT'],
  ['STORAGE','Create model-artifact GCS bucket'],['STORAGE','Set bucket lifecycle policies'],['STORAGE','Configure bucket CORS'],['STORAGE','Enable bucket versioning'],
  ['MODEL REGISTRY','Register model'],['MODEL REGISTRY','Configure container image'],['MODEL REGISTRY','Set environment variables'],['MODEL REGISTRY','Define serving signature'],
  ['ENDPOINT','Create Vertex AI endpoint'],['ENDPOINT','Configure endpoint network'],['ENDPOINT','Enable logging and monitoring'],['ENDPOINT','Enable request-response logging'],
  ['DEPLOYMENT','Deploy model'],['DEPLOYMENT','Configure autoscaling'],['DEPLOYMENT','Configure traffic split'],['DEPLOYMENT','Verify prediction caching'],
  ['MONITORING','Create Cloud Monitoring dashboards'],['MONITORING','Configure alerting policies'],['MONITORING','Enable Cloud Logging'],['MONITORING','Enable error reporting'],
  ['SECURITY','Configure IAM policies'],['SECURITY','Enable VPC Service Controls'],['SECURITY','Configure Cloud Armor'],['SECURITY','Configure audit logging'],
  ['PRODUCTION','Perform load testing'],['PRODUCTION','Set up CI/CD'],['PRODUCTION','Configure budget alerts'],['PRODUCTION','Publish runbook and SLAs'],
  ['COMMAND CENTER','Trace source commit to runtime'],['COMMAND CENTER','Verify dev/staging/prod parity'],['COMMAND CENTER','Verify database read/write/read-back'],['COMMAND CENTER','Verify realtime event delivery'],['COMMAND CENTER','Verify authentication/authorization'],['COMMAND CENTER','Verify analytics truth path'],['COMMAND CENTER','Verify AI execution path'],['COMMAND CENTER','Verify rollback path'],['COMMAND CENTER','Verify critical end-to-end path'],['COMMAND CENTER','Pass production readiness gate']
].map(([level, title], i) => ({ id: i + 1, level, title, proof: 'Execute the real check, capture evidence, compare expected vs actual, then accept verification.' }));

export function LaunchRoadmap() {
  const [status, setStatus] = useState<Record<number, Status>>({});
  const [evidence, setEvidence] = useState<Record<number, string>>({});
  const [filter, setFilter] = useState<'ALL' | Status>('ALL');
  const verified = useMemo(() => tasks.filter(t => status[t.id] === 'VERIFIED').length, [status]);
  const evidenceCount = useMemo(() => tasks.filter(t => status[t.id] === 'EVIDENCE_RECORDED').length, [status]);
  const blocked = useMemo(() => tasks.filter(t => status[t.id] === 'BLOCKED').length, [status]);
  const visible = tasks.filter(t => filter === 'ALL' || (status[t.id] ?? 'UNVERIFIED') === filter);
  const pct = Math.round((verified / 42) * 100);

  const recordEvidence = (id: number) => {
    if (!evidence[id]?.trim()) return;
    setStatus(s => ({ ...s, [id]: 'EVIDENCE_RECORDED' }));
  };

  return <section className="space-y-5">
    <div className="rounded-2xl border border-white/10 bg-black/20 p-6">
      <div className="flex flex-col gap-5 lg:flex-row lg:items-end lg:justify-between">
        <div><p className="text-xs font-mono uppercase tracking-[.25em] text-muted-foreground">GODSPEED / TRUTH GATE</p><h2 className="mt-2 text-2xl font-semibold">42-task launch roadmap</h2><p className="mt-2 max-w-3xl text-sm text-muted-foreground">No button can manufacture GREEN. VERIFIED requires real execution evidence. Evidence recorded is not the same as verified.</p></div>
        <div className="min-w-[250px]"><div className="mb-2 flex justify-between text-xs font-mono"><span>{verified}/42 VERIFIED</span><strong>{pct}%</strong></div><div className="h-2 rounded-full bg-white/10"><div className="h-full rounded-full bg-emerald-400" style={{width:`${pct}%`}} /></div><div className="mt-2 text-[11px] font-mono text-muted-foreground">Evidence {evidenceCount} · Blocked {blocked}</div></div>
      </div>
    </div>
    <div className="flex flex-wrap gap-2">{(['ALL','UNVERIFIED','EVIDENCE_RECORDED','VERIFIED','BLOCKED'] as const).map(x => <button key={x} onClick={() => setFilter(x)} className="rounded-full border border-white/10 px-3 py-1.5 text-[11px] font-mono">{x}</button>)}</div>
    <div className="space-y-3">{visible.map(t => { const s = status[t.id] ?? 'UNVERIFIED'; return <article key={t.id} className="rounded-xl border border-white/10 bg-black/10 p-4"><div className="flex flex-col gap-3 lg:flex-row lg:items-start lg:justify-between"><div className="flex gap-3"><div>{s==='VERIFIED'?<CheckCircle2 className="h-5 w-5 text-emerald-400"/>:s==='BLOCKED'?<ShieldAlert className="h-5 w-5 text-amber-400"/>:s==='EVIDENCE_RECORDED'?<FileCheck2 className="h-5 w-5 text-sky-400"/>:<Circle className="h-5 w-5 text-white/30"/>}</div><div><div className="text-[10px] font-mono uppercase tracking-widest text-muted-foreground">{t.level} · TASK {t.id}</div><h3 className="mt-1 text-sm font-medium">{t.title}</h3><p className="mt-1 text-xs text-muted-foreground">{t.proof}</p></div></div><div className="flex w-full max-w-xl gap-2"><input value={evidence[t.id]??''} onChange={e=>setEvidence(v=>({...v,[t.id]:e.target.value}))} placeholder="Evidence: run ID, log, commit, URL…" className="min-w-0 flex-1 rounded-lg border border-white/10 bg-black/20 px-3 py-2 text-xs"/><button disabled={!evidence[t.id]?.trim()} onClick={()=>recordEvidence(t.id)} className="rounded-lg border border-white/10 px-3 py-2 text-xs disabled:opacity-30">Record evidence</button></div></div><div className="mt-3 border-t border-white/5 pt-3 text-[10px] font-mono text-muted-foreground">STATE: {s} · {s==='EVIDENCE_RECORDED'?'Evidence exists; verification still required':'No verification claim'}</div></article>})}</div>
  </section>;
}
