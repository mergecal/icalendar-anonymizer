<!--- SPDX-FileCopyrightText: 2025 icalendar-anonymizer contributors -->
<!--- SPDX-License-Identifier: AGPL-3.0-or-later -->

# Contributing to icalendar-anonymizer

Quick reference for contributors. For a detailed guide with CHANGES.rst formatting and more, see the [Contributing Guide on Read the Docs](https://icalendar-anonymizer.readthedocs.io/stable/contributing.html).


## Getting Started

Fork and clone:

```bash
git clone https://github.com/mergecal/icalendar-anonymizer.git
cd icalendar-anonymizer
```

Install development dependencies:

```bash
pip install -e ".[dev]"
```

This includes pytest, ruff, pre-commit, and commitizen. For building docs, use `pip install -e ".[doc]"`.

## Development Workflow

1. Create a feature branch from `main`
2. Make changes with tests
3. Run tests and linting locally
4. Commit following conventional commits format
5. Push and open a pull request

### Running Tests

```bash
pytest
```

90% minimum coverage required. PRs fail if coverage drops. All tests must pass before merge.

CI runs tests on Python 3.11-3.13 across Ubuntu, Windows, and macOS. Coverage is tracked via Codecov.

### Code Quality with Ruff

We use [Ruff](https://docs.astral.sh/ruff/) for linting and code formatting (100-character line length).

**Manual formatting**:

```bash
ruff check .     # Check for linting errors
ruff check . --fix  # Auto-fix linting errors
ruff format .    # Auto-format code
```

**Configuration**: Ruff settings are in `pyproject.toml` under `[tool.ruff]`.

**CI enforcement**: CI runs the same Ruff version (>=0.14.0) to ensure consistency.

## Commit Message Format

We use [Conventional Commits](https://www.conventionalcommits.org/). See [docs/contribute/commit-format.rst](docs/contribute/commit-format.rst) for full details.

Format: `type(scope): subject`

**Types**: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`, `ci`, `perf`, `build`, `style`, `revert`

**Examples**:
```
feat(cli): add --output flag for file writing
fix(api): prevent SSRF in URL fetching
docs: update installation instructions
```

**PR titles** must follow the same format. We use squash merge, so the PR title becomes the commit message on `main`.

### Pre-commit Hooks (Optional but Recommended)

Pre-commit hooks catch issues before committing, providing faster feedback than waiting for CI.

**Setup** (one-time after cloning):

```bash
pre-commit install              # Install pre-commit hooks
pre-commit install --hook-type commit-msg  # Install commit message validation
```

**What runs on every commit**:

- **Ruff linting** (`ruff check --fix`) - Auto-fixes linting errors
- **Ruff formatting** (`ruff format`) - Auto-formats Python code
- **REUSE compliance** (`reuse lint`) - Validates SPDX license headers
- **Trailing whitespace** - Removes trailing spaces (preserves Markdown line breaks)
- **End-of-file fixer** - Ensures files end with exactly one newline
- **YAML validation** - Checks YAML syntax
- **JSON validation** - Checks JSON syntax
- **TOML validation** - Checks pyproject.toml syntax
- **Python AST check** - Verifies Python files parse as valid syntax
- **Case conflict check** - Detects filenames that differ only in case
- **Merge conflict detection** - Prevents committing merge markers
- **Large file prevention** - Blocks files >1MB
- **Line ending normalization** - Enforces LF line endings
- **Debug statement detection** - Catches forgotten `breakpoint()` or `pdb`
- **Commit message validation** - Enforces conventional commits format

**Performance**: All checks complete in under 5 seconds.

**Skipping hooks** (use sparingly for WIP commits):

```bash
git commit --no-verify
```

**Running manually** (without committing):

```bash
pre-commit run --all-files     # Run all hooks on all files
pre-commit run ruff --all-files  # Run specific hook
```

**Updating hook versions**:

```bash
pre-commit autoupdate
```

**Note**: Pre-commit is optional for contributors. CI enforces the same checks regardless. Core maintainers should use it.

## Pull Request Process

- One approval required before merge
- All tests must pass
- Update `CHANGES.rst` with your changes
- Follow conventional commit format for PR title

## Code Style Guidelines

### Docstrings

Use Google-style docstrings with multi-line format:

```python
def function(arg1: str, arg2: int) -> str:
    """Brief description on first line.

    More detailed explanation if needed. Can span multiple paragraphs.

    Args:
        arg1: Description of first argument
        arg2: Description of second argument

    Returns:
        Description of return value

    Raises:
        ValueError: When invalid input provided
    """
```

Don't include Examples sections unless they contain real, testable doctests.

### Test Organization

Use `pytest.mark.parametrize` for duplicate test patterns:

```python
@pytest.mark.parametrize(
    ("property_name", "expected_value"),
    [
        ("status", "CONFIRMED"),
        ("priority", 1),
    ],
)
def test_preserves_metadata(property_name, expected_value):
    """Test implementation."""
```

Organize tests into logical groups with clear section comments.

### Imports

Standard imports at top, group by: standard library, third-party, local. Sort alphabetically within groups.

## Documentation

Update `CHANGES.rst` for user-facing changes.

**Formatting guidelines**: The formatting guidelines in `CHANGES.rst` are commented out (lines 8-43) so they don't appear in the rendered documentation. Contributors should read the [source file](CHANGES.rst) directly to see the full formatting guidelines.

Add docstrings to public APIs. We use Sphinx for documentation generation.

## Project Structure

```
icalendar-anonymizer/
├── src/
│   └── icalendar_anonymizer/
│       ├── __init__.py
│       ├── version.py           # Version interface
│       ├── _version.py          # Auto-generated by hatch-vcs
│       ├── anonymizer.py        # Core library
│       ├── cli.py               # CLI (via [cli] extra)
│       ├── webapp/              # Web service (via [web] extra)
│       └── tests/               # Tests included in package
│           ├── lib/             # Library tests
│           ├── cli/             # CLI tests
│           └── web/             # Web service tests
├── docs/                        # Sphinx documentation
└── pyproject.toml               # Build system: hatchling
```

**Build system**: Uses hatchling with hatch-vcs for automatic version management.

**Code style**: 100-character line length enforced by Ruff.

## Licensing and REUSE Compliance

This project follows the [REUSE specification](https://reuse.software/) for clear licensing. All files must include SPDX headers:

```python
# SPDX-FileCopyrightText: 2025 icalendar-anonymizer contributors
# SPDX-License-Identifier: AGPL-3.0-or-later
```

For different file types:
- **Python/YAML/TOML**: Use `#` comments
- **RST files**: Use `.. SPDX-FileCopyrightText:` format
- **Markdown**: Use `<!--- SPDX-FileCopyrightText: -->` format

Pre-commit hooks automatically check REUSE compliance via `reuse lint`. You can also run it manually:

```bash
reuse lint
```

## Release Process

Releases are handled by maintainers. GitHub Actions automatically publishes to PyPI and builds Docker images when tags are pushed.

## License

By contributing, you agree that your contributions will be licensed under AGPL-3.0-or-later.

## Questions

Open an issue for discussion before starting major changes.
