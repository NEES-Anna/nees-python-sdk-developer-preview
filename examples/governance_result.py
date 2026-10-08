"""LEGACY ONLY: nees-core-sdk 0.1.x chat preview. NOT NEES Governance Platform V3.\n\nDo not use this script as a Core V3 integration or production example.\n"""\n\n"""Read the public governance fields returned by the SDK."""

from nees import NEESClient

client = NEESClient()

result = client.chat(
    "Explain why runtime governance is useful for AI applications."
)

print("Reply:")
print(result.reply)

print("\nGovernance:")
print("Decision:", result.governance.decision)
print("Status:", result.governance.status)
print("Reason:", result.governance.reason)

print("\nRequest:")
print("Request ID:", result.request_id)
print("Trace ID:", result.trace_id)
