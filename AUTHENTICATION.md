# Authentication

The NEES Python SDK uses an API key to authenticate supported remote requests.

## Recommended configuration

Store the API key in an environment variable.

### Windows PowerShell

```powershell
$env:NEES_API_KEY="your-api-key"
```

### Linux / macOS

```bash
export NEES_API_KEY="your-api-key"
```

Then initialize the SDK normally:

```python
from nees import NEESClient

client = NEESClient()
```

---

## Explicit API key

For controlled development environments, an API key can also be supplied when creating the client:

```python
from nees import NEESClient

client = NEESClient(
    api_key="your-api-key"
)
```

Avoid hard-coding production credentials in application source code.

---

## API key safety

Never publish or commit:

```text
NEES_API_KEY
```

Never include a real key in:

- GitHub repositories
- screenshots
- issue reports
- example code
- frontend JavaScript
- public logs
- documentation

API keys should be treated as secrets.

---

## Server-side use

NEES API credentials should normally remain in trusted backend environments.

Example:

```text
Browser / User
      |
      v
Your Backend
      |
      v
NEES Python SDK
      |
      v
NEES API
```

Avoid exposing NEES credentials directly to untrusted clients.

---

## Revoked or invalid credentials

Authentication failures should be handled using the SDK's documented error classes.

See [ERROR_HANDLING.md](ERROR_HANDLING.md).
