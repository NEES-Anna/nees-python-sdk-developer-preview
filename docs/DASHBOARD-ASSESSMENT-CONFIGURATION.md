# Dashboard Assessment Configuration — Developer Preview

## Hosted onboarding

1. Sign in to https://app.nees.cloud and select your authorized organization.
2. Open **Infrastructure → Assessment configuration manager**.
3. Select existing Project, Runtime and Environment.
4. Select **Registered action** from the runtime-scoped dropdown; no manual action ref is required.
5. Select **Published scope** from the matching current authority/policy state. It does not list historical scopes or invent scopes.
6. Choose **Python SDK**, **REST**, **MCP adapter**, or **Application environment variable**.
7. Click **Resolve existing assessment**, inspect the export and **Copy configuration**.

The hosted Governance Lab UI was checked on October 9, 2026: a selected synthetic action and published scope produced a REST assessment export. This proves read-only configuration generation, **not** REST action execution or governance ALLOW.

## Export and connector boundaries

The response includes action, scope, actor/principal, resource, operation and capability, and the ref/version/digest commitments for authority, policy, relationship and tool policy. It does **not** contain an API key.

- REST: use the JSON as the `assessment` object in a version-matched Runtime `POST /v1/operations` request; supply the registered action request and separate backend-owned runtime key.
- Python SDK: pass these facts using the matching SDK/API contract. The export does not install the SDK or issue credentials.
- MCP: map these facts through your supported governance adapter. The export is **not** complete MCP server configuration.
- Application environment: a single-line variable such as `NEES_RUNTIME_ASSESSMENT_BINDINGS` is an example app convention, not a universal SDK setting.

Keep credentials only in trusted backends or secret managers.

## Safety and errors

**Resolve existing assessment** is read-only and permission-checked. **Publish baseline & resolve** explicitly updates authority, policy, relationship and tool-policy records and increments versions; never use it casually to repair a missing dropdown item, because it may overwrite reviewed or customized governance.

- Empty action dropdown: no registered action for that runtime/identity.
- Empty scope dropdown: no matching current authority/policy scope discovered. It does not imply no older or custom configuration exists.
- HTTP 409: the exact current baseline does not match or is missing; inspect instead of guessing or republishing.
- HTTP 401/403: missing authentication or insufficient organization permissions.
- HTTP 404: unknown action/runtime/environment.
- HTTP 503: dependent read service unavailable.

The exported assessment is version-bound and can become stale. Runtime qualification, local target checks, actual execution reporting, evidence and receipt reconciliation remain necessary before production effects.

See [Quickstart](../QUICKSTART.md), [Integration guide](NEES-INTEGRATION-GUIDE.md), and [Production checklist](PRODUCTION-CHECKLIST.md).
