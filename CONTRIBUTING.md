# 🤝 Contributing to Cosmos Engine

Thank you for your interest in contributing to **Cosmos Engine**! This document explains how we collaborate and keep the project clean and consistent.

---

## 🌟 Ways to Contribute

- 🪐 **Add datasets** — curated astronomical data with documentation
- 🔧 **Build tools** — Python utilities for astronomical calculations
- 🛰️ **Create simulations** — physics simulations (orbits, N-body, cosmology)
- 📊 **Make visualizations** — plots, star maps, interactive charts
- 📚 **Improve docs** — tutorials, explanations, catalog entries
- 🐛 **Fix bugs** — corrections and improvements

---

## 🔄 Workflow

1. **Pick or open an issue** describing what you'll work on
2. **Create a branch** from `main`:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Make your changes** following the style guidelines below
4. **Commit** with a clear, emoji-prefixed message:
   ```bash
   git commit -m "🪐 Add TESS light curve analysis tool"
   ```
5. **Push** and open a **Pull Request** against `main`
6. **Request review** from the other maintainer

---

## 👥 Maintainer Responsibilities

To keep work coordinated between maintainers:

| Maintainer | Primary Focus |
|------------|---------------|
| [@saheb-karami](https://github.com/saheb-karami) | Tools, simulations, core architecture |
| [@sabi-karami](https://github.com/sabi-karami) | Datasets, visualizations, documentation |

*These are starting points, not hard boundaries — feel free to work across areas!*

**Rules for maintainers:**
- Don't push directly to `main` for non-trivial changes — use PRs
- Every PR needs at least one review from the other maintainer
- Keep the `main` branch always working (code should run)

---

## 📝 Style Guidelines

### Python
- Follow **PEP 8**
- Use **type hints** for function arguments and return values
- Write **docstrings** for all public functions and classes
- Keep functions focused and testable
- Add a `if __name__ == '__main__':` demo block where it helps

### Commit Messages
Use emoji prefixes to categorize commits:

| Emoji | Meaning |
|-------|---------|
| 🪐 | New feature / data |
| 🔧 | Tool / utility |
| 📊 | Visualization |
| 📚 | Documentation |
| 🐛 | Bug fix |
| ♻️ | Refactor |
| 🧪 | Tests |

### File Organization
- Tools → `tools/`
- Simulations → `simulations/`
- Datasets → `datasets/`
- Notebooks → `notebooks/`
- Catalogs → `catalogs/`

---

## 🧪 Testing

Before opening a PR, make sure your code runs:

```bash
python tools/your_tool.py   # Should run without errors
```

---

## 💬 Questions?

Open an issue, or start a discussion. We're happy to help!

---

*Happy exploring! 🌌*
