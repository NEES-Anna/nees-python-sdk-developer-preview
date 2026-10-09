# NEES Governance Platform
### Give AI Agents Capabilities. Keep Their Actions Governed.

**Developer Preview · NEES Core V3 · Nainacore Emotional Tech**

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

1. **Sign in** at [app.nees.cloud](https://app.nees.cloud) and select/create an organization.
2. **Set up your application:** Project → Runtime → Environment. Issue a runtime credential and keep it **server-side**.
3. **Register your real action** with its resource, operation, capability and side-effect metadata.
4. **Publish governance** for that action through an authorized workflow.
5. Open **Infrastructure → Assessment configuration manager**. Select **Registered action → Published scope → Integration method** and click **Resolve existing assessment**.
6. **Integrate and test:** submit → qualify → start → report the actual outcome; inspect operation, evidence and receipt.

The Dashboard exports the exact **version-bound** assessment commitments for the selected existing governance baseline. It does **not** export your API key or grant permission by itself.

**Important:** *Publish baseline & resolve* changes governance records and may overwrite custom policy commitments. Use *Resolve existing assessment* for read-only configuration lookup.

## Developer docs

| Guide | What you'll find |
| --- | --- |
| [Quickstart](QUICKSTART.md) | First integration walkthrough |
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

> **Preview scope:** Evaluation and integration testing. Independent developer onboarding and deployment-specific production readiness still require validation. Never publish real API keys, organization credentials, customer data or sensitive governance traces.

### Build AI That Can Act — With Governance You Can Verify.

© 2026 Nainacore Emotional Tech.
