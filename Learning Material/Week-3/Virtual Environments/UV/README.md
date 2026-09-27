# ⚡ UV Commands Cheat Sheet

A step-by-step flow for managing Python projects, environments, and dependencies using **uv**.

[Documentation Link](https://docs.astral.sh/uv/)

---

### 1. Project Initialization

* **`uv init project_name`**  
  Creates a new packaged Python project directory with a standard layout, including `pyproject.toml` and a `src/` folder.

* **`uv init --no-package project_name`**  
  Creates a lightweight workspace project without standard packaging files or a `src/` directory—ideal for standalone scripts and simple applications.

* **`uv init --no-package project_name --python _version`**  
  Initializes a non-packaged project explicitly configured to use a specific Python version (e.g., `--python 3.12`).

---

### 2. Python Version Management

* **`uv python pin _version`**  
  Pins a specific Python version to the current project by creating or updating the `.python-version` file.

---

### 3. Virtual Environment Control

* **`uv venv`**  
  Creates a default `.venv` virtual environment in the root directory using your default installed Python version.

* **`uv venv --python _version`**  
  Creates a `.venv` virtual environment explicitly built with a specific Python version (e.g., `--python 3.11`).

* **`deactivate`**  
  Exits the currently active virtual environment and restores your terminal session back to the global system Python.

---

### 🛠️ 4. Dependency & Sync Workflow

* **`uv add package_name`**  
  Installs a new package (e.g., `requests`, `fastapi`), records it under `[project.dependencies]` in `pyproject.toml`, and updates the lockfile.

* **`uv remove package_name`**  
  Removes a package from the project, updates `pyproject.toml`, and refreshes the lockfile.

* **`uv pip list`**  
  Lists all installed packages in the current virtual environment.


* **`uv lock`**  
  Generates or updates the `uv.lock` file to lock exact versions of all dependencies without altering your active `.venv`.

* **`uv sync`**  
  Synchronizes your virtual environment with `uv.lock`, automatically installing or removing packages so `.venv` matches your exact dependencies.

---

### 5. Code Execution

* **`uv run main.py`**  
  Executes a Python script inside the project environment, automatically ensuring all locked dependencies are available without manual environment activation.