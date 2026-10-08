# Public Governance Results — Core V3

A hosted governance result, application execution result and receipt are **not interchangeable**.

- **Decision:** Whether the operation is permitted by the applicable published governance state.
- **Execution:** Whether the actual external effect was attempted and succeeded, failed, or remained unverified.
- **Evidence:** Correlated records supporting inspection of what the system observed and reported.
- **Receipt:** The supported API's record of the operation outcome. Never claim successful execution solely from a governance ALLOW.

Exact response fields and error schemas are tied to deployed API and SDK version. This guide intentionally does **not** carry unverified example JSON or `NEESHTTPClient` method signatures.

The v0.1 `NEESChatResponse` (`reply`, `session_id`, `request_id`, `trace_id`, `governance`) belonged to the historical **`nees-core-sdk`** chat-only preview and must not be treated as the V3 operation response model.
