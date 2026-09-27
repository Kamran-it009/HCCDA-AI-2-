
<h1> Virtual Environment Management </h1>

<br />

| Features | **Poetry** | **Anaconda (Conda)** | **uv** |
| :--- | :--- | :--- | :--- |
| **Primary Focus** | Project dependency management & publishing | Data science & binary environment ecosystem | Fast, unified Python toolchain manager |
| **Written In** | Python | Python & C | Rust |
| **Python Version Switching** | ❌ Requires system Python | ✅ Via Conda packages | ✅ Built-in automated management |
| **Package Management (`pip`)** | ✅ High-level wrapper | ✅ Custom Conda channels & `pip` | ✅ Extremely fast `pip` replacement |
| **Lockfile Support** | ✅ `poetry.lock` | ❌ Basic (`environment.yml`) | ✅ `uv.lock` |
| **Non-Python / C Libraries** | ❌ No | ✅ System C/C++, CUDA drivers | ❌ No (Python/wheels only) |
| **Speed & Performance** | Moderate to Slow | Moderate to Slow | 🚀 Extremely fast (10–100x) |
| **Standard Config File** | `pyproject.toml` | `environment.yml` | `pyproject.toml` |
| **Best For...** | Library maintainers needing PyPI packaging/publishing | Machine learning engineers & heavy scientific stacks | Modern web apps, fast CI/CD pipelines, and unified workflows |
