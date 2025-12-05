# SPDX-FileCopyrightText: 2025 icalendar-anonymizer contributors
# SPDX-License-Identifier: AGPL-3.0-or-later

# syntax=docker/dockerfile:1

FROM python:3.13-slim

LABEL org.opencontainers.image.title="icalendar-anonymizer"
LABEL org.opencontainers.image.description="Strip personal data from iCalendar files while preserving technical properties for bug reproduction"
LABEL org.opencontainers.image.url="https://github.com/mergecal/icalendar-anonymizer"
LABEL org.opencontainers.image.source="https://github.com/mergecal/icalendar-anonymizer"
LABEL org.opencontainers.image.licenses="AGPL-3.0-or-later"

# Install git for version detection
RUN apt-get update && apt-get install -y --no-install-recommends git && rm -rf /var/lib/apt/lists/*

WORKDIR /app
ENV PYTHONUNBUFFERED=true

# Copy project files including .git for version detection
COPY pyproject.toml README.md ./
COPY .git/ ./.git/
COPY src/ ./src/

# Install the package with all dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -e ".[all]"

# Expose port for web API (when implemented)
EXPOSE 8000

# TODO: Update CMD when web API is implemented
# For now, just print version and exit
CMD ["python", "-c", "from icalendar_anonymizer import version; print(f'icalendar-anonymizer {version}')"]
