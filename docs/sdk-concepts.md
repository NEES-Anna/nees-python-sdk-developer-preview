# Core Concepts for SDK Users

This document explains only the concepts required to use the public NEES Python SDK.

It is not an architecture specification for NEES Core.

## Client

`NEESClient` is the primary Python interface exposed by the SDK.

```python
from nees import NEESClient

client = NEESClient()
```

---

## Request

The current SDK allows a Python application to submit a supported chat request to NEES.

```python
result = client.chat("Your message")
```

---

## Response

The SDK converts the supported service response into a small public Python model.

The primary application-facing value is:

```python
result.reply
```

---

## Governance result

A response can contain selected governance information:

```python
result.governance.decision
result.governance.status
result.governance.reason
```

These are consumer-facing results.

They do not expose the internal governance process that produced them.

---

## Request identity

Responses expose public identifiers that applications can use for correlation:

```python
result.session_id
result.request_id
result.trace_id
```

`trace_id` may be absent and should be treated as optional.

---

## Public contract

A useful rule for integrations is:

> Build against what the SDK documents, not against assumptions about the NEES service behind it.

This keeps applications isolated from internal implementation changes.
