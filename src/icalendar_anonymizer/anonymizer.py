# SPDX-FileCopyrightText: 2025 icalendar-anonymizer contributors
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Core anonymization engine for iCalendar files.

Anonymizes personal data while preserving technical properties needed for
bug reproduction. Uses deterministic hashing with configurable salt.
"""

from icalendar import Alarm, Calendar, Event, Journal, Todo
from icalendar.cal import Component
from icalendar.prop import vCalAddress

from ._hash import (
    generate_salt,
    hash_caladdress_cn,
    hash_email,
    hash_text,
    hash_uid,
)
from ._properties import (
    should_preserve_component,
    should_preserve_property,
)


def _should_preserve(prop_name: str, preserve_set: set[str]) -> bool:
    """Check if a property should be preserved.

    Args:
        prop_name: Property name (uppercase)
        preserve_set: Set of additional properties to preserve (uppercase)

    Returns:
        True if property should be preserved
    """
    return should_preserve_property(prop_name) or prop_name in preserve_set


def anonymize(
    cal: Calendar,
    salt: bytes | None = None,
    preserve: set[str] | None = None,
) -> Calendar:
    """Anonymize an iCalendar object.

    Removes personal data (names, emails, locations, descriptions) while
    preserving technical properties (dates, recurrence, timezones). Uses
    deterministic hashing so the same input produces the same output with
    the same salt.

    Args:
        cal: The Calendar object to anonymize
        salt: Optional salt for hashing. If None, generates random salt.
              Pass the same salt to get consistent output across runs.
        preserve: Optional set of additional property names to preserve.
                 Case-insensitive. User must ensure these don't contain
                 sensitive data. Example: {"CATEGORIES", "COMMENT"}

    Returns:
        New anonymized Calendar object

    Raises:
        TypeError: If cal is not a Calendar object or salt is not bytes
    """
    if not isinstance(cal, Calendar):
        raise TypeError(f"Expected Calendar, got {type(cal).__name__}")

    if salt is None:
        salt = generate_salt()
    elif not isinstance(salt, bytes):
        raise TypeError(f"salt must be bytes, got {type(salt).__name__}")

    if preserve is not None and not isinstance(preserve, set):
        raise TypeError(f"preserve must be a set or None, got {type(preserve).__name__}")

    # Normalize preserve set to uppercase
    preserve_upper = {p.upper() for p in preserve} if preserve else set()

    # UID mapping to maintain uniqueness across calendar
    uid_map: dict[str, str] = {}

    # Create new calendar to avoid modifying original
    new_cal = Calendar()

    # Copy calendar-level properties (applying same filtering rules)
    for key, value in cal.property_items():
        prop_name = key.upper()
        if _should_preserve(prop_name, preserve_upper):
            new_cal.add(key, value)
        else:
            # Anonymize calendar-level properties too
            anonymized = _anonymize_property_value(value, salt)
            new_cal.add(key, anonymized)

    # Process only top-level components (not subcomponents)
    for component in cal.subcomponents:
        # Check if this component should be completely preserved
        if should_preserve_component(component.name):
            # VTIMEZONE: preserve entirely
            new_cal.add_component(component)
            continue

        # Anonymize component
        new_component = _anonymize_component(component, salt, uid_map, preserve_upper)
        new_cal.add_component(new_component)

    return new_cal


def _anonymize_component(
    component: Component,
    salt: bytes,
    uid_map: dict[str, str],
    preserve: set[str],
) -> Component:
    """Anonymize a single component (VEVENT, VTODO, etc.).

    Args:
        component: The component to anonymize
        salt: Salt for hashing
        uid_map: UID mapping for maintaining uniqueness
        preserve: Set of additional property names to preserve (uppercase)

    Returns:
        New anonymized component
    """
    component_types = {
        "VEVENT": Event,
        "VTODO": Todo,
        "VJOURNAL": Journal,
        "VALARM": Alarm,
    }

    component_class = component_types.get(component.name, Component)
    new_component = component_class()

    # Process each property
    for key, value in component.property_items():
        prop_name = key.upper()

        # Check if property should be preserved
        if _should_preserve(prop_name, preserve):
            # Preserve as-is
            new_component.add(key, value)
        elif prop_name == "UID":
            # Special handling: hash but maintain uniqueness
            original_uid = str(value)
            hashed_uid = hash_uid(original_uid, salt, uid_map)
            new_component.add(key, hashed_uid)
        elif prop_name in ("ATTENDEE", "ORGANIZER"):
            # Special handling: anonymize email + CN parameter, preserve others
            if isinstance(value, vCalAddress):
                new_value = _anonymize_caladdress(value, salt)
            else:
                # Fallback for string values
                new_value = hash_email(str(value), salt)
            new_component.add(key, new_value)
        else:
            # Default: anonymize (includes SUMMARY, DESCRIPTION, LOCATION,
            # COMMENT, CONTACT, CATEGORIES, and unknown properties)
            anonymized_value = _anonymize_property_value(value, salt)
            new_component.add(key, anonymized_value)

    # Process subcomponents (e.g., VALARM inside VEVENT)
    for subcomponent in component.subcomponents:
        new_subcomponent = _anonymize_component(subcomponent, salt, uid_map, preserve)
        new_component.add_component(new_subcomponent)

    return new_component


def _anonymize_property_value(value, salt: bytes):
    """Anonymize a property value.

    Args:
        value: The property value to anonymize
        salt: Salt for hashing

    Returns:
        Anonymized value
    """
    # Handle different value types
    if isinstance(value, str):
        return hash_text(value, salt)
    if isinstance(value, bytes):
        return hash_text(value.decode("utf-8", errors="replace"), salt).encode("utf-8")
    if isinstance(value, list):
        # Handle lists (like CATEGORIES)
        return [hash_text(str(item), salt) for item in value]
    # For other types, convert to string and hash
    return hash_text(str(value), salt)


def _anonymize_caladdress(caladdress: vCalAddress, salt: bytes) -> vCalAddress:
    """Anonymize ATTENDEE or ORGANIZER (vCalAddress).

    Anonymizes the email and CN parameter while preserving mailto: prefix
    and other parameters (ROLE, PARTSTAT, RSVP, etc.).

    Args:
        caladdress: The vCalAddress to anonymize
        salt: Salt for hashing

    Returns:
        New anonymized vCalAddress
    """
    # Get the email address
    email = str(caladdress)

    # Hash the email while preserving mailto: prefix
    if email.startswith("mailto:"):
        email_part = email[7:]  # Remove mailto: prefix
        hashed_email = hash_email(email_part, salt)
        new_email = f"mailto:{hashed_email}"
    else:
        new_email = hash_email(email, salt)

    # Create new vCalAddress
    new_caladdress = vCalAddress(new_email)

    # Copy all parameters, anonymizing CN
    for param_key, param_value in caladdress.params.items():
        if param_key.upper() == "CN":
            # Anonymize common name
            new_caladdress.params[param_key] = hash_caladdress_cn(param_value, salt)
        else:
            # Preserve other parameters (ROLE, PARTSTAT, RSVP, etc.)
            new_caladdress.params[param_key] = param_value

    return new_caladdress
