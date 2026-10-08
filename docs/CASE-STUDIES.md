# Integration Case Studies — Public, Sanitized

These case studies are **patterns**, not copies of private source/configuration, confidential policies or production evidence.

## NainaSOS desktop agent

**Goal:** Govern an external desktop semantic-typing action through the hosted NEES Runtime.

**Pattern:** The Windows agent owns tool execution and observation. A Python SDK/transport boundary communicates with Runtime. Governed operation phases and evidence are tracked separately from actual typing.

**Issue 1 — Incomplete assessment:** Required commitments (authority, policy, relationship, tool policy and decision state) were not fully bound. **Correction:** Match the hosted assessment contract and currently published governance versions. Never place real binding digests, private state or credentials in public examples.

**Issue 2 — Transport availability:** A narrow `curl.exe` fallback was added in the *application adapter*, only for a transport-unavailable class without an HTTP status; it was not a policy bypass.

**Issue 3 — Local execution correctness:** Hosted decision ALLOW did not mean desktop typing happened. Notepad was the target but a different editor was foreground. The agent rejected the unsafe effect with `foreground_app_mismatch`, re-observed/replanned, and reported execution truthfully.

**Reusable lesson:** Governance controls authorization; application verification must independently control and report real side effects.

## Governance Lab web application

**Goal:** Let a visitor explore policy decisions for custom scenarios while routing governance through the hosted NEES boundary.

**Pattern:** Browser supplies a scenario; trusted backend normalizes facts conservatively and submits against a registered **synthetic** governed action. The UI exposes safe decision/evidence projections, not secret assessment state.

**Issue — Natural-language over-inference:** A permissive normalizer risked filling facts that were never provided. **Correction:** Make normalization strict and avoid manufacturing actor authority, consent or previous approval.

**Reusable lesson:** An interpreter is an input tool, not the policy decision-maker. Synthetic evaluation must be labeled as simulation and cannot claim actual external execution.

## What is intentionally excluded

Real organization/project/runtime identifiers, API tokens, assessment binding JSON, sensitive trace payloads, privileged policy contents and private implementation details.
