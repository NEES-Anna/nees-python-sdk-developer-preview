# Frequently Asked Questions

## What is the NEES Python SDK?

The NEES Python SDK is the official Python client for supported NEES runtime services.

It allows Python applications to interact with NEES through a deliberately limited public interface.

---

## Does this repository contain NEES Core?

No.

This repository contains documentation and developer examples only.

NEES Core implementation is not included.

---

## Is the SDK itself the NEES Core Engine?

No.

The SDK is a client interface.

NEES Core operates behind the supported NEES service boundary.

---

## What does SDK v0.1 support?

The current SDK supports authenticated chat invocation.

---

## How do I install it?

```bash
pip install nees-core-sdk
```

---

## What do I import?

```python
from nees import NEESClient
```

---

## Where should I store my API key?

Prefer an environment variable or trusted secret-management system.

Example:

```text
NEES_API_KEY
```

Do not commit credentials to Git.

---

## Can I use the SDK from frontend JavaScript?

The Python SDK is intended for Python environments.

More importantly, private NEES API credentials should normally remain on trusted backend infrastructure rather than being exposed to browsers.

---

## Does the SDK expose how NEES makes governance decisions?

No.

The SDK exposes supported public results, not the proprietary governance implementation.

---

## Can I rely on undocumented response fields?

No.

Applications should depend only on documented SDK properties.

---

## Is NEES only for chatbots?

NEES as a platform is broader than simple chat use cases.

However, the current Python SDK v0.1 exposes only the documented chat capability.

Future SDK releases may expose additional supported capabilities.

---

## Where can I learn more?

Visit:

https://nees.cloud
