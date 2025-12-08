.. SPDX-FileCopyrightText: 2025 icalendar-anonymizer contributors
.. SPDX-License-Identifier: AGPL-3.0-or-later

======================
Command-Line Interface
======================

The command-line interface provides Unix-style tools for anonymizing iCalendar files from the terminal.

Installation
============

Install the CLI with:

.. code-block:: bash

    pip install icalendar-anonymizer[cli]

This installs the Click 8.3.1+ dependency and both command-line tools.

Commands
========

Two commands are provided as aliases:

- :program:`icalendar-anonymize` - Full command name
- :program:`ican` - Short alias for convenience

Both commands work identically.

Basic Usage
===========

Anonymize a File
----------------

Read from a file and write to another file:

.. code-block:: bash

    icalendar-anonymize calendar.ics -o anonymized.ics
    ican calendar.ics -o anonymized.ics

Write to stdout
---------------

Omit the ``-o`` flag to write to stdout:

.. code-block:: bash

    icalendar-anonymize calendar.ics
    ican calendar.ics > anonymized.ics

Read from stdin
---------------

Omit the input argument or use ``-`` to read from stdin:

.. code-block:: bash

    cat calendar.ics | icalendar-anonymize > anonymized.ics
    icalendar-anonymize - -o anonymized.ics

Unix-Style Piping
-----------------

Combine with other Unix tools:

.. code-block:: bash

    # Download and anonymize
    curl https://example.com/calendar.ics | ican > anonymized.ics

    # Anonymize multiple files
    for f in *.ics; do ican "$f" -o "anon-$f"; done

    # Anonymize and compress
    cat calendar.ics | ican | gzip > anonymized.ics.gz

Options Reference
=================

.. program:: icalendar-anonymize

.. option:: [INPUT]

   Input iCalendar file to anonymize. Optional positional argument.

   - **Default**: stdin (``-``)
   - **Format**: File path or ``-`` for stdin
   - **Example**: ``ican calendar.ics``

.. option:: -o <file>, --output <file>

   Output file for anonymized calendar.

   - **Default**: stdout (``-``)
   - **Format**: File path or ``-`` for stdout
   - **Example**: ``ican input.ics -o output.ics``

.. option:: -v, --verbose

   Show processing information on stderr. Displays input/output sources and processing steps.

   - **Flag**: No value required
   - **Output**: Messages written to stderr (not stdout)
   - **Example**: ``ican -v calendar.ics -o anonymized.ics``

   Example verbose output:

   .. code-block:: text

       Reading from: calendar.ics
       Parsing calendar...
       Anonymizing calendar...
       Writing to: anonymized.ics
       Done.

.. option:: --version

   Display version information and exit.

   .. code-block:: bash

       $ ican --version
       icalendar-anonymizer, version 0.1.0

.. option:: --help

   Show usage information and exit.

   .. code-block:: bash

       ican --help

Examples
========

Basic File Conversion
---------------------

.. code-block:: bash

    # Anonymize a single file
    ican calendar.ics -o anonymized.ics

    # Verbose output shows progress
    ican -v calendar.ics -o anonymized.ics

Pipeline Processing
-------------------

.. code-block:: bash

    # Read from stdin, write to stdout
    cat calendar.ics | ican > anonymized.ics

    # Explicit stdin/stdout with -
    ican - < calendar.ics > anonymized.ics

    # Verbose output to stderr doesn't corrupt stdout
    cat calendar.ics | ican -v > anonymized.ics

Batch Processing
----------------

.. code-block:: bash

    # Anonymize all ICS files in directory
    for file in *.ics; do
        ican "$file" -o "anonymized-$file"
    done

    # Process files from a list
    while read -r file; do
        ican "$file" -o "anon-$(basename "$file")"
    done < file-list.txt

Remote Files
------------

.. code-block:: bash

    # Download and anonymize
    curl https://example.com/calendar.ics | ican > local-anon.ics

    # With error checking
    curl -f https://example.com/calendar.ics | ican -v > local-anon.ics

Combining with Other Tools
---------------------------

.. code-block:: bash

    # Anonymize and count events
    ican calendar.ics | grep -c "BEGIN:VEVENT"

    # Anonymize and validate
    ican calendar.ics | ics-validator

    # Compress anonymized output
    ican calendar.ics | gzip > anonymized.ics.gz

What Gets Anonymized?
=====================

The CLI uses the same anonymization as the Python API:

**Anonymized (hashed with SHA-256):**

- Event summaries, descriptions, locations
- Attendee and organizer names (CN parameter)
- Comments, categories, resources
- UIDs (uniqueness preserved)

**Preserved for bug reproduction:**

- All dates and times (DTSTART, DTEND, DUE)
- Recurrence rules (RRULE, RDATE, EXDATE)
- Status, priority, sequence numbers
- Timezones (complete VTIMEZONE)

See :doc:`python-api` for complete property reference.

Error Handling
==============

The CLI provides clear error messages for common issues.

File Not Found
--------------

.. code-block:: text

    $ ican nonexistent.ics
    Error: Could not open 'nonexistent.ics': No such file or directory

**Exit code**: 2

Invalid ICS File
----------------

.. code-block:: text

    $ echo "invalid content" | ican
    Error: Invalid ICS file - Expected instance of <class 'icalendar.cal.Component'>

**Exit code**: 1

