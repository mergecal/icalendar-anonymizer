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

- Added conventional commits configuration (``.cz.toml``), pre-commit hooks, CI workflows, and documentation. See `Issue 27 <https://github.com/mergecal/icalendar-anonymizer/issues/27>`_.
- Applied Sphinx best practices to ``CHANGES.rst`` including proper RST roles, subheadings, and past tense verbs. See `Issue 31 <https://github.com/mergecal/icalendar-anonymizer/issues/31>`_.
- Added project configuration files (``.gitignore``, ``.editorconfig``, ``.python-version``, ``requirements-dev.txt``). See `Issue 16 <https://github.com/mergecal/icalendar-anonymizer/issues/16>`_.
- Added AGPL-3.0-or-later license. See `Issue 14 <https://github.com/mergecal/icalendar-anonymizer/issues/14>`_.
- Added :file:`CONTRIBUTING.md` with development workflow, commit message format, testing requirements, and project structure. See `Issue 15 <https://github.com/mergecal/icalendar-anonymizer/issues/15>`_.

Bug fixes
'''''''''