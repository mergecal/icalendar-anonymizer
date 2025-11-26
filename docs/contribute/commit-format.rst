.. SPDX-FileCopyrightText: 2025 icalendar-anonymizer contributors
.. SPDX-License-Identifier: AGPL-3.0-or-later

=====================
Commit Message Format
=====================

We use `Conventional Commits <https://www.conventionalcommits.org/>`_. They make the changelog automatic and tell you what changed at a glance.

The Format
==========

Every commit message looks like this::

    type(scope): subject

    [optional body]

    [optional footer]

**type** - Required. Pick from the list below.

**scope** - Optional. The part of code you touched (``cli``, ``api``, ``docs``).

**subject** - Required. Short, lowercase, no period at end.

**body** - Optional. Explain why or add context.

**footer** - Optional. Reference issues like ``Closes #123``.

Commit Types
============

**feat**
    New feature. Bumps MINOR version (0.1.0 → 0.2.0).

    Example: ``feat(api): add endpoint for calendar anonymization``

**fix**
    Bug fix. Bumps PATCH version (0.1.0 → 0.1.1).

    Example: ``fix(cli): handle empty input files correctly``

**docs**
    Documentation changes only. No version bump.

    Example: ``docs: update installation instructions``

**refactor**
    Code change that doesn't fix a bug or add a feature.

    Example: ``refactor(core): simplify property filtering logic``

**test**
    Adding or updating tests.

    Example: ``test(api): add tests for URL validation``

**chore**
    Build process, dependencies, tooling. Not user-facing.

    Example: ``chore: update dependencies``

**ci**
    CI configuration changes.

    Example: ``ci: add codecov integration``

**perf**
    Performance improvements.

    Example: ``perf(core): optimize calendar parsing``

**build**
    Build system or dependency changes.

    Example: ``build: update pyproject.toml metadata``

**style**
    Code formatting changes (whitespace, semicolons). No logic changes.

    Example: ``style: fix indentation in parser.py``

**revert**
    Reverting a previous commit.

    Example: ``revert: revert "feat: add calendar filtering"``

Breaking Changes
================

For breaking changes, add ``!`` after the type::

    feat(api)!: remove deprecated /v1/anonymize endpoint

Or put it in the footer::

    feat(api): remove deprecated /v1/anonymize endpoint

    BREAKING CHANGE: The /v1/anonymize endpoint is gone.
    Use /anonymize instead.

Bumps MAJOR version (0.1.0 → 1.0.0).

Rules
=====

- Subject in lowercase
- No period at end
- Max 72 characters for first line
- Use imperative mood: "add feature" not "added feature"
- Reference issues in footer when relevant

Good Examples
=============

::

    feat(cli): add --output flag for file writing

    Closes #42

::

    fix(api): prevent SSRF in URL fetching

    Add URL validation to block internal IP ranges.

    Closes #58

::

    docs: add examples for Python API usage

Bad Examples
============

::

    Added new feature
    Update docs.
    Fixed bug in API endpoint
    FEAT: Add CLI flag

First three don't follow the format. Last one is uppercase.

Pull Request Titles
===================

We use "Squash and merge" for PRs. The PR title becomes the commit message on main.

**PR titles must follow the same format:**

::

    docs: add conventional commits configuration
    feat(api): add calendar anonymization endpoint
    fix(cli): handle empty input files

**Why this matters:**

When you squash merge, all commits in the PR are combined into one. The PR title is used as that commit message. Individual commits in the PR branch are discarded.

**CI will check:**

PR titles are validated automatically. Fix the title if the check fails.

Enforcement
===========

**Local enforcement:**

Install pre-commit hooks::

    pip install pre-commit commitizen
    pre-commit install --hook-type commit-msg

Hooks run commitizen to validate your commit messages before they're created.

**CI enforcement:**

Two checks run on every PR:

- Commit message validation: Checks all commits in the PR
- PR title validation: Ensures PR title follows format (for squash merge)

Both must pass before you can merge.

**To bypass locally (use sparingly):**

::

    git commit --no-verify -m "wip: experimenting with new approach"

Don't abuse this. All commits merged to main must follow the format.
