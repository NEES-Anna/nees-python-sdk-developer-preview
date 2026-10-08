"""LEGACY ONLY: nees-core-sdk 0.1.x chat preview. NOT NEES Governance Platform V3.\n\nDo not use this script as a Core V3 integration or production example.\n"""\n\n"""Basic error handling with the NEES Python SDK."""

from nees import (
    NEESAPIError,
    NEESAuthenticationError,
    NEESClient,
    NEESRateLimitError,
    NEESTimeoutError,
)

client = NEESClient()

try:
    result = client.chat("Hello from NEES")
    print(result.reply)

except NEESAuthenticationError:
    print("Authentication failed. Check your NEES API key.")

except NEESRateLimitError:
    print("The current NEES request limit has been reached.")

except NEESTimeoutError:
    print("The NEES request timed out.")

except NEESAPIError as exc:
    print("NEES API request failed:", exc)
