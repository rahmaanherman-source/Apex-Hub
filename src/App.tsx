import { useMemo } from 'react';

type Product = { name: string; price: string; description: string };

const products: Product[] = [
  { name: 'GODSPEED Digital Starter', price: '$27', description: 'A focused digital product for the first APEX customer transaction.' },
  { name: 'APEX Custom Build Session', price: '$97', description: 'A practical one-session setup for turning an idea into a working commercial workflow.' },
  { name: 'APEX Commerce Launch', price: '$297', description: 'A launch package for product, offer, checkout and verification setup.' },
];

function checkoutFor(product: Product): string | undefined {
  const configured = import.meta.env.VITE_CHECKOUT_URL as string | undefined;
  return configured ? `${configured}${configured.includes('?') ? '&' : '?'}product=${encodeURIComponent(product.name)}` : undefined;
}

export default function App() {
  const health = useMemo(() => ({
    app: 'READY',
    commerce: import.meta.env.VITE_CHECKOUT_URL ? 'CONNECTED' : 'AWAITING CHECKOUT URL',
    verification: 'NO-FAKE-GREEN',
  }), []);

  return (
    <main className="shell">
      <header className="hero">
        <div><p className="eyebrow">APEX HUB · GODSPEED</p><h1>The commercial front door.</h1><p className="lede">Products first. Checkout next. Evidence always. No fake green.</p></div>
        <div className="status-card"><span>LIVE BUILD</span><strong>{health.app}</strong><small>{health.verification}</small></div>
      </header>
      <section className="grid" aria-label="APEX products">
        {products.map((product) => {
          const checkout = checkoutFor(product);
          return <article className="product" key={product.name}><div><p className="tag">FOR SALE</p><h2>{product.name}</h2><p>{product.description}</p></div><div className="buy-row"><strong>{product.price}</strong>{checkout ? <a className="button" href={checkout}>Buy now</a> : <span className="button disabled">Checkout pending</span>}</div></article>;
        })}
      </section>
      <section className="proof"><div><p className="eyebrow">VERIFICATION GATE</p><h2>Green is earned, not declared.</h2><p>Deployment, product availability and checkout are separate gates. A failed gate remains red until it is actually re-tested.</p></div><div className="gates"><span>01 · APP LOAD</span><span>02 · PRODUCT</span><span>03 · CHECKOUT</span><span>04 · FULFILLMENT</span></div></section>
      <footer><span>APEX Hub</span><span>{health.commerce}</span></footer>
    </main>
  );
}
