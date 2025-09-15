# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Commands

This project uses `uv` for dependency management and `invoke` for task automation.

### Setup
```bash
# Install dependencies
uv sync --all-groups
```

### Testing
```bash
# Run fast tests (excluding @pytest.mark.slow)
uv run invoke test

# Run all tests including slow ones
uv run invoke test.all

# Run tests with coverage report
uv run invoke test.coverage

# Run specific test file
uv run pytest tests/test_god_slayer_factory.py
```

### Linting and Code Quality
```bash
# Fast linting (xenon, ruff, bandit, dodgy, flake8, pydocstyle)
uv run invoke lint

# Deep linting (mypy, pylint, semgrep) - slower but comprehensive
uv run invoke lint.deep

# Format code with docformatter and ruff
uv run invoke style

# Check formatting without making changes
uv run invoke style --check
```

### Build and Distribution
```bash
# Build source and wheel packages
uv run invoke dist

# Clean build artifacts
uv run invoke clean
```

## Project Architecture

**God Slayer** is a Python library that provides a generator to read "Kami CSV" files - malformed CSV files with headers, footers, and intermediate rows that go beyond standard CSV format.

### Core Components

- **`GodSlayerFactory`** (`godslayer/god_slayer_factory.py`): Factory class that creates configured GodSlayer instances with header/footer/partition patterns
- **`GodSlayer`** (`godslayer/csv/god_slayer.py`): Main iterator class that reads CSV files while skipping unwanted rows
- **`ReaderOperatorFactory`** (`godslayer/reader_operator_factory.py`): Creates appropriate reader operators based on configuration
- **Reader Operators** (`godslayer/csv/reader_operators/`): Strategy pattern implementations for different CSV reading behaviors
- **String Matching** (`godslayer/list_string_matcher.py`): Pattern matching logic for identifying header/footer/partition rows using regex

### Key Design Patterns

The library uses:
- **Factory Pattern**: `GodSlayerFactory` creates pre-configured instances
- **Strategy Pattern**: Different reader operators for various CSV reading behaviors
- **Iterator Pattern**: `GodSlayer` implements iterator protocol for memory-efficient row-by-row processing
- **Context Manager**: Automatic file handling with proper cleanup

### Configuration Parameters

- `header`: Optional list of strings/regex patterns to identify and skip header rows
- `partition`: Optional list of strings/regex patterns to skip partition/grouping rows
- `footer`: Optional list of strings/regex patterns to stop before footer rows
- `encoding`: File encoding (default: "utf-8")

## Code Style and Quality

The project maintains high code quality standards:
- **Line length**: 119 characters (Black/Ruff compatible)
- **Import style**: Single-line imports only (following OpenStack hacking H301)
- **Type hints**: Full mypy strict mode compliance
- **Documentation**: Google-style docstrings with minimum 7 characters
- **Security**: Bandit security linting
- **Complexity**: Radon complexity analysis with B-grade minimum

## Testing Strategy

- Tests located in `tests/` directory
- Uses pytest with resource path plugin
- Slow tests marked with `@pytest.mark.slow`
- Coverage reporting with exclusions for TYPE_CHECKING blocks and NotImplementedError
- Test matrix covers Python 3.7-3.13