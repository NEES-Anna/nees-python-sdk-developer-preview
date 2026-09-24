# NEES Python SDK — Developer Preview

A developer-facing guide for using the official NEES Python SDK.

NEES provides runtime governance services for AI applications. The Python SDK gives developers a simple client interface for connecting Python applications to supported NEES API capabilities.

> This repository contains documentation and safe usage examples only.
> It does not contain the NEES Core Engine source code or the proprietary SDK implementation.

---

## Current SDK

Current developer preview:

- Package: `nees-core-sdk`
- Python import: `nees`
- Python: 3.9+
- Current SDK version: `0.1.x`
- Current supported SDK capability: authenticated chat invocation

Install:

```bash
pip install nees-core-sdk
```

## Get API Access

The SDK requires a NEES API key.

Developer and evaluation access is currently provided by Nainacore Emotional Tech.

See [API_ACCESS.md](API_ACCESS.md) for access and credential setup.


Basic usage:

```python
from nees import NEESClient

client = NEESClient()

result = client.chat("Reply with exactly: NEES SDK connected")

print(result.reply)
```

The SDK reads `NEES_API_KEY` from the environment when an API key is not supplied directly.

---

## What NEES is for

NEES is designed for applications that need a governed runtime boundary around AI behavior and, as supported capabilities evolve, action-capable AI workflows.

The current Python SDK provides a deliberately small public interface.

Developers interact with documented public contracts without needing access to NEES Core internals.

---

## Public governance result

A chat response can expose selected public governance information:

```python
result.governance.decision
result.governance.status
result.governance.reason
```

These fields are intentionally limited public projections.

They should not be interpreted as exposing NEES internal policy evaluation, decision mechanics, or implementation details.

---

## Start here

- [Quickstart](QUICKSTART.md)
- [Installation](INSTALLATION.md)
- [Authentication](AUTHENTICATION.md)
- [SDK Usage](SDK_USAGE.md)
- [Error Handling](ERROR_HANDLING.md)
- [Security & Scope](SECURITY_AND_SCOPE.md)
- [Current Limitations](CURRENT_LIMITATIONS.md)

Examples are available in [`examples/`](examples/).

---

## Design principle

The developer interface is intentionally different from the implementation of NEES Core.

Applications should depend on stable public SDK contracts rather than internal governance implementation details.

---

## Current scope

The current SDK exposes authenticated chat invocation.

Additional NEES capabilities may become available through future documented SDK releases.

Do not assume that an API or capability exists unless it is explicitly documented in the current SDK.

---

## Links

Website:

https://nees.cloud

PyPI package:

`nees-core-sdk`

---

## Security

Never commit:

- NEES API keys
- access credentials
- `.env` files
- production secrets
- customer data

Use environment variables or your application's secret-management system.

See [SECURITY_AND_SCOPE.md](SECURITY_AND_SCOPE.md).

---

## Try NEES

Before integrating the Python SDK, developers can explore public NEES-powered experiences:

### Governance Lab

The Governance Lab provides a public demonstration of selected NEES governance behavior and normalized evidence.

Visit:

https://nees.cloud

### Naina Persona

Naina Persona is a public AI application that uses NEES as part of its runtime integration.

It is provided as an application-level example rather than as SDK documentation.

> These demonstrations expose selected public behavior only. They do not expose NEES Core implementation details or represent the complete NEES Core capability surface.

---
## About Nainacore

NEES is developed by **Nainacore Emotional Tech**.

© 2026 Nainacore Emotional Tech. All rights reserved.
