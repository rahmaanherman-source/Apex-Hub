import { useMemo, useState } from 'react';
import { Activity, AlertTriangle, ArrowUpRight, Bot, Boxes, CheckCircle2, Circle, Cloud, CreditCard, Database, ExternalLink, Github, Globe2, HardDrive, LayoutDashboard, LockKeyhole, Play, Search, Server, Settings, ShieldCheck, ShoppingBag, Terminal, WalletCards, Zap, ListChecks } from 'lucide-react';
import { LaunchRoadmap } from './components/LaunchRoadmap';

type Status = 'VERIFIED' | 'OBSERVED' | 'AVAILABLE' | 'BLOCKED' | 'NOT_NEEDED';
type Provider = { name: string; category: string; priority: 'P0' | 'P1' | 'P2'; status: Status; detail: string; url: string; icon: typeof Cloud; capabilities: string[] };

const providers: Provider[] = [
  { name: 'Stripe', category: 'Payments / Revenue', priority: 'P0', status: 'AVAILABLE', detail: 'Private account requires authenticated connection before live verification.', url: 'https://dashboard.stripe.com/settings/user', icon: CreditCard, capabilities: ['Products', 'Prices', 'Checkout', 'Webhooks', 'Revenue'] },
  { name: 'Google Cloud', category: 'AI / Data / Cloud', priority: 'P0', status: 'AVAILABLE', detail: 'Cloud account is an external capability provider; connect project credentials through Vault.', url: 'https://console.cloud.google.com/', icon: Cloud, capabilities: ['BigQuery', 'Vertex AI', 'Cloud Run', 'Storage', 'Pub/Sub', 'IAM'] },
  { name: 'BigQuery', category: 'Analytics / Warehouse', priority: 'P0', status: 'AVAILABLE', detail: 'Ready for project/dataset discovery once Google Cloud authorization is connected.', url: 'https://console.cloud.google.com/bigquery', icon: Database, capabilities: ['Datasets', 'Queries', 'Jobs', 'Results', 'Revenue Analytics'] },
  { name: 'Vertex AI', category: 'AI / Agents / Models', priority: 'P0', status: 'AVAILABLE', detail: 'Execution remains unverified until an authorized project and model operation succeed.', url: 'https://console.cloud.google.com/vertex-ai', icon: Bot, capabilities: ['Models', 'Agents', 'Embeddings', 'Evaluation'] },
  { name: 'Cloud Run', category: 'Apps / Agents / APIs', priority: 'P0', status: 'AVAILABLE', detail: 'Deployment and live endpoint health must be tested before GREEN.', url: 'https://console.cloud.google.com/run', icon: Server, capabilities: ['Services', 'Revisions', 'HTTPS', 'Health', 'Deployments'] },
  { name: 'GitHub', category: 'Code / Repos / CI', priority: 'P1', status: 'OBSERVED', detail: 'Repository administration access is observed; CI/live application verification is separate.', url: 'https://github.com/rahmaanherman-source/Apex-Hub', icon: Github, capabilities: ['Repositories', 'Commits', 'Issues', 'PRs', 'Actions'] },
  { name: 'Vercel', category: 'Hosting / Frontend', priority: 'P1', status: 'OBSERVED', detail: 'Deployment existence does not equal live availability. 404 observations remain diagnostic.', url: 'https://vercel.com/dashboard', icon: Globe2, capabilities: ['Projects', 'Deployments', 'Domains', 'Logs'] },
  { name: 'Cloudflare', category: 'DNS / CDN / Security', priority: 'P1', status: 'AVAILABLE', detail: 'Connect zone and account authorization through the APEX connector layer.', url: 'https://dash.cloudflare.com/', icon: ShieldCheck, capabilities: ['DNS', 'Workers', 'Zones', 'SSL', 'Security'] },
  { name: 'Shopify', category: 'Commerce / Store', priority: 'P1', status: 'AVAILABLE', detail: 'Store authorization and live order/product checks are required for VERIFIED.', url: 'https://admin.shopify.com/', icon: ShoppingBag, capabilities: ['Products', 'Orders', 'Inventory', 'Checkout', 'Webhooks'] },
  { name: 'PayPal', category: 'Payments', priority: 'P1', status: 'AVAILABLE', detail: 'Business account connection and transaction verification are pending.', url: 'https://www.paypal.com/businessmanage/', icon: WalletCards, capabilities: ['Payments', 'Transactions', 'Webhooks'] },
  { name: 'Printify', category: 'Print / Fulfillment', priority: 'P1', status: 'AVAILABLE', detail: 'Connect shop and verify catalog/order/fulfillment execution.', url: 'https://printify.com/app/', icon: Boxes, capabilities: ['Catalog', 'Products', 'Orders', 'Fulfillment'] },
  { name: 'Supabase', category: 'Database / Auth / Storage', priority: 'P1', status: 'OBSERVED', detail: 'Connector and repository references exist; live project health requires authenticated verification.', url: 'https://supabase.com/dashboard', icon: HardDrive, capabilities: ['Postgres', 'Auth', 'Storage', 'Edge Functions'] },
  { name: 'OpenAI', category: 'AI / Models / Tools', priority: 'P1', status: 'AVAILABLE', detail: 'Provider capability is available; credentials remain Vault-controlled.', url: 'https://platform.openai.com/', icon: Zap, capabilities: ['Models', 'Responses', 'Tools', 'Agents'] },
  { name: 'Microsoft Azure', category: 'Cloud / AI / Services', priority: 'P2', status: 'BLOCKED', detail: 'No connected runtime capability is currently verified in this APEX environment.', url: 'https://portal.azure.com/', icon: Server, capabilities: ['Azure AI', 'Graph', 'Entra', 'Cloud'] },
];

