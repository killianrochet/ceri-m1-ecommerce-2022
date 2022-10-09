# TP - 02: Setup project

<br>

## 🎉 Create repository

<br>

Before to dive in, every member of your team must have a
[Github account](https://github.com/signup). At least the _SRE_
should have a valid Google account to interact with
[Google Cloud Platform](https://cloud.google.com). The SRE will
then create the dedicated Github repository for your project, by
forking this repository using the following link:

<br>

[![Fork me](https://badgen.net/badge/Github/Fork%20Me/?scale=2&icon=github)](https://github.com/Faylixe/ceri-m1-ecommerce-2022/fork)

<br>

Then add the other team's member as collaborator.

<br>

> :warning: forking the repository is very important as it will allow
~~_Jean Cloud Vinil_~~ me to visualize every projects.

<br>

### Setup the backend project

<br>

```bash
mkdir backend && cd backend
pip install --user poetry
poetry init
poetry add fastapi sqlmodel uvicorn
poetry add --dev pytest isort black mypy
```

Then open the created file `pyproject.toml` and add the following section to the end:

```toml
[tool.isort]
profile = "black"
multi_line_output = 3
```

### Setup the frontend project

> tbd

### Setup the SRE project

> tbd
