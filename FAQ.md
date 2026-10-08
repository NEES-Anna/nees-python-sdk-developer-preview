# NEES Governance Platform — Frequently Asked Questions

**Which Python package should I use?** For Core V3 hosted governance integrations, use the compatible `nees-sdk` 3.x release-candidate generation. `nees-core-sdk` 0.1.x documented an older chat-only client.

**Where do I create an API key?** Use your authorized runtime onboarding workflow in https://app.nees.cloud.

**Can a browser store the runtime key?** No. Keep it in a trusted backend environment.

**Does governance ALLOW mean the action happened?** No. The application must perform, verify and accurately report actual execution.

**Can I govern non-Python applications?** The architecture supports connector-based approaches including REST, Gateway, MCP and framework adapters, subject to actual deployment, contract and availability.

**Does the public SDK expose Core internals?** No. Integrate with documented public contracts.

**Can I copy Governance Lab decisions as production policy?** No. Its synthetic scenarios demonstrate behavior and are not a substitute for your organization's published policy or an actual execution proof.

**Where should I begin?** [Quickstart](QUICKSTART.md), [Integration Guide](docs/NEES-INTEGRATION-GUIDE.md), and [Production Checklist](docs/PRODUCTION-CHECKLIST.md).
