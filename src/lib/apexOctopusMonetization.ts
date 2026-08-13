export type LaneStatus = 'SELL_NOW' | 'MAKE_SELLABLE' | 'BUILD_IN_BACKGROUND' | 'BLOCKED' | 'AUDIT';

export interface OctopusHead {
  headId: string;
  name: string;
  provider: string;
  category: LaneStatus;
  monetizationReady: boolean;
  standaloneCapable: boolean;
  deepLink?: string;
}

export interface RevenueEvidence {
  eventId: string;
  headId: string;
  provider: string;
  amountInCents: number;
  currency: string;
  entityId: string;
  evidenceHash: string;
  observedAt: string;
  verified: boolean;
  source: 'PROVIDER' | 'TEST';
}

export const APEX_OCTOPUS_HEADS: readonly OctopusHead[] = [
  { headId: 'HEAD_1_STRIPE', name: 'Stripe Payments', provider: 'Stripe', category: 'SELL_NOW', monetizationReady: true, standaloneCapable: true },
  { headId: 'HEAD_2_SHOPIFY', name: 'Shopify Storefront', provider: 'Shopify', category: 'SELL_NOW', monetizationReady: true, standaloneCapable: true },
  { headId: 'HEAD_3_CANVA', name: 'Canva / Creative Media', provider: 'Canva', category: 'SELL_NOW', monetizationReady: true, standaloneCapable: true },
  { headId: 'HEAD_4_GABBY', name: 'Gabby AI Services', provider: 'APEX', category: 'SELL_NOW', monetizationReady: true, standaloneCapable: true },
  { headId: 'HEAD_5_FULFILLMENT', name: 'Print / Fulfillment', provider: 'Fulfillment', category: 'MAKE_SELLABLE', monetizationReady: false, standaloneCapable: false },
  { headId: 'HEAD_6_GCLOUD', name: 'Google Cloud / BigQuery', provider: 'Google Cloud', category: 'BUILD_IN_BACKGROUND', monetizationReady: false, standaloneCapable: false },
  { headId: 'HEAD_7_VAULT', name: 'Vault / Gatekeeper', provider: 'APEX', category: 'BUILD_IN_BACKGROUND', monetizationReady: false, standaloneCapable: false },
  { headId: 'HEAD_8_VERCEL', name: 'Vercel / Edge', provider: 'Vercel', category: 'BLOCKED', monetizationReady: false, standaloneCapable: false },
  { headId: 'HEAD_9_NO_FAKE_GREEN', name: 'NO FAKE GREEN', provider: 'APEX', category: 'AUDIT', monetizationReady: false, standaloneCapable: false }
] as const;

export function canMonetizeHead(head: OctopusHead): boolean {
  return head.category === 'SELL_NOW' && head.monetizationReady && head.standaloneCapable;
}

/** Revenue must originate from provider evidence. Test/simulated events are never revenue. */
export async function buildRevenueEvidence(
  input: Omit<RevenueEvidence, 'evidenceHash'> & { rawEvidence: string }
): Promise<RevenueEvidence> {
  if (!input.verified || input.source !== 'PROVIDER') {
    throw new Error('NO_FAKE_GREEN: revenue evidence must be provider-observed and verified.');
  }

  const digest = await crypto.subtle.digest('SHA-256', new TextEncoder().encode(input.rawEvidence));
  const evidenceHash = `sha256:${Array.from(new Uint8Array(digest), b => b.toString(16).padStart(2, '0')).join('')}`;

  return {
    eventId: input.eventId,
    headId: input.headId,
    provider: input.provider,
    amountInCents: input.amountInCents,
    currency: input.currency,
    entityId: input.entityId,
    evidenceHash,
    observedAt: input.observedAt,
    verified: true,
    source: 'PROVIDER'
  };
}
