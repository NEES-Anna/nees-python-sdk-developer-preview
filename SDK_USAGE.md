# SDK Usage

## Import

```python
from nees import NEESClient
```

---

## Default client

```python
client = NEESClient()
```

The client can use the `NEES_API_KEY` environment variable.

---

## Custom configuration

```python
from nees import NEESClient

client = NEESClient(
    api_key="your-api-key",
    base_url="https://api.nees.cloud",
    timeout=30,
)
```

For production deployments, prefer secret-management or environment-based credential injection rather than hard-coded API keys.

---

## Chat

Current SDK v0.1 exposes authenticated chat invocation.

```python
result = client.chat(
    "Explain runtime governance in simple terms."
)
```

Read the generated reply:

```python
print(result.reply)
```

---

## Response identifiers

The public response model includes identifiers that can help applications correlate requests.

```python
print(result.session_id)
print(result.request_id)
print(result.trace_id)
```

A trace identifier may not always be present.

Applications should therefore handle it as optional.

---

## Governance result

Selected governance information is exposed through:

```python
result.governance
```

Available public fields:

```python
result.governance.decision
result.governance.status
result.governance.reason
```

Example:

```python
result = client.chat("Explain this request.")

governance = result.governance

print("Decision:", governance.decision)
print("Status:", governance.status)
print("Reason:", governance.reason)
```

These fields represent the supported public SDK contract.

They do not expose the internal governance implementation.

---

## Current capability boundary

Current SDK v0.1 supports:

```text
chat:invoke
```

Do not assume that other NEES API capabilities are available through the Python SDK unless they appear in current official SDK documentation.

Future versions may expand this interface.
