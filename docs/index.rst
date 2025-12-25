.. SPDX-FileCopyrightText: 2025 icalendar-anonymizer contributors
.. SPDX-License-Identifier: AGPL-3.0-or-later

====================
icalendar-anonymizer
====================

Strip personal data from iCalendar files while preserving technical properties for bug reproduction.

.. grid:: 2
    :gutter: 3

    .. grid-item-card:: 📦 Installation
        :link: installation
        :link-type: doc

        Install with pip or Docker

    .. grid-item-card:: 🐍 Python API
        :link: usage/python-api
        :link-type: doc

        Using the ``anonymize()`` function

    .. grid-item-card:: 💻 Command-Line Interface
        :link: usage/cli
        :link-type: doc

        Using icalendar-anonymize and ican commands

    .. grid-item-card:: 🌐 Web Service
        :link: usage/web-service
        :link-type: doc

        REST API endpoints and self-hosting

    .. grid-item-card:: 📚 API Reference
        :link: api/index
        :link-type: doc

        Function signatures and module documentation

    .. grid-item-card:: 🤝 Contributing
        :link: contributing
        :link-type: doc

        Development workflow and code style

What Gets Anonymized?
=====================

**Personal data** is hashed using SHA-256:

- Event summaries, descriptions, locations
- Attendee and organizer names
- Comments and categories

**Technical properties** are preserved for bug reproduction:

- Dates and times (DTSTART, DTEND, DUE)
- Recurrence rules (RRULE, RDATE, EXDATE)
- Metadata (STATUS, PRIORITY, SEQUENCE)
- Timezones (complete VTIMEZONE components)

See the :doc:`usage/python-api` for the complete property reference table.

Features
========

Deterministic hashing
    Same input + same salt = same output

Structure preservation
    Word count and email format stay intact

UID uniqueness
    UIDs remain unique across the calendar

Customizable
    Use ``preserve`` to keep specific properties

Secure by default
    Unknown properties get anonymized

Well tested
    High test coverage with parametrized tests

Comprehensive documentation
    "If it's not documented, it's broken."

Documentation
=============

.. toctree::
    :maxdepth: 1

    installation
    usage/python-api
    usage/cli
    usage/web-service
    api/index

.. toctree::
    :maxdepth: 1
    :hidden:

    changelog
    contributing

Project Information
===================

License
    AGPL-3.0-or-later

Source Code
    https://github.com/mergecal/icalendar-anonymizer

Issue Tracker
    https://github.com/mergecal/icalendar-anonymizer/issues

PyPI
    https://pypi.org/project/icalendar-anonymizer/
