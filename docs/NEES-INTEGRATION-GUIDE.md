# NEES Core V3 — Developer & Client Integration Guide

**Status:** Public, security-reviewed-by-design documentation draft. **Scope:** Hosted Governance Platform; not NEES Core internal implementation.

## 1. Integration contract

NEES supplies a governance boundary for supported actions. Your application retains responsibility for intent capture, tool execution, local observation, verification and accurate outcome reporting. Authorization, execution and proof are **distinct**.

```text
Trusted application / agent
   -> validate intent and current target context
   -> connector boundary (Python SDK / REST / Gateway / MCP / adapter)
   -> hosted NEES Runtime qualification and decision
   -> enforce result locally
   -> execute external effect only when authorized and still safe
   -> report actual outcome
   -> inspect operation, evidence chain and receipt
```

## 2. Prerequisites and onboarding

1. Sign in to https://app.nees.cloud.
2. Select/create an organization and a project.
3. Create/select runtime and development/staging/production environment as appropriate.
4. Issue least-privilege credentials for that runtime; never expose keys to a browser.
5. Register the **actual** governed action reference and its resource, operation, capability and side-effect metadata.
6. Publish the required authority, policy and relationship/tool governance state using supported Control Plane workflows.
7. Use **Infrastructure → Assessment configuration manager** to select registered action and published scope, then export current assessment bindings for your method. Never guess refs, versions or digests. [Dashboard workflow](DASHBOARD-ASSESSMENT-CONFIGURATION.md).
8. Check Runtime health/readiness and credential access.
9. Complete allow, deny and failure-path tests before enabling consequential production effects.

## 3. Integration choices

| Method | Typical owner | Key responsibility |
| --- | --- | --- |
| Python SDK (`nees-sdk` 3.x RC) | Python backend / agent | Align package and hosted contracts |
| REST connector | Non-Python backend | Authenticate, validate schemas, handle lifecycle and retries |
| Gateway / proxy | Backend routed tool calls | Ensure each governed path is actually mediated |
| MCP connector | MCP host/agent | Enforce governance at supported tool boundary |
| Framework adapter | Supported agent framework | Preserve authority and evidence across framework hooks |

Connector availability/configuration must be checked for the target deployment. Do not treat the existence of an adapter as a blanket guarantee that every external action is covered.

## 4. Operation lifecycle

**Submit:** Send a correctly structured operation for a registered action in the correct scope.

**Qualify:** Obtain governance qualification using published policies, authority and required assessment bindings. Incomplete or stale commitments are not permission.

**Start:** Proceed only when the hosted governance state and your local target/context allow the operation. Keep the target/capability bound to the registered action; do not silently substitute a different target.

**Execute:** Perform the actual side effect in the owning application. Re-check volatile conditions (such as the active foreground app) immediately before execution. Do not turn a failed check into a successful report.

**Report:** Send actual execution outcome through the supported runtime contract; preserve request/operation correlation IDs and avoid logging secrets.

**Inspect:** Query operation, evidence and receipt to reconcile authorization, recorded execution and verification. These may be different statuses.

The public REST base is `https://api.nees.cloud`. A previously exercised operation submission route is `POST /v1/operations`; **the full schema, headers and subsequent routes are version-bound and intentionally not fabricated here**. Use the matching published API specification/SDK version for concrete HTTP payloads.

## 5. Correctness and security invariants

- **Fail closed:** missing/negative governance, unavailable service, invalid scope or stale authority must not trigger a side effect.
- **No bypass:** do not use transport fallbacks to turn a rejection into an ALLOW.
- **No invented facts:** a natural-language normalizer may structure input, but must not invent identity, authority, resources, prior approvals or execution outcomes.
- **No uncontrolled retries:** retrying an action with side effects may duplicate execution; use version-supported idempotency/reconciliation.
- **No credential leakage:** keep runtime keys and provider keys server-side, out of commits, screenshots and traces.
- **No internal dependency:** integrate with published contracts, not Core Engine implementation or private database schemas.

## 6. Real integration learnings

**NainaSOS:** Required assessment commitments were initially incomplete. Aligning bindings resolved qualification issues. A narrow Windows `curl.exe` fallback addressed SDK transport unavailability without bypassing governance errors. Later, a governance-allowed Notepad action correctly **did not execute** when VS Code was foreground: the agent observed `foreground_app_mismatch` and requested re-observation/replanning.

**Governance Lab:** The web app uses server-side credentials and a registered synthetic action to assess user-provided scenarios. Strict normalization prevents plausible-sounding but unsupported assumptions. A simulated scenario result is not evidence of a real-world external side effect.

See [Case Studies](CASE-STUDIES.md), [Troubleshooting](TROUBLESHOOTING.md), [Production Checklist](PRODUCTION-CHECKLIST.md).

## 7. Client acceptance gate

Before go-live, record: connector/SDK version, published action configuration, environment, credential rotation procedure, ALLOW/DENY tests, target-mismatch test, stale-assessment test, network failure behavior, duplicate/retry behavior, truthful report behavior, and evidence/receipt reconciliation. Do not publish raw real-world acceptance traces without sanitization.
