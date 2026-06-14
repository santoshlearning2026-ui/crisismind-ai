# Contributing to CRISISMIND AI

Thank you for your interest in contributing! This document provides guidelines and instructions for contributing.

## Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Focus on the issue, not the person
- Help others learn and grow

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/your-username/crisismind-ai.git`
3. Create a virtual environment: `python -m venv venv`
4. Activate it: `source venv/bin/activate`
5. Install dependencies: `pip install -r backend/requirements.txt`
6. Create a branch: `git checkout -b feature/your-feature-name`

## Development Workflow

### Branch Naming
- `feature/description` - New features
- `bugfix/description` - Bug fixes
- `docs/description` - Documentation
- `refactor/description` - Code refactoring

### Commit Messages

Use clear, descriptive commit messages:

```
[TYPE] Short description

Detailed explanation of the change. Include:
- What changed and why
- Any breaking changes
- Related issue numbers (#123)
```

Types: `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `chore`

### Code Quality Standards

**Python:**
- Follow PEP 8
- Use type hints for all functions
- Docstrings for all modules, classes, and functions
- Max line length: 100 characters
- Use black for formatting
- Use pylint for linting
- Use mypy for type checking

**TypeScript/React:**
- Follow ESLint rules
- Use Prettier for formatting
- Component names in PascalCase
- File names in kebab-case
- Props interfaces end with `Props`

### Testing Requirements

- Write tests for new features
- Maintain 80%+ code coverage
- Unit tests for business logic
- Integration tests for API endpoints
- Update tests when fixing bugs

Run tests:
```bash
cd backend
pytest --cov=app
```

### Before Submitting a Pull Request

1. **Format code:**
   ```bash
   make format
   ```

2. **Run linters:**
   ```bash
   make lint
   ```

3. **Run type checking:**
   ```bash
   make type-check
   ```

4. **Run tests:**
   ```bash
   make test
   ```

5. **Update documentation** if needed

6. **Ensure all checks pass** before pushing

## Pull Request Process

1. Update README.md with any new features or changes
2. Add/update tests as needed
3. Use descriptive PR title: `[TYPE] Description`
4. Fill out the PR template completely
5. Link related issues with `Closes #123`
6. Request review from maintainers
7. Address feedback promptly
8. Ensure CI/CD passes

### PR Title Examples
- `[feat] Add weather API integration`
- `[fix] Fix risk calculation bug`
- `[docs] Update deployment guide`
- `[refactor] Improve agent architecture`

## Issues

### Reporting Bugs

Include:
- Clear description of the issue
- Steps to reproduce
- Expected behavior
- Actual behavior
- Environment details
- Error logs/screenshots

### Suggesting Features

Include:
- Clear description of the feature
- Use case and motivation
- Possible implementation approach
- Additional context

## Documentation

- Update docs for new features
- Keep README.md current
- Add docstrings to code
- Update API documentation
- Include examples for complex features

## Review Process

1. Automated checks run (linting, tests, coverage)
2. At least 1 maintainer review required
3. Feedback addressed and implemented
4. Final approval and merge

## Development Environment Setup

### Backend

```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install -r requirements-dev.txt
pre-commit install
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

### Database

```bash
# Start PostgreSQL
docker-compose up -d postgres

# Run migrations
cd backend
alembic upgrade head
```

## Common Tasks

### Adding a New API Endpoint

1. Create schema in `app/api/v1/schemas/`
2. Create endpoint in `app/api/v1/endpoints/`
3. Add tests in `tests/api/`
4. Update API documentation
5. Test with curl or Postman

### Adding a New Database Model

1. Define in `app/models/database/`
2. Create migration: `alembic revision --autogenerate -m "description"`
3. Update tests
4. Add service layer if needed

### Adding a New ML Model

1. Create in `app/models/ml/`
2. Add training notebook in `notebooks/`
3. Save model to `models/`
4. Add service wrapper
5. Create tests

## Performance Considerations

- Profile before optimizing
- Use database indexes appropriately
- Cache expensive computations
- Batch database queries
- Monitor API response times
- Test with realistic data volumes

## Security Guidelines

- Never commit secrets or API keys
- Use environment variables for config
- Validate all user inputs
- Sanitize data before storing
- Use parameterized queries
- Follow OWASP guidelines

## Getting Help

- Check existing issues/PRs
- Read documentation in `/docs`
- Ask on GitHub Discussions
- Open an issue with your question
- Review code examples

## Recognition

Contributors will be recognized in:
- CONTRIBUTORS.md
- GitHub contributors page
- Release notes

## License

By contributing, you agree your contributions will be licensed under MIT License.

---

Thank you for contributing to CRISISMIND AI!
