# Python SDK — Core V3 and Legacy Compatibility

## Current governance SDK generation

The Governance Platform Python distribution is **`nees-sdk`**, from the 3.0.0 release-candidate series (3.0.0rc2 was published and validated during integration development). The command-line entry point is **`nees`**.

```bash
python -m pip install "nees-sdk==3.0.0rc2"
nees --help
```

Verify current PyPI availability, supported Python versions and deployed API compatibility before using this exact pin in production.

Documented CLI command families in the V3 SDK include:

```text
nees health
nees actions
nees operation
nees evidence
nees receipt
```

Run `nees <command> --help` to inspect the installed version's argument syntax. The verified client constructors and CLI flags are recorded below. Complete HTTP request/response bodies and runtime behavior still require version-matched validation.

The hosted operation lifecycle is **submit → qualify → start → report**; operation/evidence/receipt retrieval supports inspection of resulting records. Consult [Integration Guide](docs/NEES-INTEGRATION-GUIDE.md).

## Legacy, not V3

The older **`nees-core-sdk` 0.1.x** distribution used `from nees import NEESClient`, `client.chat(...)` and `NEES_API_KEY`. Its examples in [examples/](examples/) are retained for historical reference. They do **not** prove or demonstrate Core V3 operation governance. Migration requires checking imports, endpoints, auth configuration and response contracts; do not assume drop-in compatibility.

## Safe operational principle

The caller retains responsibility for actual external execution, verification and outcome reporting. A governance ALLOW does not itself prove an action executed. A timeout does not establish authorization, denial or execution success.


## Verified Python interface — `nees-sdk==3.0.0rc2`

The following signatures were observed using Python `inspect.signature` on a clean installation of the published wheel on 2026-10-08. **This is interface inspection, not a live authenticated API test.**

```python
import os
from nees import NEESHTTPClient, NEESHTTPConfig, ActionRequest

config = NEESHTTPConfig(
    base_url="https://api.nees.cloud",
    api_key=os.environ["NEES_RUNTIME_API_KEY"],
    timeout_seconds=10.0,
)
client = NEESHTTPClient(config)

request = ActionRequest(
    action_ref="example.action.v1",
    operation_key="example-operation-001",
    input={"message": "example"},
)
```

This constructs SDK models/client only; the example action is NOT a registered action and is not submitted.

| Method | Inspected signature |
| --- | --- |
| `health` | `health(self) -> dict[str, Any]` |
| `list_actions` | `list_actions(self) -> list[ActionDefinition]` |
| `register_action` | `register_action(self, definition: ActionDefinition) -> ActionDefinition` |
| `submit` | `submit(self, request: ActionRequest, assessment: GovernanceAssessment) -> DecisionResult` |
| `qualify` | `qualify(self, operation_id: str) -> QualificationResult` |
| `start` | `start(self, qualification: QualificationResult) -> OperationResult` |
| `report` | `report(self, operation_id: str, qualification_id: str, status: str, result: dict[str, Any]) -> OperationResult` |
| `operation` | `operation(self, operation_id: str) -> OperationResult` |
| `evidence` | `evidence(self, operation_id: str) -> list[EvidenceEvent]` |
| `receipt` | `receipt(self, operation_id: str) -> ReceiptResult | None` |
| `reconcile` | `reconcile(self, operation_id: str, result: dict[str, Any]) -> OperationResult` |
| `answer_clarification` | `answer_clarification(self, request_id: str, response: dict[str, Any]) -> dict[str, Any]` |
| `cancel_governance_request` | `cancel_governance_request(self, request_id: str, reason: str) -> dict[str, Any]` |
| `decide_approval` | `decide_approval(self, request_id: str, *, approved: bool, approver_ref: str, expires_at: float) -> dict[str, Any]` |
| `resume` | `resume(self, request_id: str) -> dict[str, Any]` |

Inspected constructors: `NEESHTTPConfig(base_url, api_key, timeout_seconds=10.0)`, `NEESHTTPClient(config)`, `ActionRequest(action_ref, operation_key, input={})`.

**Do not publish or invent assessment bindings, privileged configuration, production digests or real keys to make these examples appear runnable.** The correct `GovernanceAssessment` values come from an authorized, configured application/runtime. The actual deployed request/response contract, policy decisions and state transitions remain to be confirmed using safely provisioned test resources.

## Verified CLI argument structure

```text
nees [--base-url BASE_URL] [--api-key API_KEY] [--timeout TIMEOUT] health
nees [--base-url BASE_URL] [--api-key API_KEY] [--timeout TIMEOUT] actions
nees [--base-url BASE_URL] [--api-key API_KEY] [--timeout TIMEOUT] operation OPERATION_ID
nees [--base-url BASE_URL] [--api-key API_KEY] [--timeout TIMEOUT] evidence OPERATION_ID
nees [--base-url BASE_URL] [--api-key API_KEY] [--timeout TIMEOUT] receipt OPERATION_ID
```

Use secure environment configuration instead of command-line key literals, which may leak through shell history/process listings.
