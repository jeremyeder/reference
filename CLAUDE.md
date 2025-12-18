# Ambient Code Reference Repository - Agent Configuration

**Version**: 1.0.0
**Last Updated**: 2025-12-17
**Purpose**: Configuration for AI-assisted development in this repository

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Development Standards](#development-standards)
3. [Architecture Patterns](#architecture-patterns)
4. [Security Standards](#security-standards)
5. [Testing Strategy](#testing-strategy)
6. [CI/CD Workflow](#cicd-workflow)
7. [Documentation Guidelines](#documentation-guidelines)
8. [Git Workflow](#git-workflow)

---

## Project Overview

### Repository Purpose

This is a **GitHub template repository** demonstrating AI-assisted development best practices using the "buffet approach" - features work independently with no prescribed sequence.

**Key Principles**:
- ✅ **Buffet approach** - Features are standalone and independently adoptable
- ✅ **Working code** - Every pattern has a functioning example
- ✅ **Succinct documentation** - No AI slop, get to the point
- ✅ **Quality automation** - Comprehensive linting and testing
- ❌ **No Red Hat branding** - Pure "Ambient Code" documentation
- ❌ **No "Amber" terminology** - Use "Codebase Agent" or "CBA" only

### Technology Stack

- **Application**: FastAPI microservice (Python 3.11+)
- **Testing**: pytest with 80%+ coverage requirement
- **Linting**: black (no line length limits), isort, ruff
- **CI/CD**: GitHub Actions
- **Container**: Podman-compatible Containerfile

---

## Development Standards

### Python Version Support

Support Python versions N and N-1:
- Python 3.11 (primary)
- Python 3.12 (tested in CI matrix)

### Virtual Environment (MANDATORY)

**ALWAYS use virtual environments**:

```bash
# Create virtual environment
python3.11 -m venv .venv

# Activate
source .venv/bin/activate

# Verify
echo $VIRTUAL_ENV  # Should show project path
```

**Never modify system Python packages.**

### Package Management

**Use `uv` instead of `pip`**:

```bash
# Install dependencies
uv pip install -r requirements.txt

# Install dev dependencies
uv pip install -r requirements-dev.txt
```

### Code Quality Tools (MANDATORY)

**Pre-commit linting workflow**:

```bash
# 1. Format code (no line length enforcement)
black app/ tests/

# 2. Sort imports
isort app/ tests/

# 3. Lint code
ruff check app/ tests/

# 4. Run tests
pytest
```

**All commands must pass before committing.**

### Black Configuration

- **NO line length enforcement** - Do not enforce character limits
- **Double quotes** for strings
- **Trailing commas** in multi-line structures

### Isort Configuration

- **Profile**: black
- **Standard import grouping**: stdlib, third-party, local
- **One import per line** for clarity

### Ruff Configuration

- **Ignore E501** (line length)
- **All other PEP 8 rules** enforced
- **No unused imports or variables**

### Error Handling

- ❌ **NEVER push** if linters report errors
- ❌ **NEVER push** if tests fail
- ✅ **ALWAYS fix issues** immediately after running linters
- ✅ **Re-run linters** after fixes to verify resolution

---

## Architecture Patterns

### Layered Architecture

```
API Layer (FastAPI routes)
    ↓ Handles HTTP, validation, serialization
Service Layer (Business logic)
    ↓ Core business rules, orchestration
Model Layer (Pydantic validation)
    ↓ Data validation, serialization
Core Layer (Config, security, utilities)
    ↓ Cross-cutting concerns
```

### Component Responsibilities

**API Layer** (`app/api/`):
- FastAPI route handlers
- Request/response models (Pydantic)
- HTTP status codes
- Error responses
- OpenAPI documentation

**Service Layer** (`app/services/`):
- Business logic
- Data manipulation
- Transaction coordination
- No HTTP concerns

**Model Layer** (`app/models/`):
- Pydantic models
- Validation rules
- Type annotations
- Serialization

**Core Layer** (`app/core/`):
- Configuration (Pydantic Settings)
- Security utilities (sanitization, validation)
- Logging configuration
- Shared utilities

### Example Resource Pattern

For each resource (e.g., Items):

1. **Model**: `app/models/item.py`
   - ItemBase (shared fields)
   - ItemCreate (creation payload)
   - ItemUpdate (update payload)
   - Item (full object)

2. **Service**: `app/services/item_service.py`
   - `create_item()`
   - `get_item()`
   - `list_items()`
   - `update_item()`
   - `delete_item()`

3. **API**: `app/api/v1/items.py`
   - POST `/api/v1/items`
   - GET `/api/v1/items`
   - GET `/api/v1/items/{id}`
   - PATCH `/api/v1/items/{id}`
   - DELETE `/api/v1/items/{id}`

---

## Security Standards

### Input Validation (CRITICAL)

**Validate at API boundary only**:
- Use Pydantic models for all request payloads
- Validators in models, not in routes
- Trust internal code - only validate external input

### Sanitization

**Location**: `app/core/security.py`

**Functions**:
- `sanitize_string()` - Remove dangerous characters, trim whitespace
- `validate_slug()` - Ensure URL-safe slugs

**Usage**:
```python
from app.core.security import sanitize_string

# In Pydantic model validator
@field_validator("name")
def sanitize_name(cls, v: str) -> str:
    return sanitize_string(v)
```

### Secrets Management

- **Environment variables only** - Use `.env` files (in `.gitignore`)
- **Pydantic Settings** - Load configuration from environment
- **Never commit secrets** - `.env` files excluded from git
- **Container secrets** - Pass as environment variables at runtime

### OWASP Prevention

**Light touch** - Don't overrotate on security:

1. **SQL Injection** - Not applicable (in-memory storage in example)
2. **XSS** - Sanitize strings, encode output
3. **Command Injection** - Validate file paths, sanitize inputs
4. **Secrets Exposure** - Environment variables, never hardcode

### Container Security

```dockerfile
# Use minimal base image
FROM python:3.11-slim

# Run as non-root user
RUN useradd -m -u 1000 app
USER app

# Copy only necessary files
COPY --chown=app:app . /app
```

---

## Testing Strategy

### Test Structure

```
tests/
├── unit/              # Service layer, isolated
├── integration/       # API endpoints, full cycle
└── e2e/              # End-to-end workflows
```

### Unit Tests

**Purpose**: Test service layer in isolation

**Pattern**: Arrange-Act-Assert

```python
def test_create_item():
    # Arrange
    service = ItemService()
    data = ItemCreate(name="Test", slug="test")

    # Act
    result = service.create_item(data)

    # Assert
    assert result.name == "Test"
    assert result.slug == "test"
```

**Coverage**: Service logic, edge cases, error handling

### Integration Tests

**Purpose**: Test API endpoints with full request/response cycle

**Tool**: FastAPI TestClient

```python
def test_create_item_endpoint(client):
    response = client.post(
        "/api/v1/items",
        json={"name": "Test", "slug": "test"}
    )
    assert response.status_code == 201
    assert response.json()["name"] == "Test"
```

**Coverage**: HTTP layer, validation, status codes

### E2E Tests

**Purpose**: Test Codebase Agent workflows

**File**: `tests/e2e/test_cba_workflow.py`

**Status**: OUTLINE ONLY (requires GitHub API credentials)

**Workflow**:
1. Create GitHub issue
2. Trigger CBA (via label)
3. Wait for PR creation
4. Verify PR contents
5. Verify CI passes
6. Clean up

### Coverage Requirements

- **Minimum**: 80% overall (enforced in CI)
- **Critical paths**: 100% (business logic, security)
- **Configuration**: Excluded from coverage

### Fixtures

**Location**: `tests/conftest.py`

```python
@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture
def sample_item():
    return ItemCreate(name="Test", slug="test")
```

---

## CI/CD Workflow

### GitHub Actions

**Workflows**:

1. **`.github/workflows/ci.yml`** (Main CI)
   - Lint: black --check, isort --check, ruff check
   - Test: pytest with coverage (Python 3.11 + 3.12 matrix)
   - Build: podman build + health check test
   - Upload: coverage to Codecov

2. **`.github/workflows/security.yml`** (Security)
   - Bandit: Python static analysis
   - Safety: Dependency vulnerability scanning
   - Schedule: Weekly + on push/PR

3. **`.github/workflows/docs-validation.yml`** (Documentation)
   - Mermaid validation (all diagrams)
   - Markdownlint
   - Triggers: on docs/** changes

4. **`.github/workflows/cba-e2e.yml`** (E2E)
   - E2E tests for CBA workflow
   - Manual workflow_dispatch only
   - Requires: GITHUB_TOKEN

### Dependabot

**File**: `.github/dependabot.yml`

**Configuration**:
- **Schedule**: Weekly
- **Auto-label**: "dependencies", "security"
- **Package ecosystem**: pip

---

## Documentation Guidelines

### Writing Style

- **Succinct**: No AI slop, get to the point
- **Practical**: Focus on how to use, not theory
- **Code-heavy**: Show examples, not just descriptions
- **Quickstart-focused**: Help users get running fast

### Documentation Structure

**Core docs** (`docs/`):
1. `quickstart.md` - 5-minute setup guide
2. `architecture.md` - Layered architecture explanation
3. `tutorial.md` - Step-by-step feature building
4. `api-reference.md` - Complete API documentation

### Mermaid Diagrams (CRITICAL)

**User note**: "Mermaid diagrams always have errors"

**ALWAYS validate** before committing:

```bash
./scripts/validate-mermaid.sh
```

**CI enforcement**: Blocks merge if diagrams invalid

### ADR (Architecture Decision Records)

**Location**: `docs/adr/`

**Scaffolding only** - NO actual content:
- `README.md` - Explains ADR purpose
- `template.md` - Shows format (YYYYMMDD-title.md)

---

## Git Workflow

### Branch Strategy

**ALWAYS work in feature branches** unless explicitly told otherwise:

```bash
# Check current branch BEFORE any modifications
git branch --show-current

# Create feature branch
git checkout -b feature/descriptive-name
```

### Commit Workflow

**Pre-commit checklist**:
1. Run linters: `black . && isort . && ruff check .`
2. Run tests: `pytest`
3. Check git status: `git status`
4. Review changes: `git diff`

**Commit message style**:
```
Add feature for X

- Implement Y
- Update Z
```

Focus on "why" rather than "what".

### Pull Request Workflow

**Before creating PR**:
1. `git status` - check untracked files
2. `git diff` - review all changes
3. `git log` - review commit history
4. Ensure CI passes

**PR requirements**:
- [ ] All linters pass
- [ ] All tests pass (80%+ coverage)
- [ ] Security scans pass
- [ ] Mermaid diagrams validated
- [ ] Documentation updated

### Git Safety

**NEVER**:
- Update git config without permission
- Run destructive commands (hard reset, force push) without explicit request
- Skip hooks (--no-verify, --no-gpg-sign)
- Force push to main/master
- Commit secrets (.env files)

---

## Codebase Agent (CBA) Integration

### Agent Configuration

**Location**: `.claude/agents/codebase-agent.md`

**Terminology**: Use "Codebase Agent" or "CBA" - **NEVER "Amber"**

### Memory System

**Location**: `.claude/context/`

**Modular files**:
- `architecture.md` - Layered architecture patterns
- `security-standards.md` - Input validation, OWASP prevention
- `testing-patterns.md` - Arrange-Act-Assert, fixtures, mocking

### Agent Capabilities

1. **Issue-to-PR Automation** - Convert well-defined issues into PRs
2. **Code Reviews** - Provide actionable feedback
3. **Proactive Maintenance** - Dependency updates, linting, docs

### Autonomy Levels

- **Level 1 (Default)**: PR creation only - WAIT for human approval
- **Level 2 (Future)**: Auto-merge for low-risk changes (requires config)

---

## Quick Reference

### Setup Commands

```bash
./scripts/setup.sh
source .venv/bin/activate
uvicorn app.main:app --reload
```

### Linting Workflow

```bash
black app/ tests/
isort app/ tests/
ruff check app/ tests/
pytest
```

### Security Scans

```bash
bandit -r app/
safety check
```

### Validation

```bash
./scripts/validate-mermaid.sh
```

---

## Anti-Requirements

**NEVER include**:
- ❌ Red Hat branding
- ❌ "Amber" terminology
- ❌ Sequenced/linear adoption path
- ❌ Deployment infrastructure
- ❌ AI slop in documentation
- ❌ Security overrotation
- ❌ Mermaid syntax errors
- ❌ Actual ADR content
- ❌ Time estimates

---

**End of Configuration**

This CLAUDE.md file is the source of truth for all AI-assisted development in this repository. Follow these standards strictly.
