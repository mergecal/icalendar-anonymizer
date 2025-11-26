# SPDX-FileCopyrightText: 2025 icalendar-anonymizer contributors
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Version information for icalendar-anonymizer.

This module provides a stable interface to the generated :file:`_version.py` file.

Version as a string:

.. code-block:: pycon

    >>> from icalendar_anonymizer import version
    >>> version  # doctest: +SKIP
    '0.1.0'

Version as a tuple:

.. code-block:: pycon

    >>> from icalendar_anonymizer import version_tuple
    >>> version_tuple  # doctest: +SKIP
    (0, 1, 0)

"""

try:
    from ._version import __version__, __version_tuple__, version, version_tuple
except ModuleNotFoundError:
    __version__ = version = "0.0.0dev0"
    __version_tuple__ = version_tuple = (0, 0, 0, "dev0")

__all__ = [
    "__version__",
    "__version_tuple__",
    "version",
    "version_tuple",
]
