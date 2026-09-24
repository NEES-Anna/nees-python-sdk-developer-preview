# Current Limitations

This document describes the public developer-preview boundary of the NEES Python SDK.

## SDK v0.1

The current Python SDK exposes authenticated chat invocation.

Current supported SDK capability:

```text
chat:invoke
```

The SDK should not currently be described as exposing the full NEES Core governance surface.

---

## Public response

The SDK returns a deliberately limited response model.

Public applications may receive:

- reply
- session identifier
- request identifier
- optional trace identifier
- selected governance decision
- selected governance status
- selected governance reason

Additional internal service information is not part of the public SDK contract.

---

## Action execution

Do not assume that consequential-action submission, approval workflows, external execution, evidence APIs, administrative operations, or other Core capabilities are available through the current Python SDK unless explicitly documented in a later SDK release.

---

## Framework integrations

The current package is a general Python client.

Framework-specific integrations should be built using the documented public SDK interface rather than depending on internal NEES service behavior.

---

## Version expectations

The SDK is still in an early developer-preview stage.

Public interfaces may expand in later releases.

Applications should pin versions where predictable dependency behavior is important.
