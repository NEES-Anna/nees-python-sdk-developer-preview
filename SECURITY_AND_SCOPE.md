# Security and Scope

This repository documents the public developer interface of the NEES Python SDK.

It does not document or expose the internal implementation of NEES Core.

## Public interface boundary

Developers should rely only on documented public SDK interfaces.

The SDK intentionally exposes a limited consumer-facing contract.

Internal governance implementation, policy evaluation mechanics, storage design, enforcement internals, and service-side architecture are outside the public SDK contract.

---

## Credential security

Treat NEES API keys as secrets.

Never:

- commit them to source control
- place them in frontend code
- include them in screenshots
- paste them into public issue reports
- store them in public configuration files

Prefer environment variables or a trusted secret-management system.

---

## Backend integration

NEES credentials should normally be used from a trusted backend:

```text
User
  |
  v
Application Backend
  |
  v
NEES Python SDK
  |
  v
NEES Service
```

The SDK is not intended to make a private server credential safe to expose in browser or untrusted client code.

---

## Governance boundary

NEES governance applies through supported service contracts and participating integrations.

The existence of an NEES decision should not be interpreted as universal control over arbitrary code, operating-system activity, network traffic, or external services outside supported integration boundaries.

Applications remain responsible for securely configuring their own:

- infrastructure
- credentials
- external tools
- databases
- operating environments
- network access
- application authentication

---

## No internal implementation dependency

Applications should not attempt to depend on undocumented service behavior.

Only documented SDK interfaces should be considered part of the developer contract.

---

## Reporting a security concern

Do not publish suspected vulnerabilities, credentials, exploit details, or sensitive traces in a public GitHub issue.

Use the official private Nainacore security-contact channel published by Nainacore when reporting security-sensitive findings.
