# AgentReady Features Inventory

This document catalogs all capabilities discovered in the `agentready` repository and related Ambient Code concepts. Use this to decide what to demonstrate in the reference implementation.

## Table of Contents

1. [Bootstrap Command Features](#bootstrap-command-features)
2. [CLI Commands](#cli-commands)
3. [Assessment Attributes (25 Total)](#assessment-attributes-25-total)
4. [Templates & Infrastructure](#templates--infrastructure)
5. [Other Ambient Code Repositories](#other-ambient-code-repositories)
6. [Key Concepts to Demonstrate](#key-concepts-to-demonstrate)

---

## Bootstrap Command Features

The `bootstrap` command (`agentready bootstrap`) generates GitHub infrastructure and best practices files:

### Generated Files

1. **GitHub Actions Workflows** (`.github/workflows/`)
   - `agentready-assessment.yml` - Automated assessment on PRs/pushes
   - `tests.yml` - Language-specific test workflows (Python/JavaScript/Go)
   - `security.yml` - Security scanning workflows
   - `repomix-update.yml` - Automated Repomix context updates

2. **GitHub Templates** (`.github/`)
   - `ISSUE_TEMPLATE/bug_report.md` - Bug report template
   - `ISSUE_TEMPLATE/feature_request.md` - Feature request template
   - `PULL_REQUEST_TEMPLATE.md` - PR template
   - `CODEOWNERS` - Code ownership rules

3. **Pre-commit Configuration**
   - `.pre-commit-config.yaml` - Language-specific hooks (black, isort, ruff for Python; prettier, eslint for JS; gofmt, golangci-lint for Go)

4. **Dependabot Configuration**
   - `.github/dependabot.yml` - Automated dependency updates

5. **Documentation Files**
   - `CONTRIBUTING.md` - Contributing guidelines (language-specific)
   - `CODE_OF_CONDUCT.md` - Code of conduct (Red Hat standard)

### Language Support

- **Python** (default fallback)
- **JavaScript**
- **Go**
- **Auto-detection** - Detects primary language from repository

### Command Options

- `--dry-run` - Preview changes without creating files
- `--language` - Specify language (python/javascript/go/auto)

---

## CLI Commands

### Core Assessment Commands

1. **`agentready assess`** - Main assessment command
   - Evaluates repository against 25 attributes
   - Generates HTML, Markdown, and JSON reports
   - Supports custom configuration files
   - Excludes specific attributes
   - Custom output directories

2. **`agentready bootstrap`** - Repository infrastructure setup
   - See [Bootstrap Command Features](#bootstrap-command-features)

3. **`agentready align`** - Automated remediation
   - Runs assessment
   - Identifies failing attributes
   - Automatically generates and applies fixes
   - Interactive mode for selective fixes
   - Dry-run mode

4. **`agentready repomix-generate`** - AI-friendly repository context
   - Generates single-file repository context for LLMs
   - Supports markdown, XML, JSON, plain formats
   - `--init` flag to create configuration
   - `--check` flag to verify freshness
   - Integrates with Repomix tool

### Research & Documentation Commands

5. **`agentready research`** - Research report management
   - `research validate` - Validate research report
   - `research init` - Generate new research report
   - `research add-attribute` - Add attribute to report
   - `research bump-version` - Update version
   - `research format` - Format research report

6. **`agentready research-version`** - Show bundled research version

7. **`agentready generate-config`** - Generate example configuration

### Learning & Skill Extraction

8. **`agentready learn`** - Extract reusable patterns as Claude Code skills
   - Analyzes assessment results
   - Identifies high-scoring patterns (≥70% confidence)
   - Generates SKILL.md files
   - Creates GitHub issue templates
   - LLM-powered enrichment (optional)
   - Multiple output formats (json, skill_md, github_issues, markdown, all)

9. **`agentready extract-skills`** - Alias for `learn` command

### Benchmarking & Evaluation

10. **`agentready benchmark`** - Agent coding benchmarks
    - Terminal-Bench evaluation (89 tasks)
    - Supports smoketest and full subsets
    - Multiple models (claude-haiku-4-5, claude-sonnet-4-5)
    - Harbor CLI integration

11. **`agentready validate-assessor`** - Validate assessor implementation

12. **`agentready eval-harness`** - Evaluation harness commands
    - `baseline` - Generate baseline measurements
    - `show-baseline` - Display baseline
    - `test-assessor` - Test individual assessor
    - `run-tier` - Run assessments by tier
    - `summarize` - Generate summary
    - `dashboard` - Create evaluation dashboard

### Batch & Experiment Commands

13. **`agentready assess-batch`** - Batch repository assessment
    - Assess multiple repositories
    - Generates aggregated reports (SQLite, CSV, JSON, HTML)
    - Comparison tables
    - Progress tracking

14. **`agentready experiment`** - SWE-bench experiment commands
    - `run-agent` - Run agent on SWE-bench
    - `evaluate` - Evaluate predictions
    - `compare` - Compare experiment results
    - `analyze` - Analyze correlation and generate heatmap

### Harbor Integration

15. **`agentready harbor`** - Harbor CLI integration
    - `compare` - Compare assessor impact
    - `list` - List comparisons
    - `view` - View comparison results

### Submission & Demo

16. **`agentready submit`** - Submit to leaderboard
    - Creates PR to agentready/agentready
    - Requires GITHUB_TOKEN
    - Validates repository access
    - Dry-run mode

17. **`agentready demo`** - Create demo repository
    - Generates sample repository
    - Runs assessment
    - Opens HTML report in browser
    - Supports Python, JavaScript, Go

### Schema & Validation

18. **`agentready validate-report`** - Validate assessment report schema

19. **`agentready migrate-report`** - Migrate reports between schema versions

---

## Assessment Attributes (25 Total)

### Tier 1: Essential (50% weight, 6 attributes)

1. **`claude_md_file`** (10% weight) - CLAUDE.md Configuration Files
   - Most important attribute
   - Binary pass/fail (exists or not)
   - Must be >50 bytes

2. **`readme_file`** - README.md Quality
   - Structure, completeness, examples

3. **`type_annotations`** - Type Annotations
   - Python: type hints
   - JavaScript: TypeScript or JSDoc
   - Go: native types

4. **`standard_layout`** - Standard Repository Layout
   - Language-specific conventions

5. **`dependency_pinning`** - Dependency Lock Files
   - requirements.txt.lock, package-lock.json, go.sum, etc.

6. **`dependency_security`** - Dependency Security Scanning
   - Automated security checks

### Tier 2: Critical (30% weight, 10 attributes)

7. **`test_coverage`** - Test Coverage
   - Minimum thresholds
   - Coverage reports

8. **`pre_commit_hooks`** - Pre-commit Hooks
   - Automated checks before commit

9. **`conventional_commits`** - Conventional Commits
   - Commit message format

10. **`gitignore_file`** - .gitignore File
    - Proper ignore patterns

11. **`one_command_setup`** - One-Command Setup
    - Easy development environment setup

12. **`file_size_limits`** - File Size Limits
    - Reasonable file sizes for AI context

13. **`separation_of_concerns`** - Separation of Concerns
    - Code organization

14. **`concise_documentation`** - Concise Documentation
    - Documentation length and clarity

15. **`inline_documentation`** - Inline Documentation
    - Docstrings, comments

16. **`cyclomatic_complexity`** - Cyclomatic Complexity
    - Code complexity metrics

### Tier 3: Important (15% weight, 7 attributes)

17. **`architecture_decisions`** - Architecture Decision Records (ADRs)
    - ADR files present

18. **`issue_pr_templates`** - Issue/PR Templates
    - GitHub templates

19. **`cicd_pipeline_visibility`** - CI/CD Pipeline Visibility
    - Public CI/CD status

20. **`semantic_naming`** - Semantic Naming Conventions
    - Clear, descriptive names

21. **`structured_logging`** - Structured Logging
    - JSON logs, structured formats

22. **`openapi_specs`** - OpenAPI/Swagger Specs
    - API documentation

### Tier 4: Advanced (5% weight, 3 attributes)

23. **`branch_protection`** - Branch Protection Rules
    - GitHub branch protection

24. **`code_smells`** - Code Smell Detection
    - Anti-pattern detection

25. **`container_setup`** - Container Setup
    - Dockerfile/Containerfile (conditional)

---

## Templates & Infrastructure

### Bootstrap Templates

Located in `src/agentready/templates/bootstrap/`:

- **Base templates** (`_base/`)
  - `precommit.yaml.j2`
  - `workflows/security.yml.j2`
  - `workflows/tests.yml.j2`

- **Language-specific templates**
  - `python/` - Python-specific workflows and pre-commit
  - `javascript/` - JavaScript-specific workflows and pre-commit
  - `go/` - Go-specific workflows and pre-commit

- **GitHub templates**
  - `issue_templates/bug_report.md.j2`
  - `issue_templates/feature_request.md.j2`
  - `PULL_REQUEST_TEMPLATE.md.j2`
  - `CODEOWNERS.j2`

- **Documentation templates**
  - `CONTRIBUTING.md.j2`
  - `CODE_OF_CONDUCT.md.j2`

- **Configuration templates**
  - `dependabot.yml.j2`

- **Workflow templates**
  - `workflows/agentready-assessment.yml.j2`
  - `workflows/repomix-update.yml.j2`

### Report Templates

- HTML report template (Jinja2)
- Markdown report template
- JSON schema (versioned)

---

## Other Ambient Code Repositories

From GitHub API, the `ambient-code` organization includes:

1. **agentready** - Main repository (this one)
2. **mcp-atlassian** - MCP server for Atlassian integration
3. **platform** - Platform repository
4. **workflows** - Workflows repository
5. **mobile** - Mobile-related repository
6. **.github** - Organization-level GitHub configuration

*Note: Full exploration of these repositories would require cloning and examining each one.*

---

## Key Concepts to Demonstrate

### 1. Evidence-Based Assessment
- 25 attributes derived from 50+ research citations
- Tier-based weighting system
- Research report versioning

### 2. AI-Assisted Development Readiness
- CLAUDE.md files for project-specific AI configuration
- Context window optimization
- File size limits
- Concise documentation

### 3. Automated Infrastructure
- Bootstrap command for one-time setup
- GitHub Actions workflows
- Pre-commit hooks
- Dependabot configuration

### 4. Continuous Improvement Loop
- Assessment → Identify gaps → Align fixes → Re-assess
- Learning loop: Extract skills from high-scoring repos
- Skill extraction and reuse

### 5. Multi-Format Reporting
- HTML (interactive, filterable)
- Markdown (git-diffable, version-controlled)
- JSON (machine-readable, API-friendly)

### 6. Language-Agnostic Design
- Supports Python, JavaScript, Go
- Auto-detection
- Language-specific templates

### 7. Research Foundation
- Bundled research report
- Versioned schema
- Evidence citations

### 8. Community & Leaderboard
- Submit assessments
- Public leaderboard
- Comparison and benchmarking

---

## Next Steps

1. **Decide scope**: Which features/concepts to demonstrate?
2. **Choose language**: Python, JavaScript, Go, or multi-language?
3. **Determine depth**: 
   - Minimal (just bootstrap output)?
   - Exemplary (high-scoring repository)?
   - Comprehensive (all features)?
4. **Plan structure**: How to organize the reference implementation?

