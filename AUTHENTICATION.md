# Authentication — Governance Platform V3

Sign in to https://app.nees.cloud, create or select the authorized organization, project, runtime and environment, then issue a runtime credential through the supported dashboard workflow.

**Keep credentials server-side.** Inject secrets through the deployment's secret manager and select the configuration mechanism required by your pinned connector/SDK version. Example application-side configuration pattern (no real secret values):

```text
NEES_RUNTIME_URL=https://api.nees.cloud
NEES_RUNTIME_API_KEY=<your-own-runtime-credential>
```

The variable names above were used by one hosted application adapter; **not every connector automatically reads them**. Confirm the version-specific documented configuration.

Never publish actual keys, access tokens, credential prefixes coupled with identifying account data, privileged assessment JSON or confidential authorization results. On an authentication failure, validate scope and configuration without logging the secret; rotate or revoke if exposure is suspected.

**Historical only:** `NEES_API_KEY`, `from nees import NEESClient` and the `client.chat` API belonged to the older `nees-core-sdk` chat preview. They are not instructions for V3 Governance Platform authentication.
