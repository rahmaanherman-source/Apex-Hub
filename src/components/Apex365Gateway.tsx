import { ArrowUpRight, Bot, Cloud, Github, Globe2, LockKeyhole, Server, ShoppingBag, Sparkles } from 'lucide-react';

type GatewayAction = 'shopify' | 'vercel' | 'github' | 'ai-studio' | 'overview';

type GatewayProps = { onAction: (action: GatewayAction) => void };

const surfaces = [
  { key: 'shopify' as const, eyebrow: 'COMMERCE', title: 'APEX 365 Storefront', copy: 'Customer commerce stays on the Shopify storefront while APEX remains the front door.', icon: ShoppingBag, tone: 'gold', state: 'LIVE ROUTE' },
  { key: 'vercel' as const, eyebrow: 'DEVELOPER INFRASTRUCTURE', title: 'Vercel Apps', copy: 'Reach deployed APEX applications without making the hosting provider the destination.', icon: Globe2, tone: 'violet', state: 'CONTROLLED HANDOFF' },
  { key: 'github' as const, eyebrow: 'ENGINEERING', title: 'GitHub Workspace', copy: 'Source, issues, pull requests, and delivery remain behind an explicit engineering handoff.', icon: Github, tone: 'blue', state: 'OBSERVED' },
  { key: 'ai-studio' as const, eyebrow: 'AI / MODELS', title: 'Google AI Studio', copy: 'Open the real AI Studio workspace. Authorization and model execution remain evidence-gated.', icon: Bot, tone: 'green', state: 'AVAILABLE' },
];

export function Apex365Gateway({ onAction }: GatewayProps) {
  return (
    <div className="gateway-view">
      <section className="gateway-hero">
        <div className="gateway-hero-copy">
          <p className="eyebrow">APEX LIFE GLOBAL / FRONT DOOR</p>
          <h2>One front door.<br /><span>Every capability underneath.</span></h2>
          <p>APEX 365 is the gateway and control layer for commerce, developer infrastructure, engineering, and AI. Customers do not need to know which provider powers the next step.</p>
          <div className="gateway-actions">
            <button className="primary-button" onClick={() => onAction('shopify')}><ShoppingBag size={17} /> ENTER APEX 365</button>
            <button className="secondary-button" onClick={() => onAction('overview')}><Sparkles size={17} /> WHOLE PICTURE</button>
          </div>
        </div>
        <div className="gateway-orbit" aria-label="APEX 365 capability map">
          <div className="orbit-ring ring-one" />
          <div className="orbit-ring ring-two" />
          <div className="orbit-core">
            <span>APEX</span>
            <strong>365</strong>
            <small>CONTROL LAYER</small>
          </div>
          <span className="orbit-node node-top"><Cloud size={15} /> AI</span>
          <span className="orbit-node node-right"><Server size={15} /> APPS</span>
          <span className="orbit-node node-bottom"><ShoppingBag size={15} /> COMMERCE</span>
        </div>
      </section>
      <section className="gateway-strip">
        <div>
          <LockKeyhole size={16} />
          <strong>TRUTH GATE</strong>
          <span>Provider boundaries stay visible to operators. Customer journeys stay simple.</span>
        </div>
        <button className="text-button" onClick={() => onAction('overview')}>VIEW ARCHITECTURE <ArrowUpRight size={14} /></button>
      </section>
      <section className="gateway-section">
        <div className="section-head">
          <div>
            <p className="eyebrow">CAPABILITY ROUTES</p>
            <h3>Choose the work, not the provider</h3>
          </div>
          <span className="gateway-count">{surfaces.length} surfaces · 1 runtime</span>
        </div>
        <div className="gateway-grid">
          {surfaces.map(({ key, eyebrow, title, copy, icon: Icon, tone, state }) => (
            <button className={`gateway-card ${tone}`} key={key} onClick={() => onAction(key)}>
              <span className="gateway-card-icon"><Icon size={21} /></span>
              <span className="gateway-card-body">
                <small>{eyebrow}</small>
                <strong>{title}</strong>
                <span>{copy}</span>
              </span>
              <span className="gateway-card-foot">
                <em>{state}</em>
                <ArrowUpRight size={15} />
              </span>
            </button>
          ))}
        </div>
      </section>
      <section className="gateway-footer-note">
        <Cloud size={17} />
        <span><strong>Google AI Studio is linked, not duplicated.</strong> Use the real workspace for model work; APEX 365 remains the orchestration surface.</span>
        <button className="text-button" onClick={() => onAction('ai-studio')}>OPEN AI STUDIO <ArrowUpRight size={14} /></button>
      </section>
    </div>
  );
}

export type { GatewayAction };
