<!--- SPDX-FileCopyrightText: 2025 icalendar-anonymizer contributors -->
<!--- SPDX-License-Identifier: AGPL-3.0-or-later -->

# icalendar-anonymizer

Strip personal data from iCalendar files while preserving technical properties for bug reproduction.

Calendar bugs are hard to reproduce without actual calendar data, but people can't share their calendars publicly due to privacy concerns. This tool uses hash-based anonymization to remove sensitive information (names, emails, locations, descriptions) while keeping all date/time, recurrence, and timezone data intact.

[![Tests](https://github.com/mergecal/icalendar-anonymizer/actions/workflows/tests.yml/badge.svg)](https://github.com/mergecal/icalendar-anonymizer/actions/workflows/tests.yml)
[![codecov](https://codecov.io/gh/mergecal/icalendar-anonymizer/graph/badge.svg?token=6tcJpy0th3)](https://codecov.io/gh/mergecal/icalendar-anonymizer)
[![PyPI version](https://img.shields.io/pypi/v/icalendar-anonymizer.svg)](https://pypi.org/project/icalendar-anonymizer/)
[![Python versions](https://img.shields.io/pypi/pyversions/icalendar-anonymizer.svg)](https://pypi.org/project/icalendar-anonymizer/)
[![Docker pulls](https://img.shields.io/docker/pulls/sashankbhamidi/icalendar-anonymizer.svg)](https://hub.docker.com/r/sashankbhamidi/icalendar-anonymizer)
[![License: AGPL-3.0-or-later](https://img.shields.io/badge/License-AGPL%203.0--or--later-blue.svg)](LICENSE)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

## Installation

```bash
# Library only
pip install icalendar-anonymizer

# With CLI tool
pip install icalendar-anonymizer[cli]

# With web service
pip install icalendar-anonymizer[web]

# Everything
pip install icalendar-anonymizer[all]
```

**Docker:**

```bash
docker-compose up -d
```

**From source:**

```bash
git clone https://github.com/mergecal/icalendar-anonymizer.git
cd icalendar-anonymizer
pip install -e ".[dev]"
```

## Usage

### Python API

```python
from icalendar import Calendar
from icalendar_anonymizer import anonymize

# Load calendar
with open('calendar.ics', 'rb') as f:
    cal = Calendar.from_ical(f.read())

# Anonymize
anonymized_cal = anonymize(cal)

# Save
with open('anonymized.ics', 'wb') as f:
    f.write(anonymized_cal.to_ical())
```

### Command Line

```bash
# Basic usage
icalendar-anonymize input.ics -o output.ics

# Shorter alias
ican input.ics -o output.ics

# Unix-style piping
cat calendar.ics | icalendar-anonymize > anonymized.ics

# Stdout by default
icalendar-anonymize calendar.ics
```

**Options:**
- `-i, --input FILE` - Input file (default: stdin)
- `-o, --output FILE` - Output file (default: stdout)
- `-v, --verbose` - Show processing details
- `--version` - Print version

### Web Service

```bash
# POST with ICS content
curl -X POST https://anonymizer.example.com/anonymize \
     -H "Content-Type: application/json" \
     -d '{"ics": "BEGIN:VCALENDAR..."}'

# Upload ICS file
curl -X POST https://anonymizer.example.com/upload \
     -F "file=@calendar.ics"

# Fetch and anonymize URL
curl "https://anonymizer.example.com/fetch?url=https://example.com/cal.ics"
```

FastAPI provides interactive docs at `/docs` for testing.

**Self-hosting:**

```bash
docker-compose up -d
```

Runs on port 8000 by default. Includes SSRF protection (blocks localhost and private IPs), 10-second timeout, and 10MB max file size.

## How It Works

**Hash-based anonymization** - Same input always produces the same output, preserving patterns for bug analysis.

**Structure preservation** - A 10-word summary stays 10 words. Emails still look like emails.

**What gets anonymized:**
- SUMMARY, DESCRIPTION, LOCATION
- ATTENDEE, ORGANIZER (including CN fields)
- COMMENT, CONTACT
- Unknown/X- properties (safe by default)

**What stays intact:**
- DTSTART, DTEND, DUE, DURATION, DTSTAMP
- RRULE, RDATE, EXDATE
- VTIMEZONE, TZID, TZOFFSETFROM, TZOFFSETTO
- UID (hashed but unique)
- SEQUENCE, STATUS, TRANSP, CLASS, PRIORITY
- CATEGORIES

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for development workflow, commit format, and testing requirements.

## License

AGPL-3.0-or-later. See [LICENSE](LICENSE).
