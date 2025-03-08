# notes on UV

## sources

- [Setting Up a Python Project in 2024: uv and vscode](https://blog.phle.dev/posts/python-setup-2024/index.html)
- [Using uv with Jupyter](https://docs.astral.sh/uv/guides/integration/jupyter/#using-jupyter-with-a-non-project-environment)

## random

Add dev packages:

```bash
uv add --dev ruff ipykernel pytest pytest-cov mypy
```

You can make dependency groups!
The name here is testgroup.

```bash
uv add --group testgroup polars
```