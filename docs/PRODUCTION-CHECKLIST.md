# Production Integration Checklist

- [ ] Supported SDK or connector version pinned and API compatibility checked
- [ ] Organization, project, runtime, environment and action registered through authorized platform workflow
- [ ] API credentials restricted to backend, scoped to correct runtime and excluded from logs/browser/build output
- [ ] Credential rotation/revocation and incident response procedure tested
- [ ] Published governance and required assessment commitments validated (no example bindings copied)
- [ ] ALLOW executes only the exactly authorized target/action
- [ ] DENY, missing policy, stale authority and incomplete assessment all fail closed
- [ ] Network timeout/uncertain response never authorizes an external effect
- [ ] Local target/environment verification prevents execution on wrong resource
- [ ] Execute/report/receipt reflect actual outcome, including failures
- [ ] Duplicate request, retry and idempotency behavior tested against side effects
- [ ] Evidence and receipt are correlatable without leaking sensitive payloads
- [ ] Staging acceptance evidence retained privately and sanitized public examples reviewed
- [ ] Only public SDK/API contracts imported; no private Core code or policy internals shipped

Release gate: do not mark the integration production-ready until all applicable checks are verified.
