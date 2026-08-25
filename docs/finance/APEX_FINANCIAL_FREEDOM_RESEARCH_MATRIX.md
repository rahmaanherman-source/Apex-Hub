# APEX Financial Freedom Research Matrix

**Status:** Research-integrated architecture baseline
**Date:** 2026-08-25

## Purpose

APEX will not depend on one financial educator, one book, or one calculator. We use publicly available material from multiple credible sources to identify overlapping principles, distinguish opinions from broadly supported financial mechanics, and turn the useful mechanics into measurable dashboards.

We do not reproduce copyrighted books or paid course material. We extract high-level principles from public sources and build original APEX implementations.

## Source families reviewed

### 1. Anthony O'Neal

Public materials currently expose a Money Plan Guide, Debt Calculator, Wealth Projection Calculator, Life Insurance Calculator, Wealth Builder Tool, retirement worksheet, savings tracker, debt-payoff material, and ongoing articles.

Recurring themes:
- Budget every dollar / give income a job.
- Build savings and emergency protection.
- Eliminate consumer debt.
- Track net worth and financial milestones.
- Increase income and build wealth.
- Use projections to make the future visible.

### 2. Consumer Financial Protection Bureau — Your Money, Your Goals

The CFPB provides a large free toolkit with 43 tools/handouts covering goals, saving, income, bills, cash-flow budgeting, debt, debt-to-income, credit, financial-product selection, and protecting money.

APEX extraction:
- Cash-flow timing matters, not just monthly totals.
- Bills should be prioritized when resources are constrained.
- Debt and credit should be tracked explicitly.
- Financial goals need action plans and revision loops.

### 3. FDIC — Money Smart

FDIC provides free financial education resources, including a 14-module adult curriculum and interactive tools. FDIC evaluation data reports associations between use of Money Smart and improved budgeting, regular saving, emergency savings, financial knowledge, and financial well-being.

APEX extraction:
- Financial education should be actionable.
- Behavioral reinforcement matters.
- Savings and emergency capacity deserve their own metrics.

### 4. Investor.gov / SEC

Investor.gov provides free compound-interest, savings-goal, retirement, investment-analysis, and other tools.

APEX extraction:
- Separate contributions from investment growth.
- Model return assumptions as assumptions, not promises.
- Show ranges/scenarios rather than a single deterministic outcome.
- Make fees and investment-risk considerations visible.

### 5. Money Guy — Financial Order of Operations

The current public FOO framework provides a nine-step sequence: deductibles, employer match, high-interest debt, emergency fund, Roth IRA/HSA, employer plans, hyperaccumulation, future expenses, and low-interest debt.

APEX extraction:
- The next dollar needs a priority order.
- Different financial stages require different actions.
- A financial plan is not necessarily linear; state can move backward or forward.

### 6. Ramit Sethi — Conscious Spending Plan

Public material organizes money into fixed costs, investments, savings, and guilt-free spending, emphasizing intentional allocation and automation rather than tracking every transaction as the primary behavioral mechanism.

APEX extraction:
- Intentional allocation can coexist with flexibility.
- Spending should be evaluated against values and priorities.
- Automation can reduce decision fatigue.

## Cross-source convergence

Across these sources, the strongest common architecture is:

```text
KNOW THE NUMBERS
      ↓
DEFINE THE GOAL
      ↓
CONTROL CASH FLOW
      ↓
PROTECT AGAINST SHOCKS
      ↓
ELIMINATE HIGH-COST DEBT / LEAKS
      ↓
ALLOCATE THE NEXT DOLLAR INTENTIONALLY
      ↓
INVEST CONSISTENTLY
      ↓
INCREASE INCOME / CAPACITY
      ↓
MEASURE NET WORTH + PROGRESS
      ↓
RECALCULATE
```

This is the seed. APEX grows it into an observable financial operating system.

## APEX Financial Freedom Dashboard

### Core state

- Verified cash
- Available cash
- Committed cash
- Monthly essential burn
- Monthly discretionary capacity
- Emergency reserve
- Reserve months of coverage
- Total debt
- High-interest debt
- Debt-to-income ratio
- Net worth
- Invested assets
- Monthly contributions
- Verified income
- Recurring income
- Variable income
- Taxes/obligations reserved

