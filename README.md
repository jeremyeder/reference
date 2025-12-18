# Ambient Code Reference Repository

A GitHub template demonstrating AI-assisted development best practices with a **buffet approach** - adopt features independently, no prescribed sequence.

## Quick Start

```bash
# Clone this repository
git clone https://github.com/jeremyeder/reference.git
cd reference

# Run one-command setup
./scripts/setup.sh

# Start the application
source .venv/bin/activate
uvicorn app.main:app --reload

# Visit the application
curl http://localhost:8000/health
```

## What's Included

This repository demonstrates:

- ✅ **Codebase Agent (CBA)** - AI agent for issue-to-PR automation, code reviews, and proactive maintenance
- ✅ **FastAPI Microservice** - Production-ready layered architecture with health endpoints
- ✅ **Comprehensive Testing** - Unit, integration, and E2E tests with 80%+ coverage
- ✅ **CI/CD Automation** - GitHub Actions for linting, testing, security scanning
- ✅ **Security Patterns** - Input validation, sanitization, secrets management
- ✅ **Documentation** - Quickstart, architecture, tutorials, API reference
- ✅ **Quality Automation** - Black, isort, ruff, Mermaid validation

## Buffet Approach

Pick what you need. Each feature works independently:

| Feature | Description | Adopt Independently |
|---------|-------------|---------------------|
| **Codebase Agent** | Issue-to-PR automation | ✅ Copy `.claude/` directory |
| **FastAPI App** | Layered architecture example | ✅ Use `app/` as template |
| **Testing** | Comprehensive test patterns | ✅ Copy test structure |
| **CI/CD** | GitHub Actions workflows | ✅ Copy `.github/workflows/` |
| **Documentation** | Docs structure | ✅ Copy `docs/` templates |

## Repository Structure

```
ambient-code-reference/
├── .claude/               # Codebase Agent configuration
│   ├── agents/           # CBA agent definition
│   └── context/          # Modular memory system
├── app/                  # FastAPI microservice
│   ├── api/             # API endpoints
│   ├── core/            # Config, security, logging
│   ├── models/          # Pydantic models
│   └── services/        # Business logic
├── tests/               # Comprehensive test suite
├── docs/                # Documentation
├── .github/workflows/   # CI/CD automation
└── scripts/             # Setup and validation scripts
```

## Features

### Codebase Agent (CBA)

The Codebase Agent combines best practices from Ambient Code for AI-assisted development:

- **Issue-to-PR Automation** - Convert well-defined issues into pull requests
- **Code Reviews** - Provide actionable feedback on PRs
- **Proactive Maintenance** - Dependency updates, linting fixes, documentation

See [`.claude/agents/codebase-agent.md`](.claude/agents/codebase-agent.md) for details.

### FastAPI Application

Production-ready microservice with:

- **Layered Architecture** - API, Service, Model, Core layers
- **Health Endpoints** - `/health`, `/readiness`, `/liveness`
- **CRUD Operations** - Complete Items resource example
- **Security** - Input validation, sanitization at API boundary
- **Structured Logging** - JSON format for observability

### Testing

- **Unit Tests** - Service layer isolation
- **Integration Tests** - Full API request/response cycles
- **E2E Tests** - CBA workflow automation (outline)
- **80%+ Coverage** - Enforced in CI

### CI/CD

GitHub Actions workflows:

- **Continuous Integration** - Lint, test, build on every push
- **Security Scanning** - Bandit, Safety for vulnerabilities
- **Documentation Validation** - Mermaid diagram syntax checking
- **Dependabot** - Automated dependency updates

## Documentation

- **[Quickstart](docs/quickstart.md)** - Get running in 5 minutes
- **[Architecture](docs/architecture.md)** - System design and patterns
- **[Tutorial](docs/tutorial.md)** - Build your first feature
- **[API Reference](docs/api-reference.md)** - Complete endpoint documentation

## Development

```bash
# Install dependencies
uv pip install -r requirements-dev.txt

# Run linters
black app/ tests/
isort app/ tests/
ruff check app/ tests/

# Run tests
pytest

# Security scans
bandit -r app/
safety check

# Validate Mermaid diagrams
./scripts/validate-mermaid.sh
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

MIT - See [LICENSE](LICENSE) for details.

---

**Use this template**: Click "Use this template" button to create your own repository with these patterns.
