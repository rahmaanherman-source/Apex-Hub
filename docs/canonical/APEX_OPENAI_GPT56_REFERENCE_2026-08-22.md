# APEX — OpenAI GPT-5.6 Reference

**Status:** Canonical staging / source-ingested
**Source:** User-supplied GPT-5.6 documentation
**Verification:** Current official-source verification required before promotion to independently verified platform truth

## Model family

The supplied source describes this naming scheme:

- `gpt-5.6` → alias routing to `gpt-5.6-sol`
- `gpt-5.6-sol` → flagship capability
- `gpt-5.6-terra` → strong performance at lower price
- `gpt-5.6-luna` → efficient, high-volume workloads

## New capabilities recorded

- Programmatic Tool Calling (PTC)
- Multi-agent beta in the Responses API
- Explicit prompt caching
- Persisted reasoning through `reasoning.context`
- `max` reasoning effort
- Pro mode through `reasoning.mode: "pro"`
- Improved token efficiency
- Improved frontend design judgment
- Improved intent understanding
- Preservation of original image dimensions for `original`/`auto` image detail

## Responses API routing

The supplied source directs reasoning, tool-calling, and multi-turn workflows toward the Responses API.

APEX should treat this as a documented routing candidate, not as proof that a specific APEX deployment is already configured for GPT-5.6.

## Reasoning controls

The supplied source lists:

`none`, `low`, `medium`, `high`, `xhigh`, `max`

It recommends starting from the existing GPT-5.5/GPT-5.4 reasoning setting during migration and comparing the same setting with one level lower on representative tasks.

`max` is described as a quality-first option for the hardest tasks.

## Pro mode

Pro mode is described as a Responses API execution mode using the selected GPT-5.6 model with:

`reasoning.mode: "pro"`

Reasoning mode and reasoning effort are independent. The source recommends measuring quality, completeness, tokens, latency, and cost before broad adoption.

## Persisted reasoning

The supplied source describes `reasoning.context` and states that GPT-5.6 defaults to `all_turns` when omitted or set to `auto`.

For stable multi-turn goals, `all_turns` can be used with `previous_response_id`. When earlier reasoning is no longer relevant, `current_turn` is appropriate.

APEX must preserve the distinction between model-documented behavior and APEX memory architecture. Persisted model reasoning is not automatically canonical APEX memory.

## Programmatic Tool Calling

PTC is described as appropriate for bounded, predictable processing such as:

- filtering;
- joining;
- ranking;
- deduplication;
- aggregation;
- validation;
- other deterministic processing of intermediate tool results.

The supplied source cautions against using PTC merely because calls are parallel or dependent. Direct calls remain preferable when one call is sufficient, outputs are small, each result may change the next model decision, approval is required, or native citations/artifacts must be preserved.

APEX routing rule:

```text
Semantic judgment / approval / final validation → direct model/tool path
Bounded deterministic processing → consider PTC
```

PTC adoption must be benchmarked against direct calling using task success, final completeness, evidence requirements, tokens, latency, cost, calls, turns, and retries.

## Multi-agent beta

The supplied source describes Multi-agent as a beta Responses API feature allowing a GPT-5.6 instance to coordinate multiple subagents in parallel and synthesize results.

APEX should treat this as a candidate orchestration capability for independently divisible workstreams. Beta status means it requires explicit verification before production-critical dependence.

## Prompt caching

The supplied source describes explicit prompt caching and notes:

- cache writes billed at 1.25× the uncached input rate;
- cache reads remain discounted;
- implicit automatic caching remains available;
- `prompt_cache_options.mode: "explicit"` can define explicit breakpoints;
- `prompt_cache_retention` should be replaced with `prompt_cache_options.ttl`.

APEX should track `cached_tokens` and `cache_write_tokens` when evaluating cost impact.

## Prompting / autonomy policy

The supplied source recommends defining autonomy and approval boundaries explicitly. Its example separates:

- answer/explain/review/diagnose/plan → inspect and report, no implementation unless requested;
- change/build/fix → make requested in-scope local changes and run non-destructive validation;
- external writes, destructive actions, purchases, or material scope expansion → require confirmation.

This aligns with APEX's no-fake-green and approval-boundary architecture and should be treated as source-derived guidance pending current official verification.

## Prompt efficiency

The source recommends leaner prompts:

- state each instruction once;
- remove redundant examples/instructions incrementally;
- expose only relevant tools;
- keep descriptions concise and precise;
- retain examples that encode real product requirements;
- measure context growth over long sessions.

Reported internal evaluation ranges in the supplied source are directional only and must not be treated as guaranteed APEX performance gains.

## Output verbosity

The source describes `text.verbosity` with `low`, `medium`, and `high` defaults. Task-specific prompts should state required content, structure, and length where necessary.

## Safety / identifiers

The supplied source describes real-time cyber and biology misuse classifiers and recommends a stable, privacy-preserving `safety_identifier` for individual end users.

APEX should not store or expose safety identifiers unnecessarily. Any implementation must be verified against current official safety documentation and applicable privacy requirements.

## Migration rule

For an APEX workload migrating from GPT-5.5 or GPT-5.4:

```text
CURRENT MODEL + CURRENT REASONING SETTING
        ↓
GPT-5.6 SAME SETTING
        ↓
GPT-5.6 ONE LEVEL LOWER
        ↓
REPRESENTATIVE EVALS
        ↓
SUCCESS / COMPLETENESS / EVIDENCE
        ↓
TOKENS / LATENCY / COST
        ↓
PROMOTE ONLY WITH EVIDENCE
```

## Capability Registry candidate

```yaml
provider: OpenAI
capability_family: reasoning_model
model_family: GPT-5.6
aliases:
  - gpt-5.6
models:
  - gpt-5.6-sol
  - gpt-5.6-terra
  - gpt-5.6-luna
api_preference: Responses API
capabilities:
  - programmatic_tool_calling
  - multi_agent_beta
  - explicit_prompt_caching
  - persisted_reasoning
  - max_reasoning_effort
  - pro_mode
  - text_verbosity
status: source_ingested
confidence: user_supplied_docs
verificationRequired: true
```

## No-Fake-Green gate

Documentation alone does not establish that any GPT-5.6 model is available to an APEX account, configured in a repository, connected through the intended SDK/API path, or performing successfully in production.

Promotion remains:

`DOCUMENTED → CONFIGURED → CONNECTED → EXECUTED → TESTED → VERIFIED`

Do not mark GPT-5.6 production-ready without runtime evidence and representative evaluation results.
