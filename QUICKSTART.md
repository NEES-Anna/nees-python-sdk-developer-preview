# Governance Platform Quickstart (Core V3)

This replaces the **recommended** v0.1 chat-only walkthrough. Old chat examples remain under `examples/` as historical material.

## 1. Onboard

Visit https://app.nees.cloud and authenticate. In the dashboard, create/select your **organization**, **project**, **runtime**, and **environment**. Issue a runtime credential using the authorized dashboard workflow. Store it in your secret manager; it may not be displayed again.

## 2. Register and govern an action

In the authorized platform workflow, register the application's external action with a stable action reference, resource, operation, capability, and side-effect semantics. Publish the required authority and policy configuration before submitting an operation.

Example **illustrative identifiers, not provisioning commands**:

```text
organization: example-org
project: sample-agent
runtime: sample-runtime
environment: development
action ref: example.agent.send_message.v1
resource: messaging.outbox
operation: send_message
capability: send_message
side_effect: true
```

The action must actually exist in your own runtime; copying these strings does **not** register it.

## 3. Choose a connector

- **Python:** `python -m pip install "nees-sdk==3.0.0rc2"` (known historical release candidate; confirm currently published compatible version and Python requirements before use).
- **REST:** Use an approved backend connection to the Runtime API.
- **Gateway / MCP / framework connector:** Follow the corresponding supported deployment and connector docs.

For the Python package, inspect the installed CLI with `nees --help` and see [SDK_USAGE.md](SDK_USAGE.md). Do **not** use the v0.1 `NEESClient.chat` quickstart as a V3 example.

## 4. Configure credentials safely

The following names illustrate the application-side integration pattern previously used in NainaSOS; consult your selected connector's current config contract:

```text
NEES_RUNTIME_URL=https://api.nees.cloud
NEES_RUNTIME_API_KEY=<obtain-from-your-own-runtime>
```

Set the API key in your trusted backend runtime or a secret manager. Never commit literal key values, use a browser bundle, or paste them into support tickets.

## 5. Construct a V3 client and request (no network call)

The following constructor signatures were inspected directly from the published `nees-sdk==3.0.0rc2` package. It is a **setup example**, not a valid end-to-end operation: the action identifier is illustrative and assessment bindings must come from your own authorized runtime.

```python
import os
from nees import NEESHTTPClient, NEESHTTPConfig, ActionRequest

api_key = os.environ["NEES_RUNTIME_API_KEY"]

client = NEESHTTPClient(
    NEESHTTPConfig(
        base_url="https://api.nees.cloud",
        api_key=api_key,
        timeout_seconds=20.0,
    )
)
request = ActionRequest(
    action_ref="example.action.v1",
    operation_key="example-request-001",
    input={"message": "Hello"},
)
# No operation is sent here.
```

`NEESHTTPClient` rejects an empty API key during initialization, even before calling its `health()` method. Set the environment variable privately; never paste its value into a public issue or CLI arguments.

## 6. Govern and verify

Use the supported submit → qualify → start → report workflow. Inspect the operation, evidence, and receipt using your version's documented commands/routes.

**Do not execute a side effect unless the governing result and the local target/context checks allow it.** Treat reject, missing authority, ambiguous response and unavailable service as fail-closed. Record the *actual* result, not merely a planned or authorized result.

## 7. Acceptance tests

Verify one allowed operation, one blocked operation, one stale/invalid configuration, one transport failure, and one external execution failure. Check that evidence/receipt and reported execution state agree.

Next: [Complete integration guide](docs/NEES-INTEGRATION-GUIDE.md).
