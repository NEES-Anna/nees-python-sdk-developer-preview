# Installation

## Requirements

The NEES Python SDK requires:

- Python 3.9 or newer
- internet access to the configured NEES API endpoint
- a valid NEES API key

---

## Install from PyPI

```bash
pip install nees-core-sdk
```

Upgrade an existing installation:

```bash
pip install --upgrade nees-core-sdk
```

---

## Verify installation

```bash
python -c "from nees import NEESClient; print('NEES SDK installed')"
```

Expected output:

```text
NEES SDK installed
```

---

## Package name vs import name

The PyPI distribution name is:

```text
nees-core-sdk
```

The Python package is imported as:

```python
import nees
```

or:

```python
from nees import NEESClient
```

---

## Virtual environment

Using a virtual environment is recommended.

Windows:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install nees-core-sdk
```

Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install nees-core-sdk
```

---

## Next

Continue with [QUICKSTART.md](QUICKSTART.md).
