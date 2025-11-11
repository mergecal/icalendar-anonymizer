# Contributing to icalendar-anonymizer

Thanks for contributing to icalendar-anonymizer.


## Getting Started

Fork and clone:

```bash
git clone https://github.com/YOUR-USERNAME/icalendar-anonymizer.git
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

Aim for 90%+ coverage. All tests must pass before merge.

CI runs tests on Python 3.9-3.12 across Ubuntu, Windows, and macOS. Coverage is tracked via Codecov.

### Code Quality

Check code style and auto-format:

```bash
ruff check .    # Check for linting errors
ruff format .   # Auto-format code
```

CI enforces the same Ruff version and checks.

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

### Pre-commit Hooks (Optional)

Enable to validate commits locally:

```bash
pre-commit install --hook-type commit-msg
```

CI validates all commits and PR titles regardless.

## Pull Request Process

- One approval required before merge
- All tests must pass
- Update `CHANGES.rst` with your changes
- Follow conventional commit format for PR title

## Documentation

Update `CHANGES.rst` for user-facing changes. See the file header for formatting guidelines.

Add docstrings to public APIs. We use Sphinx for documentation generation.

## Project Structure

- **Library**: Core anonymization in `src/icalendar_anonymizer/`
- **CLI**: Command-line interface (installed via `[cli]` extra)
- **Web**: FastAPI web service (installed via `[web]` extra)
- **Tests**: In `tests/`

## Release Process

Releases are handled by maintainers. GitHub Actions automatically publishes to PyPI and builds Docker images when tags are pushed.

## License

By contributing, you agree that your contributions will be licensed under AGPL-3.0-or-later.

## Questions

Open an issue for discussion before starting major changes.
