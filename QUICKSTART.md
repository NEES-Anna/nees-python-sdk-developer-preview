# NEES Python SDK Quickstart

This guide shows the smallest supported integration with the NEES Python SDK.

## 1. Install

```bash
pip install nees-core-sdk
```

Python 3.9 or newer is required.

---

## 2. Configure your API key

### Windows PowerShell

```powershell
$env:NEES_API_KEY="your-api-key"
```

### Linux / macOS

```bash
export NEES_API_KEY="your-api-key"
```

Do not place real API keys directly in source files that will be committed.

---

## 3. Create a client

```python
from nees import NEESClient

client = NEESClient()
```

When no API key is passed directly, the SDK reads `NEES_API_KEY` from the environment.

---

## 4. Send a chat request

```python
result = client.chat("Reply with exactly: NEES SDK connected")

print(result.reply)
```

A minimal complete example:

```python
from nees import NEESClient

client = NEESClient()

result = client.chat(
    "Reply with exactly: NEES SDK connected"
)

print(result.reply)
```

---

## 5. Inspect public governance information

```python
print(result.governance.decision)
print(result.governance.status)
print(result.governance.reason)
```

These values are public SDK fields.

They are intentionally limited and do not expose NEES Core internal governance mechanics.

---

## Next

Read:

- [SDK Usage](SDK_USAGE.md)
- [Response Model](docs/response-model.md)
- [Error Handling](ERROR_HANDLING.md)
- [Security & Scope](SECURITY_AND_SCOPE.md)
