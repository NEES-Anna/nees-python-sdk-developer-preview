# Governance Platform Access

Open https://app.nees.cloud to sign in and use the available organization, project, runtime and environment onboarding screens. Provision a runtime key only for resources your account is authorized to manage.

Hosted Runtime: https://api.nees.cloud

Hosted Control Plane: https://control-api.nees.cloud

Do not use a public client application to carry a secret runtime key. Store it in a trusted backend, environment secret or secrets manager. Never publish a key, a real organization credential, privileged policy binding or sensitive governance record.

Historical `nees-core-sdk` v0.1 used `NEES_API_KEY`; Core V3 integrations may use connector-specific configuration such as `NEES_RUNTIME_API_KEY`. The two should **not** be assumed interchangeable.

See [Quickstart](QUICKSTART.md), [SDK usage](SDK_USAGE.md) and [Security](SECURITY_AND_SCOPE.md).
