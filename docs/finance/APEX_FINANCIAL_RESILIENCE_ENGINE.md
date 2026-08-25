# APEX Financial Resilience Engine

**Status:** INTERNAL R&D SPECIFICATION — NOT A FINANCIAL ADVICE PRODUCT

## Principle

A household financial problem is not solved by omitting variables. APEX therefore models income, essential obligations, debt, resources, location-specific opportunities, reserves, risk, and future known obligations together.

## Core variables

### Income
- all income sources
- gross/net income
- pay frequency
- income volatility
- taxes/withholding
- benefits and employer resources

### Essential spending
- housing
- utilities
- food
- transportation
- insurance
- healthcare
- childcare
- education
- required services
- known periodic expenses

### Debt
- balance
- APR
- minimum payment
- due date
- fees
- promotional expiration
- secured/unsecured status
- utilization
- interest cost

### Assets/reserves
- cash
- emergency reserve
- retirement
- investments
- other verified assets

### Resource opportunity layer

APEX may identify potentially relevant federal, state, county, city, employer, utility, nonprofit, education, workforce, tax, and other programs. Location and eligibility are variables.

A potential resource is never treated as received money until verified.

## Core equations

```text
Financial Position
= Income
+ Verified Benefits
+ Verified Other Resources
- Essential Expenses
- Debt Obligations
- Taxes
- Known Future Obligations
```

```text
Deployable Capital
= Financial Position - Required Safety Reserve
```

The system must not recommend deploying money that is required for essential obligations or the defined reserve floor.

## Debt strategy

APEX can compare multiple payoff strategies instead of blindly selecting one:

- highest-interest-first (avalanche)
- smallest-balance-first (snowball)
- cash-flow relief strategy
- hybrid strategy
- refinance/consolidation scenario where appropriate

Each strategy must show total interest, payoff time, required monthly cash, and sensitivity to income/expense changes.

## Scenario engine

Scenarios may include:

- income increase/decrease
- expense increase/decrease
- rate changes
- unexpected expense
- benefit approval/denial
- debt refinance
- accelerated payoff
- reserve target changes

Scenarios are explicitly labeled as scenarios, not predictions.

## Monitoring

```text
BASELINE -> INTERVENTION -> OBSERVE -> VERIFY -> COMPARE -> LEARN
```

Record:

- expected outcome
- actual outcome
- variance
- reason for variance
- source evidence
- date checked

```text
Model Error = Actual Outcome - Expected Outcome
```

APEX learns from measured error instead of silently changing historical results.

## Research policy

The research program may study established personal-finance, economics, behavioral-finance, health, wealth, and resilience frameworks. Sources are treated as research inputs, not truth. Claims must be attributed, checked against primary/credible sources where possible, and separated into:

- source claim
- APEX interpretation
- APEX calculation
- observed result

The eventual APEX book is built from documented evidence and original synthesis, not copied text or unsupported promises.
