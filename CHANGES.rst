==========
Change log
==========

icalendar-anonymizer uses `Semantic Versioning <https://semver.org>`_.

Given a version number MAJOR.MINOR.PATCH, increment the:

- MAJOR version when you make incompatible API changes.
- MINOR version when you add functionality in a backward compatible manner.
- PATCH version when you make backward compatible bug fixes.

When adding entries:

- Add entries as bullet points under the appropriate category.
- Use double backticks for `inline literals <https://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html#rst-roles>`_.

  .. code-block:: rst

      ``PROPERTY``

- Use the `Python domain <https://www.sphinx-doc.org/en/master/usage/domains/python.html>`_ to mark up Python modules, classes, methods, and other Python objects.

  .. code-block:: rst

      :py:func:`function_name`

- Use the ``:file:`` directive for `files <https://www.sphinx-doc.org/en/master/usage/restructuredtext/roles.html#role-file>`_.

  .. code-block:: rst

      :file:`file.py`

- Reference issues and pull requests with a link when relevant.

  .. code-block:: rst

      See `Issue 123 <url>`_.

- Start with a past tense verb, such as "Added", "Fixed", "Removed", "Updated", and other verbs.

0.1.0 (unreleased)
------------------

Breaking changes
''''''''''''''''

New features
''''''''''''

- Added comprehensive CI/CD workflows with GitHub Actions: test matrix across Ubuntu/Windows/macOS with Python 3.11-3.13, Ruff to lint and check the format of code, Codecov integration with multi-platform coverage tracking, PyPI trusted publishing (OIDC, no tokens required), Docker multi-arch builds (AMD64/ARM64), and automatic GitHub releases with generated notes. Added :file:`.github/workflows/tests.yml`, :file:`.github/workflows/publish.yml`, :file:`.github/workflows/docker.yml`, and :file:`.github/workflows/release.yml`. Configured hatch test matrix for local multi-version testing and coverage exclusions in :file:`pyproject.toml`. Added CI/CD badges to :file:`README.md` (tests, coverage, PyPI version, Python versions, Docker pulls). Added test structure with placeholder files referencing related issues. Docker images published to Docker Hub at ``sashankbhamidi/icalendar-anonymizer``. See `Issue 10 <https://github.com/mergecal/icalendar-anonymizer/issues/10>`_.
- Added :file:`.gitattributes` to normalize line endings across platforms (LF in repository, native line endings on checkout).
- Added comprehensive pre-commit hooks configuration with Ruff linting/formatting, file integrity checks, and commit message validation. Updated :file:`CONTRIBUTING.md` with setup instructions and usage documentation. Added Ruff badge to :file:`README.md`. See `Issue 20 <https://github.com/mergecal/icalendar-anonymizer/issues/20>`_.
- Added conventional commits configuration (``.cz.toml``), pre-commit hooks, CI workflows, and documentation. See `Issue 27 <https://github.com/mergecal/icalendar-anonymizer/issues/27>`_.
- Applied Sphinx best practices to ``CHANGES.rst`` including proper RST roles, subheadings, and past tense verbs. See `Issue 31 <https://github.com/mergecal/icalendar-anonymizer/issues/31>`_.
- Added project configuration files (``.gitignore``, ``.editorconfig``, ``.python-version``, ``requirements-dev.txt``). See `Issue 16 <https://github.com/mergecal/icalendar-anonymizer/issues/16>`_.
- Added :file:`LICENSE` with AGPL-3.0-or-later license. See `Issue 14 <https://github.com/mergecal/icalendar-anonymizer/issues/14>`_.
- Added :file:`CONTRIBUTING.md` with development workflow, commit message format, testing requirements, and project structure. See `Issue 15 <https://github.com/mergecal/icalendar-anonymizer/issues/15>`_.
- Added :file:`README.md` with installation instructions and usage examples for Python API, CLI, and web service. See `Issue 13 <https://github.com/mergecal/icalendar-anonymizer/issues/13>`_.
- Added :file:`pyproject.toml` with hatchling build system, hatch-vcs version management, package structure, and dependencies. Tests included in package at ``src/icalendar_anonymizer/tests/``. See `Issue 12 <https://github.com/mergecal/icalendar-anonymizer/issues/12>`_.

Bug fixes
'''''''''
