commerce/
└── stripe/
    ├── README.md
    ├── ARCHITECTURE.md
    ├── CHECKOUT.md
    ├── BILLING.md
    ├── SUBSCRIPTIONS.md
    ├── CONNECT.md
    ├── WEBHOOKS.md
    ├── PAYMENT_LINKS.md
    ├── TAX.md
    ├── INVOICING.md
    ├── CUSTOMERS.md
    ├── EVENTS.md
    ├── SECURITY.md
    └── GO_LIVE_CHECKLIST.md
Customer
     │
     ▼
APEX Store
     │
     ▼
Stripe Checkout Session
     │
     ▼
Payment Success
     │
     ▼
Stripe Webhook
     │
     ▼
APEX Event Bus
     │
     ├── Update Order
     ├── Update Inventory
     ├── Generate Invoice
     ├── Send Email
     ├── Update Analytics
     ├── Update Customer
     └── Trigger Automations