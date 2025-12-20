.. SPDX-FileCopyrightText: 2025 icalendar-anonymizer contributors
.. SPDX-License-Identifier: AGPL-3.0-or-later

============
Installation
============

This guide covers installation for end users. For development setup, see :doc:`contributing`.

Requirements
============

- Python 3.11, 3.12, or 3.13
- pip package manager

Basic Installation
==================

Install the core package with pip:

.. code-block:: shell

    pip install icalendar-anonymizer

This installs only the Python package with its core dependency (``icalendar``).

Optional Features
=================

Install optional extras for CLI and web service support:

Command-Line Interface
----------------------

Install with:

.. code-block:: shell

    pip install icalendar-anonymizer[cli]

This installs the :program:`icalendar-anonymize` and :program:`ican` commands. See :doc:`usage/cli` for usage details.

Web Service
-----------

Install with:

.. code-block:: shell

    pip install icalendar-anonymizer[web]

This installs FastAPI, uvicorn, and dependencies for the REST API server. See :doc:`usage/web-service` for usage details.

All Features
------------

Install all optional extras:

.. code-block:: shell

    pip install icalendar-anonymizer[all]

Docker
======

.. note::
    Not yet implemented. See `Issue #8 <https://github.com/mergecal/icalendar-anonymizer/issues/8>`_.

When available:

.. code-block:: shell

    docker pull sashankbhamidi/icalendar-anonymizer

Verifying Installation
======================

Check the installation:

.. code-block:: python

    import icalendar_anonymizer
    print(icalendar_anonymizer.__version__)

Or check the installed version with pip:

.. code-block:: shell

    pip show icalendar-anonymizer

Upgrading
=========

Upgrade to the latest version:

.. code-block:: shell

    pip install --upgrade icalendar-anonymizer

Uninstalling
============

Remove the package:

.. code-block:: shell

    pip uninstall icalendar-anonymizer

Troubleshooting
===============

Import Error
------------

If you get an ``ImportError`` when importing ``icalendar_anonymizer``:

#. Verify the package is installed.

   .. code-block:: shell

       pip list | grep icalendar

#. Check you're using a supported version of Python.

   .. code-block:: shell

       python --version

#. Ensure you're in the correct virtual environment

Dependency Conflicts
--------------------

If you encounter dependency conflicts with ``icalendar``:

#. The package requires a compatible version of ``icalendar``

#. Check your installed version.

   .. code-block:: shell

       pip show icalendar

#. Upgrade if needed.

   .. code-block:: shell

       pip install --upgrade icalendar

Getting Help
============

If you encounter installation issues:

- Check the `Issue Tracker <https://github.com/mergecal/icalendar-anonymizer/issues>`_
- Open a new issue if there isn't an existing one
