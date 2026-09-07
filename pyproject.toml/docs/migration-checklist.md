---
last_verified: 2026-09-07
tool_version: n/a
---

# Migrating from setup.py/setup.cfg/requirements.txt to pyproject.toml

## Purpose

Modern Python packaging consolidates project metadata in pyproject.toml, replacing the older trio of setup.py, setup.cfg, and requirements.txt. This guide walks through converting an existing project to the single-file format.

## When to use

- A project still uses setup.py or setup.cfg for metadata
- Dependencies are split across requirements.txt and setup.py install_requires
- You want a single source of truth for build-system, project metadata, and tool configuration

## Prerequisites

- An existing Python package with setup.py, setup.cfg, or requirements.txt
- A build backend installed (setuptools, hatchling, flit, etc.)

## Steps

1. **Inventory current files.** List what each existing file declares: project name, version, dependencies, entry points, and tool configs.

2. **Add build-system table.** Declare the build backend and its requirements. For setuptools:

   ```toml
   [build-system]
   requires = ["setuptools", "wheel"]
   build-backend = "setuptools.build_meta"
   ```

3. **Migrate project metadata.** Move name, version, description, authors, and classifiers from setup.py or setup.cfg into [project]. Remove setup.py arguments that now live under [project].

4. **Handle dynamic fields.** If version or description is computed in setup.py, list them under `dynamic = ["version"]` and use [tool.setuptools.dynamic] to declare how to read them.

5. **Move dependencies.** Copy install_requires to [project.dependencies] and extras_require to [project.optional-dependencies].

6. **Migrate package discovery.** If setup.py used find_packages(), replace with [tool.setuptools.packages.find] or set [tool.setuptools.packages] explicitly.

7. **Move tool configs.** Settings that lived in setup.cfg sections become [tool.*] tables in pyproject.toml.

8. **Validate.** Run the build command and install the wheel in a fresh venv to confirm metadata and dependencies resolve correctly.

## Verify

- Build succeeds without setup.py
- Installing the wheel pulls the expected dependencies
- Tool behavior matches pre-migration behavior

## Common errors

- **Missing version:** setup.py often computed version dynamically; pyproject.toml requires either a static version field or a dynamic declaration.
- **Entry points lost:** console_scripts and gui_scripts in setup.py entry_points become [project.scripts] and [project.gui-scripts].
- **Package data forgotten:** package_data and include_package_data in setup.py map to [tool.setuptools.package-data] and [tool.setuptools.include-package-data].
- **Tool config drift:** Some tools read setup.cfg sections differently than pyproject.toml [tool.*] tables; run the tool's own validation command after migration.