const commands = ['apex connectors list', 'apex connectors health stripe', 'apex connectors verify bigquery', 'apex connectors evidence google-cloud'];
const statusMeta: Record<Status, { label: string; tone: string; icon: typeof Circle }> = {
  VERIFIED: { label: 'VERIFIED', tone: 'verified', icon: CheckCircle2 },
  OBSERVED: { label: 'OBSERVED', tone: 'observed', icon: Activity },
  AVAILABLE: { label: 'AVAILABLE', tone: 'available', icon: Circle },
  BLOCKED: { label: 'BLOCKED', tone: 'blocked', icon: AlertTriangle },
  NOT_NEEDED: { label: 'NOT NEEDED', tone: 'muted', icon: Circle },
};

function openExternal(url: string) { window.open(url, '_blank', 'noopener,noreferrer'); }

export default function App() {
  const [selected, setSelected] = useState('Stripe');
  const [filter, setFilter] = useState('ALL');
  const [query, setQuery] = useState('');
  const [view, setView] = useState<'dashboard' | 'launch'>('dashboard');
  const selectedProvider = providers.find((provider) => provider.name === selected) ?? providers[0];
  const SelectedIcon = selectedProvider.icon;
  const visibleProviders = useMemo(() => providers.filter((provider) => {
    const matchesFilter = filter === 'ALL' || provider.status === filter || provider.priority === filter;
    const haystack = `${provider.name} ${provider.category} ${provider.capabilities.join(' ')}`.toLowerCase();
    return matchesFilter && haystack.includes(query.toLowerCase());
  }), [filter, query]);
  const counts = useMemo(() => ({
    verified: providers.filter((p) => p.status === 'VERIFIED').length,
    observed: providers.filter((p) => p.status === 'OBSERVED').length,
    available: providers.filter((p) => p.status === 'AVAILABLE').length,
    blocked: providers.filter((p) => p.status === 'BLOCKED').length,
  }), []);

  return (
    <main className="app-shell">
      <aside className="sidebar">
        <div className="brand"><div className="brand-mark">△</div><div><strong>APEX HUB</strong><span>COMMAND CENTER</span></div></div>
        <nav>
          <button className={view === 'dashboard' ? 'nav-item active' : 'nav-item'} onClick={() => setView('dashboard')}><LayoutDashboard size={17} /> Dashboard</button>
          <button className="nav-item" onClick={() => setFilter('ALL')}><Boxes size={17} /> Connectors</button>
          <button className="nav-item" onClick={() => setSelected('Stripe')}><CreditCard size={17} /> Revenue</button>
          <button className="nav-item" onClick={() => setSelected('Google Cloud')}><Cloud size={17} /> Google Cloud</button>
          <button className="nav-item" onClick={() => setSelected('GitHub')}><Github size={17} /> GitHub</button>
          <button className="nav-item" onClick={() => setSelected('OpenAI')}><Bot size={17} /> Agents</button>
          <button className={view === 'launch' ? 'nav-item active' : 'nav-item'} onClick={() => setView('launch')}><ListChecks size={17} /> Launch Roadmap</button>
          <button className="nav-item" onClick={() => setFilter('BLOCKED')}><AlertTriangle size={17} /> Diagnostics</button>
          <button className="nav-item"><Settings size={17} /> Settings</button>
        </nav>
        <div className="sidebar-bottom"><div className="security-badge"><LockKeyhole size={16} /><span>NO FAKE GREEN</span></div><small>Truth Gate: evidence first.<br />LLM: proposal only.</small></div>
      </aside>

      <section className="workspace">
        <header className="topbar">
          <div><p className="eyebrow">APEX / KERNEL</p><h1>{view === 'launch' ? 'Launch Roadmap' : 'Command Center'}</h1></div>
          <div className="top-actions">
            {view === 'dashboard' && <div className="search"><Search size={16} /><input value={query} onChange={(event) => setQuery(event.target.value)} placeholder="Search providers, capabilities…" /></div>}
            <button className="icon-button" title="Open GitHub" onClick={() => openExternal('https://github.com/rahmaanherman-source/Apex-Hub')}><Github size={18} /></button>
            <button className="icon-button" title="Open Google Cloud" onClick={() => openExternal('https://console.cloud.google.com/')}><Cloud size={18} /></button>
            <button className="icon-button" title="Open Stripe" onClick={() => openExternal('https://dashboard.stripe.com/settings/user')}><CreditCard size={18} /></button>
          </div>
        </header>

        {view === 'launch' ? <LaunchRoadmap /> : <>
          <section className="hero-panel">
            <div><p className="eyebrow">GODSPEED / EXECUTION SURFACE</p><h2>Everything important.<br /><span>One command surface.</span></h2><p>APEX determines what is available, opens the real service, executes only inside authority, and refuses to manufacture GREEN.</p></div>
            <div className="hero-actions"><button className="primary-button" onClick={() => setView('launch')}><Play size={17} /> RUN LAUNCH AUDIT</button><button className="secondary-button" onClick={() => openExternal('https://github.com/rahmaanherman-source/Apex-Hub')}><Github size={17} /> REPOSITORY</button></div>
          </section>

          <section className="stat-grid">
            <button onClick={() => setFilter('VERIFIED')} className="stat-card verified"><span>CONNECTED + VERIFIED</span><strong>{counts.verified}</strong><small>Actual proof only</small></button>
            <button onClick={() => setFilter('OBSERVED')} className="stat-card observed"><span>OBSERVED / NOT GREEN</span><strong>{counts.observed}</strong><small>Evidence exists; verification separate</small></button>
            <button onClick={() => setFilter('AVAILABLE')} className="stat-card available"><span>AVAILABLE / NOT CONNECTED</span><strong>{counts.available}</strong><small>Capability exists</small></button>
            <button onClick={() => setFilter('BLOCKED')} className="stat-card blocked"><span>BLOCKED</span><strong>{counts.blocked}</strong><small>Needs a capability or authorization</small></button>
          </section>

          <section id="provider-inventory" className="content-grid">
            <div className="inventory-panel">
              <div className="section-head"><div><p className="eyebrow">PROVIDER INVENTORY</p><h3>APEX Arsenal</h3></div><div className="filter-row">{['ALL', 'P0', 'P1', 'VERIFIED', 'OBSERVED', 'AVAILABLE', 'BLOCKED'].map((item) => <button key={item} className={filter === item ? 'filter active' : 'filter'} onClick={() => setFilter(item)}>{item}</button>)}</div></div>
              <div className="provider-list">{visibleProviders.map((provider) => { const Icon = provider.icon; const StatusIcon = statusMeta[provider.status].icon; return <button key={provider.name} className={selected === provider.name ? 'provider-row selected' : 'provider-row'} onClick={() => setSelected(provider.name)}><span className="provider-avatar"><Icon size={19} /></span><span className="provider-main"><strong>{provider.name}</strong><small>{provider.category}</small></span><span className={`status-pill ${statusMeta[provider.status].tone}`}><StatusIcon size={12} /> {statusMeta[provider.status].label}</span><span className={`priority ${provider.priority.toLowerCase()}`}>{provider.priority}</span><ArrowUpRight size={15} /></button>; })}</div>
            </div>

            <aside className="detail-panel">
              <div className="detail-head"><div className="provider-avatar large"><SelectedIcon size={27} /></div><div><p className="eyebrow">CAPABILITY PROVIDER</p><h3>{selectedProvider.name}</h3><span>{selectedProvider.category}</span></div><button className="icon-button" title={`Open ${selectedProvider.name}`} onClick={() => openExternal(selectedProvider.url)}><ExternalLink size={18} /></button></div>
              <div className={`detail-status ${statusMeta[selectedProvider.status].tone}`}><span>{statusMeta[selectedProvider.status].label}</span><small>{selectedProvider.priority} · {selectedProvider.category}</small></div>
              <p className="detail-copy">{selectedProvider.detail}</p>
              <div className="capability-grid">{selectedProvider.capabilities.map((capability) => <button key={capability} onClick={() => openExternal(selectedProvider.url)}><CheckCircle2 size={14} />{capability}<ArrowUpRight size={13} /></button>)}</div>
              <button className="open-service" onClick={() => openExternal(selectedProvider.url)}><ExternalLink size={16} /> OPEN {selectedProvider.name.toUpperCase()} <span>↗</span></button>
              <div className="gate-list">{['DISCOVERED', 'AVAILABLE', 'AUTHORIZED', 'CONNECTED', 'HEALTHY', 'EXECUTABLE', 'VERIFIED'].map((gate, index) => <div key={gate} className={index < (selectedProvider.status === 'VERIFIED' ? 7 : selectedProvider.status === 'OBSERVED' ? 1 : 2) ? 'gate passed' : 'gate'}><span>{index + 1}</span><strong>{gate}</strong><small>{index === 6 && selectedProvider.status !== 'VERIFIED' ? 'NO GREEN' : index < 2 ? 'EVIDENCE' : 'PENDING'}</small></div>)}</div>
            </aside>
          </section>

          <section className="lower-grid">
            <div className="console-panel"><div className="section-head"><div><p className="eyebrow">APEX TERMINAL</p><h3>Command shortcuts</h3></div><Terminal size={19} /></div><div className="terminal"><div className="terminal-title"><span /><span /><span /><small>apex://kernel/commandbus</small></div>{commands.map((command) => <button key={command} onClick={() => navigator.clipboard?.writeText(command)}><span>$</span>{command}<ArrowUpRight size={13} /></button>)}</div></div>
            <div className="revenue-panel"><div className="section-head"><div><p className="eyebrow">P0 / MONEY PATH</p><h3>Revenue flow</h3></div><CreditCard size={19} /></div><div className="flow"><span><ShoppingBag size={18} />Product</span><b>→</b><span><CreditCard size={18} />Stripe</span><b>→</b><span><Zap size={18} />Payment</span><b>→</b><span><Activity size={18} />Webhook</span><b>→</b><span><Database size={18} />APEX Record</span></div><div className="revenue-note"><AlertTriangle size={15} /><span>LIVE REVENUE IS NOT CLAIMED until checkout, event delivery, and revenue-record reconciliation are actually verified.</span></div><button className="open-service compact" onClick={() => openExternal('https://dashboard.stripe.com/settings/user')}><CreditCard size={15} /> OPEN STRIPE</button></div>
          </section>
        </>}
        <footer className="footer"><span>APEX HUB · COMMAND CENTER</span><span>STATE: EVIDENCE-DRIVEN · LLM: PROPOSAL ONLY · NO FAKE GREEN</span></footer>
      </section>
    </main>
  );
}
