# API Access

The NEES Python SDK requires a valid NEES API key.

Developer and evaluation access is currently provided by Nainacore Emotional Tech.

To request access, visit:

https://nees.cloud

Do not purchase, share, publish, or request API credentials through unofficial third parties.

Once you receive a key, configure it as:

Windows PowerShell:

```powershell
$env:NEES_API_KEY="your-api-key"

# Linux/macOS:

export NEES_API_KEY="your-api-key"

Never commit your API key to source control.

No backend provisioning details. No key-generation mechanics.