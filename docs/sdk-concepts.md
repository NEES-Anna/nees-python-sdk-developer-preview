# SDK Concepts — Governance Platform V3

- **Client:** The compatible `nees-sdk` 3.x interface, distinct from legacy `NEESClient.chat`.
- **Operation:** A requested action associated with a published, registered action reference.
- **Qualification:** Governance assessment against the required authority/policy/relationship/tool context.
- **Authorization:** Permission under the applicable validated decision; **not proof** of external execution.
- **Execution:** Actual application-owned effect, protected by target/context rechecks.
- **Report:** Truthful record of observed execution outcome.
- **Evidence / receipt:** Auditable projections for tracing and reconciling activity.

The documented hosted sequence is submit → qualify → start → report → inspect. Refer to your pinned release for exact signatures and argument syntax. Do not import private Core implementation packages.

See [SDK Usage](../SDK_USAGE.md) and [Integration Guide](NEES-INTEGRATION-GUIDE.md).
