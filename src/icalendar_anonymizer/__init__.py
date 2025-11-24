"""icalendar-anonymizer - Strip personal data from iCalendar files.

This package provides tools to anonymize iCalendar data while preserving
technical properties for bug reproduction.
"""

from .anonymizer import anonymize
from .version import __version__, __version_tuple__, version, version_tuple

__all__ = [
    "__version__",
    "__version_tuple__",
    "anonymize",
    "version",
    "version_tuple",
]
