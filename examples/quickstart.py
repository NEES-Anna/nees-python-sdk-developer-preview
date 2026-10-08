"""LEGACY ONLY: nees-core-sdk 0.1.x chat preview. NOT NEES Governance Platform V3.\n\nDo not use this script as a Core V3 integration or production example.\n"""\n\n"""Minimal NEES Python SDK example."""

from nees import NEESClient

client = NEESClient()

result = client.chat(
    "Reply with exactly: NEES SDK connected"
)

print(result.reply)
