# NEES Governance Platform Integration Patterns

| Pattern | Integration boundary | Supported responsibility |
| --- | --- | --- |
| Python SDK | Trusted Python service / agent | Client transport for hosted governed-operation lifecycle |
| REST API | Trusted backend of any compatible language | Explicit authenticated operation and evidence calls |
| Gateway / Proxy | Routed backend calls | Enforce governance on supported mediated paths |
| MCP | MCP-compatible host and tools | Govern actions exposed through supported connector |
| Framework adapter | Compatible agent framework | Preserve governance boundary and evidence |

These are **integration patterns**, not a guarantee that each feature is publicly enabled for every account or framework. Verify deployment availability and version-specific configuration before use.

```text
User / UI
   -> trusted application backend / agent
   -> selected supported NEES boundary
   -> hosted governance assessment
   -> application enforces decision
   -> executes only safe/authorized action
   -> reports actual effect and checks evidence
```

**Do not embed NEES runtime credentials in browser JavaScript.** Do not replace an approved target or capability after qualification, infer authority from a prompt, or assume an ALLOW is proof of execution.

See [Complete Integration Guide](NEES-INTEGRATION-GUIDE.md).
