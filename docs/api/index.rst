.. SPDX-FileCopyrightText: 2025 icalendar-anonymizer contributors
.. SPDX-License-Identifier: AGPL-3.0-or-later

=============
API Reference
=============

Auto-generated from docstrings.

Public API
==========

The :py:func:`icalendar_anonymizer.anonymize` function and version information.

.. toctree::
   :maxdepth: 2

   anonymizer
   version

Internal Modules
================

Internal implementation. Not part of the public API - may change without notice.

.. toctree::
   :maxdepth: 2

   hash
   properties

Module Overview
===============

:mod:`icalendar_anonymizer.anonymizer`
    Main anonymization function and logic

:mod:`icalendar_anonymizer.version`
    Version information access

:mod:`icalendar_anonymizer._hash`
    Hash functions for text, email, and UID hashing (internal)

:mod:`icalendar_anonymizer._properties`
    Property classification constants (internal)

Quick Reference
===============

.. py:currentmodule:: icalendar_anonymizer

Main Function
-------------

.. autosummary::
   :nosignatures:

   anonymize

Version Information
-------------------

.. autosummary::
   :nosignatures:

   __version__
   __version_tuple__
   version
   version_tuple
