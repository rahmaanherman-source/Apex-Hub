import { useMemo } from "react";

const destinations = [
  { name: "Shopify", action: "OPEN / SYNC / PUBLISH / VERIFY" },
  { name: "Stripe", action: "PAYMENTS / WEBHOOKS / VERIFY" },
  { name: "Vercel", action: "DEPLOYMENT / LOGS / REDEPLOY" },
  { name: "GitHub", action: "SOURCE / COMMITS / STATUS" },
  { name: "Google", action: "MERCHANT / ADS / AI STUDIO" },
];

export default function App() {
  const timestamp = useMemo(() => new Date().toISOString(), []);

  return (
    <main style={{ minHeight: "100vh", background: "#090909", color: "#f5f5f5", fontFamily: "Inter, system-ui, sans-serif", padding: 32 }}>
      <section style={{ maxWidth: 1100, margin: "0 auto" }}>
        <header style={{ display: "flex", justifyContent: "space-between", gap: 24, alignItems: "center", flexWrap: "wrap", marginBottom: 32 }}>
          <div>
            <div style={{ fontSize: 12, letterSpacing: 3, opacity: 0.7 }}>GODSPEED</div>
            <h1 style={{ margin: "8px 0", fontSize: 42 }}>APEX HUB</h1>
            <p style={{ margin: 0, opacity: 0.72 }}>One control plane. Many authorized doors. One verification standard.</p>
          </div>
          <div style={{ border: "1px solid #333", borderRadius: 12, padding: "12px 16px", fontSize: 13 }}>
            DEPLOYMENT SHELL ONLINE
          </div>
        </header>

        <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fit, minmax(210px, 1fr))", gap: 14 }}>
          {destinations.map((destination) => (
            <article key={destination.name} style={{ border: "1px solid #2a2a2a", borderRadius: 14, padding: 18, background: "#111" }}>
              <strong>{destination.name}</strong>
              <div style={{ marginTop: 10, fontSize: 12, opacity: 0.65 }}>{destination.action}</div>
              <div style={{ marginTop: 18, fontSize: 11, opacity: 0.5 }}>LIVE STATUS: REQUIRES PROVIDER VERIFICATION</div>
            </article>
          ))}
        </div>

        <section style={{ marginTop: 24, border: "1px solid #2a2a2a", borderRadius: 14, padding: 20, background: "#0f0f0f" }}>
          <h2 style={{ marginTop: 0 }}>P0 — Money Path</h2>
          <p style={{ opacity: 0.72 }}>Catalog → Shopify → Storefront → Checkout → Stripe → Webhook → APEX → Verified Order</p>
          <p style={{ fontSize: 12, opacity: 0.5 }}>Runtime observation: {timestamp}</p>
        </section>
      </section>
    </main>
  );
}
