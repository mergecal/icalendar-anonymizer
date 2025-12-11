# SPDX-FileCopyrightText: 2025 icalendar-anonymizer contributors
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Command-line interface for icalendar-anonymizer.

Provides the `icalendar-anonymize` and `ican` commands for anonymizing
iCalendar files from the command line.
"""

import sys
from typing import BinaryIO

import click
from icalendar import Calendar

from .anonymizer import anonymize
from .version import __version__


@click.command(
    help=(
        "Anonymize iCalendar files by removing personal data while preserving technical properties."
    ),
    epilog="Examples:\n\n"
    "  icalendar-anonymize input.ics -o output.ics\n"
    "  cat input.ics | icalendar-anonymize > output.ics\n"
    "  ican -v calendar.ics -o anonymized.ics\n",
)
@click.argument(
    "input",
    type=click.File("rb"),
    default="-",
    required=False,
)
@click.option(
    "-o",
    "--output",
    type=click.File("wb"),
    default="-",
    help="Output file (default: stdout)",
)
@click.option(
    "-v",
    "--verbose",
    is_flag=True,
    default=False,
    help="Show processing information",
)
@click.version_option(version=__version__, prog_name="icalendar-anonymizer")
def main(input: BinaryIO, output: BinaryIO, verbose: bool) -> None:  # noqa: A002, FBT001
    """Anonymize an iCalendar file.

    Reads an ICS file, anonymizes personal data, and writes the result.
    Supports stdin/stdout for Unix-style piping.

    Args:
        input: Input file handle (stdin or file)
        output: Output file handle (stdout or file)
        verbose: Whether to show processing information
    """
    try:
        # Get file names for verbose output
        input_name = _get_stream_name(input)
        output_name = _get_stream_name(output)

        if verbose:
            click.echo(f"Reading from: {input_name}", err=True)

        # Read ICS data
        ics_data = input.read()

        if not ics_data:
            click.echo("Error: Input is empty", err=True)
            sys.exit(1)

        if verbose:
            click.echo("Parsing calendar...", err=True)

        # Parse calendar
        try:
            cal = Calendar.from_ical(ics_data)
        except ValueError as e:
            click.echo(f"Error: Invalid ICS file - {e}", err=True)
            sys.exit(1)

        if verbose:
            click.echo("Anonymizing calendar...", err=True)

        # Anonymize (uses random salt by default)
        try:
            anonymized_cal = anonymize(cal)
        except TypeError as e:
            # This shouldn't happen with valid Calendar object, but catch it anyway
            click.echo(f"Error: Anonymization failed - {e}", err=True)
            sys.exit(1)

        if verbose:
            click.echo(f"Writing to: {output_name}", err=True)

        # Write output
        output.write(anonymized_cal.to_ical())

        if verbose:
            click.echo("Done.", err=True)

    except OSError as e:
        # Handle file I/O errors (permission denied, disk full, etc.)
        click.echo(f"Error: {e}", err=True)
        sys.exit(1)
    except KeyboardInterrupt:
        # Handle Ctrl+C gracefully
        click.echo("\nInterrupted", err=True)
        sys.exit(130)  # Standard exit code for SIGINT
    except Exception as e:  # noqa: BLE001
        # Catch-all for unexpected errors
        click.echo(f"Error: Unexpected error - {e}", err=True)
        click.echo(
            "Please report this issue at https://github.com/mergecal/icalendar-anonymizer/issues",
            err=True,
        )
        sys.exit(1)


def _get_stream_name(stream: BinaryIO) -> str:
    """Get a human-readable name for a stream.

    Args:
        stream: File handle or stdin/stdout

    Returns:
        Stream name (e.g., "<stdin>", "/path/to/file.ics")
    """
    # Check if stream is stdin/stdout
    if stream == sys.stdin.buffer:
        return "<stdin>"
    if stream == sys.stdout.buffer:
        return "<stdout>"

    # Get file path from stream
    name = getattr(stream, "name", None)
    if name and name not in ("<stdin>", "<stdout>"):
        return name

    # Fallback
    return "<stream>"


if __name__ == "__main__":
    main()
