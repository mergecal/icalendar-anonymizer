.. SPDX-FileCopyrightText: 2025 icalendar-anonymizer contributors
.. SPDX-License-Identifier: AGPL-3.0-or-later

============
Installation
============

Requirements
============

- Python 3.11 or later
- pip package manager

Basic Installation
==================

Install the core library with pip:

.. code-block:: bash

    pip install icalendar-anonymizer

This installs only the Python library with its core dependency (``icalendar>=6.3.0``).

Optional Features
=================

Install optional extras for CLI and web service support:

Command-Line Interface
----------------------

Install with:

.. code-block:: bash

    pip install icalendar-anonymizer[cli]

This installs the :program:`icalendar-anonymize` and :program:`ican` commands. See :doc:`usage/cli` for usage details.

Web Service
-----------

.. note::
    Not yet implemented. See `Issue #4 <https://github.com/mergecal/icalendar-anonymizer/issues/4>`_.

When available, install with:

.. code-block:: bash

    pip install icalendar-anonymizer[web]

All Features
------------

Install all optional extras:

.. code-block:: bash

    pip install icalendar-anonymizer[all]

Development Installation
========================

To contribute, install with dev dependencies:

.. code-block:: bash

    git clone https://github.com/mergecal/icalendar-anonymizer.git
    cd icalendar-anonymizer
    pip install -e ".[dev]"

This includes:

- pytest for testing
- ruff for linting and formatting
- pre-commit hooks
- commitizen for conventional commits
- reuse for license compliance
- build and twine for packaging

See the :doc:`contributing` guide for more details.

Documentation Building
======================

To build the documentation locally:

.. code-block:: bash

    pip install -e ".[doc]"
    cd docs
    make html

The documentation will be built in ``docs/_build/html/``.

Docker
======

.. note::
    Not yet implemented. See `Issue #8 <https://github.com/mergecal/icalendar-anonymizer/issues/8>`_.

When available:

.. code-block:: bash

    docker pull sashankbhamidi/icalendar-anonymizer

Verifying Installation
======================

Check the installation:

.. code-block:: python

    import icalendar_anonymizer
    print(icalendar_anonymizer.__version__)

Or check the installed version with pip:

.. code-block:: bash

    pip show icalendar-anonymizer

Upgrading
=========

Upgrade to the latest version:

.. code-block:: bash

    pip install --upgrade icalendar-anonymizer

Uninstalling
============

Remove the package:

.. code-block:: bash

    pip uninstall icalendar-anonymizer

Troubleshooting
===============

Import Error
------------

If you get an ``ImportError`` when importing ``icalendar_anonymizer``:

1. Verify the package is installed: ``pip list | grep icalendar``
2. Check you're using Python 3.11+: ``python --version``
3. Ensure you're in the correct virtual environment

Dependency Conflicts
--------------------

If you encounter dependency conflicts with ``icalendar``:

1. The package requires ``icalendar>=6.3.0``
2. Check your installed version: ``pip show icalendar``
3. Upgrade if needed: ``pip install --upgrade icalendar``

Getting Help
============

If you encounter installation issues:

- Check the `Issue Tracker <https://github.com/mergecal/icalendar-anonymizer/issues>`_
- Open a new issue with your Python version, OS, and error message
