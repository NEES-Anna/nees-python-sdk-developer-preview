# Installation — NEES Governance Platform V3

The recommended Governance Platform Python package is `nees-sdk` (3.x release-candidate series), **not** the historical `nees-core-sdk` chat client.

Use a virtual environment and verify your chosen published version supports your Python interpreter:

```bash
python -m pip install "nees-sdk==3.0.0rc2"
nees --help
```

The pin above is a previously tested candidate, **not a claim that it is the newest release**. Check https://pypi.org/project/nees-sdk/ and your hosted API compatibility before deployment. Do not install both NEES distributions into the same interpreter without verifying import ownership and compatibility.

Continue with [Quickstart](QUICKSTART.md) and [SDK Usage](SDK_USAGE.md).

## Legacy v0.1 chat interface

The `nees-core-sdk` package and its `NEESClient.chat` examples in `examples/` are archived compatibility references, not V3 integration instructions. The historical public PyPI release used Python 3.9+; do not infer V3's Python requirements from that older package.
