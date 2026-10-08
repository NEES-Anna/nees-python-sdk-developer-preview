# NEES Governance Platform — Developer Preview & Integration Guide

Official public-facing integration documentation from **Nainacore Emotional Tech**.

NEES provides an independent governance boundary for supported AI agents, automation systems and application actions. Your application owns the action and verifies the outcome; NEES governs the supported operation through its published contracts.

> **Public documentation only.** This repository contains no NEES Core source, private governance policies, private SDK implementation, credentials, customer data or production assessment bindings.

## Start here

1. [Access and onboarding](API_ACCESS.md)
2. [Governance Platform quickstart](QUICKSTART.md)
3. [Complete integration guide](docs/NEES-INTEGRATION-GUIDE.md)
4. [Integration patterns](docs/integration-patterns.md)
5. [Python SDK usage and migration](SDK_USAGE.md)
6. [Production readiness](docs/PRODUCTION-CHECKLIST.md)
7. [Troubleshooting](docs/TROUBLESHOOTING.md)
8. [Security and scope](SECURITY_AND_SCOPE.md)

## Current platform

| Surface | Public URL | Role |
| --- | --- | --- |
| Website | https://nees.cloud | Product overview |
| Dashboard | https://app.nees.cloud | Organization, project, runtime and credential onboarding |
| Runtime | https://api.nees.cloud | Hosted governed-operation lifecycle |
| Control Plane | https://control-api.nees.cloud | Management API; authenticated/authorized |
| Gateway | https://nees-gateway.onrender.com | HTTP governance boundary |

These are public *service addresses*, not authorization to access another organization's resources.

## SDK generations — read before installing

**Governance Platform / Core V3:** The Python distribution is `nees-sdk` (3.0.0 release-candidate series); the CLI is `nees`. See [SDK_USAGE.md](SDK_USAGE.md). Check the latest published PyPI release before pinning.

**Historical chat-only developer preview:** The older `nees-core-sdk` (0.1.x) with `from nees import NEESClient` and `client.chat(...)` is a *different, legacy interface*. It is not the documented V3 governance-operation client. The former examples in `examples/` remain as **legacy reference only**, not recommended Governance Platform examples. Do not mix the packages or assume API compatibility.

## Execution boundary

```text
Application / Agent (owns intent, observations and effects)
    -> supported SDK / REST connector / Gateway / MCP adapter
    -> NEES hosted Runtime (qualify / govern)
    -> application enforces authorized result, executes and verifies
    -> report actual outcome; inspect operation / evidence / receipt
```

Authorization is not proof that an external action occurred. A transport error is not permission to bypass governance.

## Examples and case studies

- [NainaSOS desktop agent](docs/CASE-STUDIES.md#nainasos-desktop-agent): authorization, foreground-target verification, outcome reporting.
- [Governance Lab](docs/CASE-STUDIES.md#governance-lab-web-application): strict scenario normalization, synthetic actions, evidence.
- [Legacy chat examples](examples/): archival v0.1 chat interface only; **not** V3 governance examples.

## Publication and security

All example values are intentionally placeholders. Do not add real keys, organization IDs, production assessment JSON, tokens, internal policy documents, customer traces, or copied private repository source. See [SECURITY_AND_SCOPE.md](SECURITY_AND_SCOPE.md).

Documentation edition: **Governance Platform integration v1 draft (2026-10-08)**. Actual request/response shapes must be validated against the version of the live API/SDK being used. No capability is guaranteed just by appearing in this overview.

© 2026 Nainacore Emotional Tech. Nainacore™.