Empty Input
-----------

.. code-block:: text

    $ echo "" | ican
    Error: Input is empty

**Exit code**: 1

Permission Denied
-----------------

.. code-block:: text

    $ ican protected.ics -o /root/output.ics
    Error: [Errno 13] Permission denied: '/root/output.ics'

**Exit code**: 1

Keyboard Interrupt
------------------

.. code-block:: text

    $ ican large-file.ics
    ^C
    Interrupted

**Exit code**: 130

Exit Codes
==========

The CLI follows Unix conventions for exit codes:

.. list-table::
   :header-rows: 1
   :widths: 10 20 70

   * - Code
     - Meaning
     - When Used
   * - 0
     - Success
     - Anonymization completed successfully
   * - 1
     - General error
     - Invalid ICS, empty input, I/O errors, unexpected errors
   * - 2
     - File error
     - Input file not found or cannot be opened
   * - 130
     - Interrupted
     - User pressed Ctrl+C (SIGINT)

Troubleshooting
===============

Command Not Found
-----------------

If you get ``command not found`` after installation:

1. Verify the CLI extra is installed:

   .. code-block:: bash

       pip show icalendar-anonymizer | grep cli

2. Check your PATH includes pip's script directory:

   .. code-block:: bash

       python -m site --user-base

3. Reinstall with CLI extra:

   .. code-block:: bash

       pip install --force-reinstall icalendar-anonymizer[cli]

4. Use the full Python module path:

   .. code-block:: bash

       python -m icalendar_anonymizer.cli calendar.ics

Binary Mode on Windows
----------------------

The CLI automatically handles binary mode on Windows. You don't need to worry about CRLF line endings.

If you encounter encoding issues on Windows:

.. code-block:: bash

    # Use binary mode with PowerShell
    Get-Content calendar.ics -Raw | ican > anonymized.ics

Large Files
-----------

The CLI loads the entire file into memory. For very large files (>100MB):

1. **Monitor memory usage**: Use verbose mode to track progress

   .. code-block:: bash

       ican -v large-file.ics -o output.ics

2. **Process in chunks**: Split large calendars before anonymizing

   .. code-block:: bash

       # Example: Split by year, then anonymize
       grep -A 100 "DTSTART:2024" calendar.ics | ican > 2024-anon.ics

3. **Use the Python API**: For programmatic control over memory usage

Hyphen as Filename
------------------

To use a file literally named ``-``:

.. code-block:: bash

    # Use ./ prefix to treat - as a filename
    ican ./- -o output.ics

Debugging
---------

Enable verbose mode to see processing steps:

.. code-block:: bash

    ican -v calendar.ics -o anonymized.ics

Check the exit code after running:

.. code-block:: bash

    ican calendar.ics
    echo $?  # Unix/macOS/Linux
    echo %ERRORLEVEL%  # Windows cmd
    echo $LASTEXITCODE  # Windows PowerShell

Getting Help
============

If you encounter issues with the CLI:

- Use ``ican --help`` for usage information
- Check the `Issue Tracker <https://github.com/mergecal/icalendar-anonymizer/issues>`_
- Open a new issue with:
  - Your command
  - Error message
  - Operating system
  - Python version (``python --version``)
  - Package version (``ican --version``)

Advanced Usage
==============

Custom Salt (Python API Only)
------------------------------

The CLI uses a default salt. For reproducible output with custom salt, use the Python API:

.. code-block:: python

    from icalendar import Calendar
    from icalendar_anonymizer import anonymize

    with open('calendar.ics', 'rb') as f:
        cal = Calendar.from_ical(f.read())

    anonymized = anonymize(cal, salt=b"my-custom-salt-32-bytes-long!")

    with open('anonymized.ics', 'wb') as f:
        f.write(anonymized.to_ical())

See :doc:`python-api` for details.

Preserving Properties (Python API Only)
----------------------------------------

The CLI anonymizes all personal data by default. To preserve specific properties, use the Python API:

.. code-block:: python

    anonymized = anonymize(cal, preserve={"CATEGORIES", "LOCATION"})

See :doc:`python-api` for details.

Integration Examples
====================

Git Pre-Commit Hook
--------------------

Automatically anonymize calendars before committing:

.. code-block:: bash

    #!/bin/bash
    # .git/hooks/pre-commit

    for file in *.ics; do
        if [ -f "$file" ]; then
            ican "$file" -o "anon-$file"
            git add "anon-$file"
        fi
    done

Cron Job
--------

Periodically anonymize shared calendars:

.. code-block:: bash

    # Crontab entry: Anonymize daily at 2 AM
    0 2 * * * /usr/bin/ican /path/to/calendar.ics -o /path/to/anon.ics

Web Service Integration
-----------------------

Use in web applications:

.. code-block:: python

    import subprocess

    def anonymize_uploaded_file(input_path, output_path):
        """Anonymize uploaded ICS file using CLI."""
        result = subprocess.run(
            ['ican', input_path, '-o', output_path],
            capture_output=True,
            text=True
        )
        if result.returncode != 0:
            raise RuntimeError(f"Anonymization failed: {result.stderr}")

See Also
========

- :doc:`python-api` - Python API for programmatic usage
- :doc:`../installation` - Installation instructions
- :doc:`../api/index` - Complete API reference
- :doc:`../contributing` - Development guide
