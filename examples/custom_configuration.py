"""Configure the NEES client explicitly."""

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
