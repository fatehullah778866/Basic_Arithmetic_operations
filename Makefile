# Makefile for Advanced Arithmetic Calculator
# Provides convenient commands for development and testing

.PHONY: help run demo test clean install format lint check

# Default target
help:
	@echo "🧮 Advanced Arithmetic Calculator - Available Commands:"
	@echo ""
	@echo "  make run     - Run the interactive calculator"
	@echo "  make demo    - Run the calculator in demo mode"
	@echo "  make test    - Run the test suite"
	@echo "  make clean   - Clean up temporary files"
	@echo "  make install - Install development dependencies"
	@echo "  make format  - Format code with black"
	@echo "  make lint    - Run linting with flake8"
	@echo "  make check   - Run type checking with mypy"
	@echo "  make all     - Run format, lint, and test"
	@echo ""

# Run the interactive calculator
run:
	@echo "🚀 Starting interactive calculator..."
	python3 basic_python_arithmetic_operations.py

# Run the calculator in demo mode
demo:
	@echo "🎯 Running calculator demo..."
	python3 basic_python_arithmetic_operations.py --demo

# Run the test suite
test:
	@echo "🧪 Running test suite..."
	python3 test_calculator.py

# Clean up temporary files
clean:
	@echo "🧹 Cleaning up temporary files..."
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.pyd" -delete
	find . -type f -name ".coverage" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -exec rm -rf {} +
	find . -type d -name ".mypy_cache" -exec rm -rf {} +
	@echo "✅ Cleanup completed!"

# Install development dependencies (optional)
install:
	@echo "📦 Installing development dependencies..."
	@echo "Note: This project uses only built-in Python modules."
	@echo "Optional development tools can be installed with:"
	@echo "  pip install black flake8 mypy pytest pytest-cov"
	@echo "Or uncomment the relevant lines in requirements.txt"

# Format code with black (requires black to be installed)
format:
	@echo "🎨 Formatting code with black..."
	@if command -v black >/dev/null 2>&1; then \
		black *.py; \
		echo "✅ Code formatting completed!"; \
	else \
		echo "❌ Black not found. Install with: pip install black"; \
		exit 1; \
	fi

# Run linting with flake8 (requires flake8 to be installed)
lint:
	@echo "🔍 Running linting with flake8..."
	@if command -v flake8 >/dev/null 2>&1; then \
		flake8 *.py --max-line-length=88 --ignore=E203,W503; \
		echo "✅ Linting completed!"; \
	else \
		echo "❌ Flake8 not found. Install with: pip install flake8"; \
		exit 1; \
	fi

# Run type checking with mypy (requires mypy to be installed)
check:
	@echo "🔍 Running type checking with mypy..."
	@if command -v mypy >/dev/null 2>&1; then \
		mypy *.py --ignore-missing-imports; \
		echo "✅ Type checking completed!"; \
	else \
		echo "❌ MyPy not found. Install with: pip install mypy"; \
		exit 1; \
	fi

# Run all quality checks
all: format lint test
	@echo "🎉 All quality checks completed!"

# Check Python version
check-python:
	@echo "🐍 Checking Python version..."
	@python3 --version
	@python3 -c "import sys; assert sys.version_info >= (3, 8), 'Python 3.8+ required'"
	@echo "✅ Python version check passed!"

# Create a simple development environment setup
setup-dev:
	@echo "🔧 Setting up development environment..."
	@echo "1. Creating virtual environment..."
	python3 -m venv venv
	@echo "2. Activate virtual environment with:"
	@echo "   source venv/bin/activate  # On Linux/Mac"
	@echo "   venv\\Scripts\\activate     # On Windows"
	@echo "3. Install optional dev tools:"
	@echo "   pip install black flake8 mypy pytest pytest-cov"
	@echo "✅ Development environment setup instructions provided!"

# Show project information
info:
	@echo "📋 Project Information:"
	@echo "  Name: Advanced Arithmetic Calculator"
	@echo "  Python Version: 3.8+"
	@echo "  Dependencies: None (uses built-in modules only)"
	@echo "  Main File: basic_python_arithmetic_operations.py"
	@echo "  Test File: test_calculator.py"
	@echo ""
	@echo "📁 Files:"
	@ls -la *.py *.txt *.md Makefile 2>/dev/null || echo "No files found"