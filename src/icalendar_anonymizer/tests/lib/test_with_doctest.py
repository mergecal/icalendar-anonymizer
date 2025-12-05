# SPDX-FileCopyrightText: 2025 icalendar-anonymizer contributors
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Doctest validation for core modules."""

import doctest

import icalendar_anonymizer._hash
import icalendar_anonymizer._properties
import icalendar_anonymizer.anonymizer


def test_hash_doctests():
    """Run doctests for _hash module."""
    results = doctest.testmod(icalendar_anonymizer._hash)
    assert results.failed == 0, f"Doctest failures in _hash: {results.failed}"


def test_properties_doctests():
    """Run doctests for _properties module."""
    results = doctest.testmod(icalendar_anonymizer._properties)
    assert results.failed == 0, f"Doctest failures in _properties: {results.failed}"


def test_anonymizer_doctests():
    """Run doctests for anonymizer module."""
    results = doctest.testmod(icalendar_anonymizer.anonymizer)
    assert results.failed == 0, f"Doctest failures in anonymizer: {results.failed}"
