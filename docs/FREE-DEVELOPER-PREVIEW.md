# Free Developer Preview — Start Here

**Live public early access · October 12, 2026**

[Create a Free Account](https://app.nees.cloud/login) · [Hosted Developer Guide](https://app.nees.cloud/developer-preview) · [NEES Dashboard](https://app.nees.cloud)

## What you can use

| Feature or allowance | Free Developer |
| --- | --- |
| Verified account / organization | 1 Free organization per account |
| Projects / runtimes / environments | 1 / 1 / 1 |
| Environment type | **Development only** |
| Active runtime API credentials | 2 |
| New governance operation submissions | **1,000 each UTC calendar month** |
| Authenticated runtime requests | 30 per minute per organization |

The monthly counter covers **new governance operation submissions**, not LLM tokens. Unused credits do not roll over. Looking up an existing operation, evidence or receipt and reporting/reconciling it does not consume a new-submission credit, though request-rate restrictions still apply. Your **Dashboard → Billing** page shows the current authoritative Free allowance.

**Unavailable on Free:** another Free organization, more resources than the caps, staging/production environments, checkout and self-service paid upgrades. Backend entitlements enforce these limits even if an API client offers unsupported options.

## First action in your browser

1. Sign up and verify the email delivered to your inbox.
2. Sign in and create your Free Developer organization.
3. Open **Developer Onboarding**. Create a project, runtime and development environment with identity binding, then issue your **one-time** runtime credential. Keep the secret server-side; do not expose it in frontend code, issues or screenshots.
4. Choose an integration path and select **Run informational proof** or **Run governed execution proof** in the Dashboard.
5. Inspect your Core governance decision, evidence and any receipt. The built-in execution proof is a **bounded hosted demonstration**, not proof that Gmail, GitHub or your own external tool performed an effect.

If onboarding fails halfway through, inspect **Infrastructure** before trying to create the same resource again.

## Integrate your own agent

For a Python backend, use a compatible published `nees-sdk` version; see [SDK Usage](../SDK_USAGE.md). For a non-Python backend, use the version-matched hosted Runtime REST contract with the separate server-side `X-NEES-API-Key` header. Gateway, MCP, framework adapters and the connector catalog require **additional trusted-host configuration**; selecting a tile does not automatically connect third-party services.

For your real consequential action, register the actual action and publish authorized governance. In **Infrastructure → Assessment configuration manager**, select the **Registered action**, **Published scope** and integration method, then **Resolve existing assessment**. This provides a version-bound assessment export, **not an API credential**. **Publish baseline & resolve** is a state-changing, privileged operation and can replace prior governance commitments. Do not use it casually.

An ALLOW decision is **not** execution permission by itself and never proves the action happened. Executable side effects require qualification/permit/start, local target checks, actual application execution, truthful report and evidence reconciliation.

## Which Dashboard sections are available?

- **Overview:** tenant counts and the Free allowance.
- **Developer Onboarding:** resource creation and bounded hosted proof.
- **Infrastructure:** resource and credential management, registered actions, published scopes and assessment export.
- **Governance:** commitment inspection, policy metadata and authorized human reviews, where configured.
- **Evidence:** inspect operation, evidence, audit and receipt when available.
- **Usage:** descriptive lifecycle telemetry and trends; this is **not** the quota ledger.
- **Billing:** Free Plan and usage limits; there is **no checkout or self-service paid upgrade**.
- **Enterprise:** some read-only metadata is visible, **not proof of active enterprise entitlement**.
- **Settings:** organization profile, role-dependent memberships and evidence retention. Email invitations and organization-profile editing are not self-service.

## What has been verified?

**Live verified:** signup, verification email, authenticated sign-in, Free organization creation and allowance display.

**Not claimed as production-verified for a new Free account:** the full hosted execution lifecycle, all boundary exhaustion/replay cases, every connector and production workloads. Developer Preview is development/evaluation access, not a production SLA.

[Open a sanitized feedback issue](https://github.com/NEES-Anna/nees-python-sdk-developer-preview/issues). Do **not** post credentials, confidential traces, customer data or privileged assessment digests. See [Security Policy](../SECURITY.md) for sensitive findings.
