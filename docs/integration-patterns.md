# Integration Patterns

The NEES Python SDK is designed to be used from trusted Python application environments.

## Backend application

Typical pattern:

```text
User Interface
      |
      v
Application Backend
      |
      v
NEES Python SDK
      |
      v
NEES API
```

The application backend retains the NEES API credential.

---

## Existing AI application

The SDK can be added to an existing Python service without requiring the application's user interface to communicate directly with NEES.

```text
Application
    |
    +---- existing application logic
    |
    +---- NEES Python SDK
```

Keep NEES credentials in the trusted application environment.

---

## Web API backend

A Python web application may use `NEESClient` inside its backend service.

Conceptually:

```python
from nees import NEESClient

nees = NEESClient()

def handle_request(message: str):
    result = nees.chat(message)
    return result.reply
```

Production applications should add their normal authentication, validation, logging, timeout, and error-handling requirements around this integration.

---

## Framework independence

The SDK is a Python client rather than an agent framework.

Applications remain free to choose their own:

- web framework
- AI framework
- model provider
- application architecture
- user interface

Do not couple an integration to undocumented NEES internals.

---

## Future capabilities

As additional capabilities become part of the supported Python SDK, new integration patterns can be documented here.

A capability should not be considered supported until it appears in current official SDK documentation.