### Projection engine

Inputs:
- Current age
- Target financial-freedom age
- Current investments
- Monthly contribution
- Expected return assumption
- Inflation assumption
- Contribution growth assumption
- Optional income-growth assumption

Outputs:
- Conservative projection
- Base projection
- Optimistic projection
- Initial principal
- Total contributions
- Estimated growth
- Projected portfolio value
- Estimated financial-freedom date
- Required monthly contribution to hit target
- Gap to target

**No projection is presented as guaranteed.**

## Monitoring model

Financial state becomes an observable system rather than a static spreadsheet.

```text
SOURCE
  ↓
INGEST
  ↓
VERIFY
  ↓
NORMALIZE
  ↓
CALCULATE
  ↓
COMPARE AGAINST TARGETS
  ↓
GENERATE SIGNAL
  ↓
RECOMMEND NEXT ACTION
  ↓
HUMAN APPROVAL FOR MATERIAL ACTION
  ↓
EXECUTE
  ↓
READ BACK / VERIFY
```

### Signal examples

- `GREEN`: reserve target maintained and cash flow positive.
- `YELLOW`: reserve falling, recurring obligations rising, or debt payoff slowing.
- `RED`: negative cash flow, missed obligation, reserve breach, unauthorized transaction, or material financial anomaly.
- `OPPORTUNITY`: verified surplus available for the highest-value approved next upgrade.
- `PROJECTION_DRIFT`: actual contribution/growth trajectory materially diverges from target.

## Calculator registry

Each calculator is treated as a versioned APEX service, not a copied third-party page.

| Calculator | Inputs | Output | State |
|---|---|---|---|
| Net Worth | assets, liabilities | net worth | Planned |
| Cash Flow | income, bills, spending | monthly surplus/deficit | Planned |
| Debt Payoff | balance, APR, minimum, extra | payoff date/interest | Planned |
| Debt-to-Income | monthly debt, gross income | DTI | Planned |
| Emergency Reserve | essential burn, reserve | months covered | Planned |
| Compound Growth | principal, contribution, years, return | projection | Planned |
| Savings Goal | target, principal, years, return | required contribution | Planned |
| Financial Freedom | assets, income need, contributions, assumptions | FI gap/date | Planned |
| Next-Dollar Allocator | available surplus + priorities | recommended allocation | Planned |
| Upgrade ROI | cost + expected measurable benefit | payback/ROI | Planned |

## Governance rules

1. A projection is never treated as verified wealth.
2. External calculator results are references, not authoritative APEX state.
3. Financial data must carry source, timestamp, verification state, and confidence.
4. Material transfers/investments remain human-approved unless an explicit future policy authorizes automation.
5. A recommendation must expose the assumptions behind it.
6. A change in financial state should trigger recalculation.
7. No single educator's philosophy becomes an APEX financial law without cross-source review.
8. The system should prefer free, primary, government, regulatory, and transparent educational sources where possible.
9. Copyrighted material is not copied into APEX; principles and original implementations are used.
10. The dashboard is for planning/decision support and does not replace individualized legal, tax, or investment advice.

## Source links

- Anthony O'Neal: https://www.anthonyoneal.com/
- Anthony O'Neal Debt Calculator: https://www.anthonyoneal.com/debt-calculator
- Anthony O'Neal Wealth Builder: https://www.anthonyoneal.com/wealthbuilder
- CFPB Your Money, Your Goals: https://www.consumerfinance.gov/consumer-tools/educator-tools/your-money-your-goals/toolkit/
- FDIC Money Smart: https://www.fdic.gov/consumer-resource-center/learn-money-smart
- Investor.gov Financial Planning Tools: https://www.investor.gov/free-financial-planning-tools
- Money Guy Financial Order of Operations: https://moneyguy.com/guide/foo/
- Ramit Sethi Conscious Spending Basics: https://www.iwillteachyoutoberich.com/conscious-spending-basics/

## APEX principle

**Monitor what matters. Keep the numbers visible. Make the next dollar intentional. Verify before acting. Recalculate after acting.**
