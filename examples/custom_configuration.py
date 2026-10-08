"""LEGACY ONLY: nees-core-sdk 0.1.x chat preview. NOT NEES Governance Platform V3.\n\nDo not use this script as a Core V3 integration or production example.\n"""\n\n"""Configure the NEES client explicitly."""

import os

from nees import NEESClient

client = NEESClient(
    api_key=os.environ["NEES_API_KEY"],
    base_url="https://api.nees.cloud",
    timeout=30,
)

result = client.chat(
    "Explain AI runtime governance in one sentence."
)

print(result.reply)
