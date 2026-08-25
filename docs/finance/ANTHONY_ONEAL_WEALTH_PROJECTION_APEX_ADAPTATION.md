# Anthony O'Neal Wealth Projection — APEX Adaptation

**Status:** Integrated research/design baseline
**Source:** Anthony O'Neal Wealth Calculator / Wealth Projection Calculator

## What the tool does

Anthony O'Neal's public Wealth Calculator asks for:

- Current age
- Planned retirement age
- Current investments
- Expected annual return
- Monthly contribution

It projects the future investment value and separates the result into **initial balance, contributions, and growth**. O'Neal's tool also states a 15% paycheck-investing guideline. citeturn1view0

## APEX principle

We are adding this as a **financial-freedom projection instrument**, not a promise of investment returns.

The question changes from:

> “How much money do I have today?”

to:

> “If I consistently deploy verified capital, what can compounding potentially build by the date I choose?”

## Core projection model

For a starting portfolio `P`, monthly contribution `C`, annual nominal return `r`, and `n` months:

```text
monthly_rate = r / 12
months = (retirement_age - current_age) × 12

future_value =
    P × (1 + monthly_rate)^months
    + C × [((1 + monthly_rate)^months - 1) / monthly_rate]
```

If the annual return is 0%, the second term becomes simply:

```text
C × months
```

The model should report:

```text
Initial Balance
+ Total Contributions
+ Estimated Growth
= Projected Future Value
```

## APEX upgrade: do not use one return assumption

The public tool accepts one annual-return assumption. APEX should preserve that simple view but add scenario analysis:

- Conservative
- Base
- Optimistic

The user should be able to see how sensitive the outcome is to return assumptions rather than treating one percentage as guaranteed.

## APEX upgrade: connect income to contributions

Instead of only asking for a monthly contribution, APEX can calculate the contribution from verified income:

```text
verified monthly take-home income
× chosen investment rate
= planned monthly investment
```

The 15% figure can be presented as a reference point from O'Neal's public tool, while the actual APEX rate remains configurable based on the user's verified budget, reserves, debt, taxes, business needs, and goals. citeturn1view0

## APEX upgrade: business-owner version

For APEX, the calculator should eventually support two distinct capital streams:

### Personal wealth engine

```text
Personal verified income
→ emergency reserve
→ debt reduction where applicable
→ retirement/investment contribution
→ long-term assets
```

### Business wealth engine

```text
Verified business revenue
→ operating reserve
→ taxes/obligations
→ reinvestment
→ infrastructure upgrades
→ owner distribution
→ personal investment
```

The two ledgers must not be mixed merely because both contribute to net worth.

## Next-Upgrade Engine

The wealth projection should be paired with the APEX stability framework already documented in:

`docs/finance/ANTHONY_ONEAL_STOP_LIVING_PAYCHECK_TO_PAYCHECK_APEX_ADAPTATION.md`

Before deploying capital into an upgrade, APEX evaluates:

1. **Stability:** Does it strengthen the base?
2. **Leak removal:** Does it reduce unnecessary recurring cost or expensive debt?
3. **Revenue capacity:** Does it measurably increase verified earning capacity?
4. **Risk reduction:** Does it reduce security, operational, or compliance exposure?
5. **Compounding:** Does it improve long-term asset growth?

The upgrade with the strongest verified value per dollar wins.

## No-fake-green financial states

Every financial projection must distinguish:

- `reported` — user/system says funds exist
- `verified` — transaction/account evidence confirms funds
- `committed` — already assigned to an obligation
- `reserve` — intentionally protected
- `deployable` — available for an approved action
- `invested` — actually deployed into an investment
- `projected` — mathematical estimate only

A projection is **not an asset**.

A projected return is **not revenue**.

A projected retirement balance is **not guaranteed wealth**.

## Suggested APEX dashboard

```text
FINANCIAL FREEDOM PULSE

Current age:                 [verified/input]
Target freedom age:          [input]
Verified investments:        [$]
Monthly investment:          [$]
Investment rate:             [%]
Years remaining:             [calculated]

CONSERVATIVE                  BASE                  OPTIMISTIC
Projected value               Projected value       Projected value
Initial                       Initial               Initial
Contributions                 Contributions         Contributions
Growth                        Growth                Growth

Emergency reserve:            [$]
High-cost debt:               [$]
Business reserve:             [$]
Deployable upgrade capital:   [$]
Verified monthly revenue:     [$]
Verified monthly expenses:    [$]
```

## Guardrails

- Never imply a market return is guaranteed.
- Show nominal dollars unless inflation adjustment is explicitly enabled.
- Clearly label projections as estimates.
- Keep personal and business funds separate.
- Do not let a projected investment balance authorize current spending.
- Require verified balances before treating current assets as inputs to an execution decision.
- Preserve source attribution to O'Neal's public calculator.

## Strategic use

This becomes part of the APEX **Financial Freedom Arsenal** alongside the stabilization framework.

The sequence is:

```text
EARN
  ↓
VERIFY
  ↓
STABILIZE
  ↓
PROTECT
  ↓
REMOVE LEAKS / DEBT
  ↓
FUND OPERATIONS
  ↓
SELECT NEXT UPGRADE
  ↓
VERIFY RESULTS
  ↓
INVEST CONSISTENTLY
  ↓
COMPOUND
  ↓
FINANCIAL FREEDOM
```

**Doctrine:** The objective is not to create a system where the owner must work forever to maintain it. The objective is to build a system in which disciplined capital deployment progressively buys back time and increases durable asset ownership.

## Source

Anthony O'Neal, Wealth Calculator / Wealth Projection Calculator. The public calculator documents the inputs and describes the projection purpose; its public page states the 15% paycheck investment recommendation and notes that historical S&P 500 returns have been roughly 10–12% over a 30-year period. Those historical figures must not be treated as a guaranteed future return. citeturn1view0
