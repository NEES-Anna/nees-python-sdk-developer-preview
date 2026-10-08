# Error Handling — Governance Platform V3

**Never treat an HTTP failure, timeout or missing/ambiguous response as approval to execute an external side effect.** The exact Python exception names and HTTP error body shapes are version-specific: confirm them against the pinned `nees-sdk` release or connector implementation.

| Condition | Application behavior |
| --- | --- |
| Invalid authentication or scope | Fail closed, verify configuration, do not print credentials |
| Governance rejection | Do not execute; preserve safe reason/operation correlation |
| Incomplete or stale assessment | Re-qualify with properly published authorized state |
| Unknown action/endpoint | Confirm action registration and deployed API version |
| Timeout after submission/start | Reconcile operation status before any retry |
| Tool target/context mismatch | Stop execution, reobserve and replan |
| Execution failure after ALLOW | Report the observed failure honestly and retain evidence |

NainaSOS used a narrowly-scoped transport fallback for one Windows environment. It was **not** a generic SDK recommendation and never converted a governance denial into authorization.

For historical `nees-core-sdk` 0.1.x exception examples, inspect the older package's PyPI documentation; they are not a verified Core V3 exception API.

See [Troubleshooting](docs/TROUBLESHOOTING.md).
