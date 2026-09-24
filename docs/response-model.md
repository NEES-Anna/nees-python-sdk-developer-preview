# Public Response Model

The NEES Python SDK intentionally exposes a limited response model.

## `NEESChatResponse`

A successful chat call returns a response containing:

```text
reply
session_id
request_id
trace_id
governance
```

Example:

```python
result = client.chat("Hello")

print(result.reply)
print(result.session_id)
print(result.request_id)
print(result.trace_id)
```

`trace_id` is optional.

---

## `governance`

The governance property exposes selected public fields:

```text
decision
status
reason
```

Example:

```python
print(result.governance.decision)
print(result.governance.status)
print(result.governance.reason)
```

Each field may be absent depending on the supported response.

Applications should therefore avoid assuming that every governance field always contains a value.

---

## Deliberate response boundary

The SDK may receive service-side information that is not part of its public developer contract.

Undocumented fields should not be treated as supported SDK behavior.

This allows NEES services to evolve without requiring developers to depend on internal implementation details.
