# NEES Governance Platform
### Give AI Agents Capabilities. Keep Their Actions Governed.

**Public Free Developer Preview · NEES Core V3 · Nainacore Emotional Tech**

**[Create free account](https://app.nees.cloud/login) · [Live Developer Guide](https://app.nees.cloud/developer-preview) · [Free Plan limits](docs/FREE-DEVELOPER-PREVIEW.md)**

AI agents can send emails, update databases, access files and call external APIs. But **just because an agent can perform an action, should it be allowed to?**

**NEES is an independent AI action governance platform.** It helps applications evaluate an agent's authority, policies, permitted scope and current governance state *before* consequential actions proceed.

NEES is **not** an LLM, chatbot or replacement for your agent framework. It is a governance boundary that helps make supported AI actions **controlled, traceable and accountable**.

## Why does AI governance matter?

Imagine an agent asked to send a confidential report. It knows how to send email—but:

- Is it authorized to send messages?
- Is that recipient within the permitted scope?
- Does policy require approval or block this operation?
- Can we inspect the decision and what actually happened?

NEES provides governance checks and evidence. **An ALLOW decision is not proof of execution**: the owning application must still validate its actual target, perform the effect safely and report the real outcome.

## How NEES works

```text
User / Application -> AI Agent -> Proposed Action
                                  |
                                  v
                          NEES Governance
                     Authority · Policy · Scope
                     Tool permissions · State
                                  |
                         Governance result
                          /             \
                   Not authorized     Authorized
                        |                  |
                   Do not execute     App rechecks context
                                           |
                                    Executes & verifies
                                           |
                                     Reports outcome
                                           |
                                    Evidence & receipt
```

**NEES governs supported operations; your application owns execution and verification.**

## Public Free Developer Preview — live now

New developers can sign up, confirm email, sign in and create a **Free Developer** organization without a payment method. Signup, verified sign-in and Free organization provisioning have been tested on the hosted service.

| Free allowance | Limit |
| --- | --- |
| New governance operation submissions | **1,000 per UTC calendar month** |
| Free organizations | 1 per verified account |
| Projects | 1 |
| Runtimes | 1 |
| Environments | 1, **development only** |
| Active runtime API credentials | 2 |
| Authenticated runtime requests | 30/minute per organization |

Monthly credits renew on the UTC calendar boundary without rollover. Inspection and reporting of existing operations do not consume new-submission credits, but rate limits still apply. Staging/production environments, checkout and self-service paid upgrades are unavailable on Free.

**Hosted proof status:** Public signup, email confirmation, sign-in, Free organization creation and allowance display are verified; a complete new-Free-account execution and every quota boundary have not yet been individually production-verified. This is a **Developer Preview**, not production GA.

Read the [Free Developer Preview guide](docs/FREE-DEVELOPER-PREVIEW.md) for supported screens, integration boundaries and exact restrictions.

## Choose your integration

| Method | Typical use |
| --- | --- |
| **Python SDK** | Python agents and backends |
| **REST API** | Applications in any supported language |
| **Gateway / Proxy** | Mediated HTTP service and tool calls |
| **MCP Adapter** | Supported MCP-based agent/tool integrations |
| **Framework Adapters** | Supported agent framework hooks |

Availability and configuration depend on the specific connector and deployment.

## Get started in the Governance Platform

1. **Create a free account** at [app.nees.cloud](https://app.nees.cloud/login), confirm your email, sign in and create your Free organization.
2. **Open Developer Onboarding**. Provision a project, runtime, development environment and one-time runtime credential; store the key **server-side**.
3. **Run a governance proof** in the Dashboard and inspect the decision, evidence and (where applicable) receipt. This bounded proof is **not** external-provider execution.
4. **For your real application**, register the actual action with its resource, operation, capability and side-effect metadata. Publish appropriate governance through an authorized workflow.
5. Open **Infrastructure → Assessment configuration manager**. Select **Registered action → Published scope → Integration method** and click **Resolve existing assessment** for version-bound commitments.
6. **Integrate and test** through the compatible SDK/REST/connector: submit → qualify → start → execute safely → report the actual outcome → inspect evidence/receipt.

The Dashboard exports the exact **version-bound** assessment commitments for the selected existing governance baseline. It does **not** export your API key or grant permission by itself.

**Important:** *Publish baseline & resolve* changes governance records and may overwrite custom policy commitments. Use *Resolve existing assessment* for read-only configuration lookup.

## Developer docs

| Guide | What you'll find |
| --- | --- |
| [Quickstart](QUICKSTART.md) | First integration walkthrough |
| [Free Developer Preview](docs/FREE-DEVELOPER-PREVIEW.md) | Plan limits, onboarding and restrictions |
| [Hosted Developer Guide](https://app.nees.cloud/developer-preview) | Current getting-started page |
| [Dashboard assessment configuration](docs/DASHBOARD-ASSESSMENT-CONFIGURATION.md) | Actions, published scopes, exports and safety |
| [Complete integration guide](docs/NEES-INTEGRATION-GUIDE.md) | Supported lifecycle and boundaries |
| [Integration patterns](docs/integration-patterns.md) | SDK, REST, Gateway, MCP and adapters |
| [Python SDK usage](SDK_USAGE.md) | V3 Python client and CLI |
| [Access](API_ACCESS.md) | Account and credential guidance |
| [Troubleshooting](docs/TROUBLESHOOTING.md) | Common errors and recovery |
| [Production checklist](docs/PRODUCTION-CHECKLIST.md) | Production acceptance gates |
| [Security and scope](SECURITY_AND_SCOPE.md) | Secrets, limits and responsibilities |
| [Case studies](docs/CASE-STUDIES.md) | Governance Lab and NainaSOS learnings |

**Python SDK note:** Current V3 governance SDK uses the `nees-sdk` 3.x release-candidate family. The older `nees-core-sdk` 0.1.x chat interface is **not** a compatible V3 governance client. See [SDK usage](SDK_USAGE.md).

## Try the Developer Preview

We welcome **AI agent developers, backend engineers, researchers and testers** to explore governance for their supported actions, test allow/deny paths, inspect evidence and share integration feedback.

- **[Open Governance Dashboard](https://app.nees.cloud)**
- **[Product website](https://nees.cloud)**
- **[Report feedback or issues](https://github.com/NEES-Anna/nees-python-sdk-developer-preview/issues)**

> **Preview scope:** Public signup and Free organization enrollment are live and verified. The complete governance execution path for a new Free account, all quota boundaries and production readiness have not been verified end to end. Never publish keys, sensitive governance traces or customer data.

### Build AI That Can Act — With Governance You Can Verify.

© 2026 Nainacore Emotional Tech.
