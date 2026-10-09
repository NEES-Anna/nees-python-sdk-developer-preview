# Governance Integration Troubleshooting

| Symptom | Likely boundary | Safe next step |
| --- | --- | --- |
| 401 / authentication failure | Credential missing, expired, wrong scope | Verify secret injection and assigned runtime; rotate/revoke as appropriate; never log key |
| 403 / governance or authorization rejection | Permission or published policy | Inspect documented reason and scope; do not override locally |
| 404 / unknown action or endpoint | Action not registered, wrong runtime, unsupported route | Compare deployed API version and action reference |
| assessment incomplete | Required commitments not bound | Resolve current action and published scope in the Dashboard Integration Manager; never invent commitments |
| 409 assessment mismatch | Missing or modified baseline | Inspect current governance; do not overwrite customized policy just to export |
| No action/scope dropdown choice | No matching current registration or published authority/policy | Verify selected runtime and existing publication |
| stale decision / version | Governance state changed | Re-qualify with current published state; do not reuse an old approval |
| transport timeout/unavailable | Network / hosted service | Fail closed; reconcile uncertain requests before retrying side effects |
| foreground target mismatch | Application environment differs from plan | Stop, reobserve and replan; do not report a side effect as executed |
| Evidence shows ALLOW but execution missing | Authorization and execution are distinct | Check local verifier, report state and receipt |
| Odd decision on free-form scenario | Input normalizer inferred facts | Inspect normalized input; preserve unknown/ambiguous state |
| duplicate side effect after retry | Missing idempotency/reconciliation | Use supported idempotency guarantees, correlate operations and inspect before retry |

Always sanitize issue reports: remove credentials, production identifiers, policy digests, customer content and full raw traces.

See [Integration Guide](NEES-INTEGRATION-GUIDE.md).
