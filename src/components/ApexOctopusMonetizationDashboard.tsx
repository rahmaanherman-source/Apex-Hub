import React, { useMemo, useState } from 'react';
import { APEX_OCTOPUS_HEADS, OctopusHead, canMonetizeHead } from '../lib/apexOctopusMonetization';

const laneLabel: Record<OctopusHead['category'], string> = {
  SELL_NOW: '🟢 SELL NOW',
  MAKE_SELLABLE: '🟡 MAKE SELLABLE',
  BUILD_IN_BACKGROUND: '🔵 BACKGROUND',
  BLOCKED: '🔴 BLOCKED',
  AUDIT: '🧪 AUDIT'
};

export function ApexOctopusMonetizationDashboard(): React.ReactElement {
  const [informative, setInformative] = useState(true);
  const [ownerView, setOwnerView] = useState(true);
  const [query, setQuery] = useState('');

  const heads = useMemo(() => {
    const q = query.trim().toLowerCase();
    if (!q) return APEX_OCTOPUS_HEADS;
    return APEX_OCTOPUS_HEADS.filter((h) => `${h.name} ${h.provider} ${h.headId}`.toLowerCase().includes(q));
  }, [query]);

  return (
    <section aria-label="APEX Octopus Heads Monetization" className="rounded-3xl border border-white/10 bg-[#080812]/95 p-4 text-white shadow-2xl backdrop-blur-xl sm:p-6">
      <header className="mb-5 flex flex-col gap-4 lg:flex-row lg:items-center lg:justify-between">
        <div>
          <div className="text-xs font-semibold uppercase tracking-[0.24em] text-white/50">APEX OWNER CONTROL</div>
          <h2 className="mt-1 text-2xl font-black tracking-tight">🐙 Octopus Heads</h2>
          <p className="mt-1 max-w-2xl text-sm text-white/60">Sell what is ready. Build what is unfinished. Verify every claim.</p>
        </div>
        <div className="flex flex-wrap gap-2">
          <button type="button" onClick={() => setOwnerView((v) => !v)} className="rounded-full border border-white/15 px-3 py-2 text-xs font-bold hover:bg-white/10">
            {ownerView ? 'OWNER / BUILDER' : 'CUSTOMER VIEW'}
          </button>
          <button type="button" onClick={() => setInformative((v) => !v)} className="rounded-full border border-white/15 px-3 py-2 text-xs font-bold hover:bg-white/10">
            APEX INFORMATIVE: {informative ? 'ON' : 'OFF'}
          </button>
        </div>
      </header>

      <div className="mb-5 flex flex-col gap-3 sm:flex-row">
        <input
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Ask Gabby: Stripe, Shopify, Vercel, BigQuery..."
          aria-label="Find an APEX capability"
          className="min-w-0 flex-1 rounded-2xl border border-white/10 bg-white/5 px-4 py-3 text-sm outline-none placeholder:text-white/35 focus:border-white/30"
        />
      </div>

      <div className="grid grid-cols-1 gap-3 sm:grid-cols-2 xl:grid-cols-3">
        {heads.map((head) => {
          const sellable = canMonetizeHead(head);
          return (
            <article key={head.headId} className="group rounded-2xl border border-white/10 bg-white/[0.035] p-4 transition hover:-translate-y-0.5 hover:bg-white/[0.06]">
              <div className="flex items-start justify-between gap-3">
                <div className="flex h-11 w-11 shrink-0 items-center justify-center rounded-xl border border-white/10 bg-white/5 text-lg" aria-hidden="true">
                  {head.provider.slice(0, 1)}
                </div>
                <span className="rounded-full border border-white/10 px-2 py-1 text-[10px] font-black tracking-wide text-white/70">{laneLabel[head.category]}</span>
              </div>
              <h3 className="mt-4 font-bold">{head.name}</h3>
              <p className="mt-1 text-xs text-white/45">{head.provider} · {head.headId}</p>

              {informative && (
                <div className="relative mt-3 rounded-xl border border-white/10 bg-black/20 p-3 text-xs leading-relaxed text-white/65">
                  <span className="mr-1">💭</span>
                  {sellable
                    ? 'This head is a monetization target. Provider verification is still required before APEX marks a real transaction GREEN.'
                    : head.category === 'BLOCKED'
                      ? 'This head is blocked. Fix the observed external dependency before treating it as live.'
                      : 'This head can continue in the background without stopping revenue-capable lanes.'}
                </div>
              )}

              <div className="mt-4 flex items-center justify-between gap-2">
                <span className="text-[11px] text-white/40">Truth state: UNVERIFIED until evidence</span>
                <button type="button" className="rounded-xl border border-white/15 px-3 py-2 text-xs font-bold hover:bg-white/10" onClick={() => window.dispatchEvent(new CustomEvent('apex:open-head', { detail: head.headId }))}>
                  OPEN →
                </button>
              </div>
            </article>
          );
        })}
      </div>

      {!ownerView && (
        <div className="mt-5 rounded-2xl border border-white/10 bg-white/[0.03] p-4 text-sm text-white/65">
          Customer view is active. Owner controls remain isolated from the customer projection.
        </div>
      )}
    </section>
  );
}

export default ApexOctopusMonetizationDashboard;
