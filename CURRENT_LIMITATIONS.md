# Current Limitations and Compatibility

This repo documents **Core V3 Governance Platform integration** and preserves some older v0.1 developer-preview files.

- Free Developer Preview signup, email verification, sign-in, Free organization creation and allowance display are live and verified as of October 12, 2026. First complete governance execution and every quota boundary have not yet been individually verified on a freshly enrolled Free account.
- Free users receive one organization, one project, one runtime, **one development environment**, two active runtime credentials, 1,000 new submissions/UTC calendar month and 30 authenticated runtime requests/minute. Staging/production environments and self-service paid upgrades are unavailable.
- Billing and Enterprise information panels may be visible without a commercial subscription or enterprise self-service functionality.
- The older `nees-core-sdk` chat client and the newer `nees-sdk` governance client are not interchangeable.
- Exact SDK signatures, command flags and REST request/response schemas must be validated against the installed package and deployed API revision before publication as copy-paste reference code.
- Gateway, MCP, REST and framework adapter availability depends on the specific deployment/connector, credential permissions and supported integration contract; implementation in the ecosystem is not proof of public universal availability.
- NEES governs operations routed through supported integration boundaries; it does not automatically intercept every process or external tool in an application.
- An ALLOW result is authorization, not evidence of completed execution.
- Never extrapolate Governance Lab's simulated outcomes into real-world execution guarantees.
- Public documentation does not expose private Core Engine source, governance policy rules, production assessment bindings or privileged administrative interfaces.

See [Integration Guide](docs/NEES-INTEGRATION-GUIDE.md) and [Production Checklist](docs/PRODUCTION-CHECKLIST.md).
