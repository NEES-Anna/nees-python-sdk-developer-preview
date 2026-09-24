# Error Handling

The NEES Python SDK exposes structured exception classes for common API and configuration failures.

## General error handling

Use `NEESAPIError` when you want to catch API-related failures broadly.

```python
from nees import NEESClient, NEESAPIError

client = NEESClient()

try:
    result = client.chat("Hello")
    print(result.reply)

except NEESAPIError as exc:
    print("NEES API error:", exc)
```

---

## Available public exceptions

The SDK currently exports:

```python
NEESAPIError
NEESAuthenticationError
NEESAuthorizationError
NEESBadRequestError
NEESConfigurationError
NEESConflictError
NEESConnectionError
NEESNotFoundError
NEESRateLimitError
NEESServerError
NEESTimeoutError
NEESValidationError
```

---

## Example

```python
from nees import (
    NEESClient,
    NEESAuthenticationError,
    NEESRateLimitError,
    NEESTimeoutError,
    NEESAPIError,
)

client = NEESClient()

try:
    result = client.chat("Hello from my application")
    print(result.reply)

except NEESAuthenticationError:
    print("Check the configured NEES API key.")

except NEESRateLimitError:
    print("The current request limit has been reached.")

except NEESTimeoutError:
    print("The NEES request timed out.")

except NEESAPIError as exc:
    print("NEES request failed:", exc)
```

---

## Do not expose sensitive error context

Production applications should avoid returning raw backend exceptions, credentials, headers, or internal configuration information directly to end users.

Log only the information your operational environment requires.
