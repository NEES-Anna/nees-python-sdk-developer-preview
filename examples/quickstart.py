"""Minimal NEES Python SDK example."""

from nees import NEESClient

client = NEESClient()

result = client.chat(
    "Reply with exactly: NEES SDK connected"
)

print(result.reply)
