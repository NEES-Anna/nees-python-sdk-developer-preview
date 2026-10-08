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

Run `nees <command> --help` to inspect the installed version's argument syntax. This repository intentionally does not invent argument flags, request bodies or `NEESHTTPClient` constructor signatures that have not been verified against the published release.

The hosted operation lifecycle is **submit → qualify → start → report**; operation/evidence/receipt retrieval supports inspection of resulting records. Consult [Integration Guide](docs/NEES-INTEGRATION-GUIDE.md).

## Legacy, not V3

The older **`nees-core-sdk` 0.1.x** distribution used `from nees import NEESClient`, `client.chat(...)` and `NEES_API_KEY`. Its examples in [examples/](examples/) are retained for historical reference. They do **not** prove or demonstrate Core V3 operation governance. Migration requires checking imports, endpoints, auth configuration and response contracts; do not assume drop-in compatibility.

## Safe operational principle

The caller retains responsibility for actual external execution, verification and outcome reporting. A governance ALLOW does not itself prove an action executed. A timeout does not establish authorization, denial or execution success.
