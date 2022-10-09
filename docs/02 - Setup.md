# 02 - Configuration du project

<br>

## 🎉 Création du repository

<br>

Avant de rentrer dans le vif du sujet, chaque membre de l'équipe doit avoir un
[compte Github](https://github.com/signup). A minima, le _SRE_ de l'équipe doit
avoir un compte [Gmail](https://www.google.com/account/about/) afin de pouvoir
intéragir avec [Google Cloud Platform](https://cloud.google.com). Le _SRE_ doit
créer un repository [Github](https://github.com) dédié pour votre projet, en
forkant ce repository via le lien suivant:

<br>

[![Fork me](https://badgen.net/badge/Github/Fork%20Me/?scale=2&icon=github)](https://github.com/Faylixe/ceri-m1-ecommerce-2022/fork)

<br>

Ensuite, il devra ajouter les autres membres de l'équipe comme collaborateur sur
le repository crée.

<br>

> :warning: vous devez absolument forker le repositor your permettre à ~~_Jean Cloud Vinil_~~
votre enseignant de pouvoir suivre vos projets facilement. Tout manquement à cette régle
entrainera une pénalité à votre équipe, à savoir un point sur votre note.

<br>

## 🔨 Configuration des projets par stack

<br>

### Configuration du projet backend

<br>

Nous allons utiliser [poetry](https://www.python-poetry.org) pour gérer notre projet.
Pour cela vous pouvez utiliser les commandes suivantes à la racine de votre repository
pour configurer le projet:

<br>

```bash
mkdir backend
mkdir -p backend/src
mkdir -p backend/tests
cd backend
pip install --user poetry
poetry init
poetry add fastapi sqlmodel uvicorn
poetry add --dev pytest isort black mypy
```

<br>

Vous devez par la suite ouvrir le fichier `pyproject.toml` et ajouter la section suivante
à la fin du fichier:

<br>

```toml
[tool.isort]
profile = "black"
multi_line_output = 3
```

<br>

Voici la liste des dépendances qui ont été ajouté par l'étape précédente:

<br>

| Name     | Description                                          |
| -------  | ---------------------------------------------------- |
| FastAPI  | Framework for implementing REST API in modern python |
| SQLModel | ORM based on SQLAlchemy and Pydantic data validation |
| Uvicorn  | Process manager implementing the ASGI protocol       |
| pytest   | Unit test framework                                  |
| black    | Python source code linter                            |
| isort    | Python import statement linter                       |
| mypy     | Static type analysis                                 |

<br>

En attendant la tenue du meeting initiale avec votre client _Jean Cloud Vinil_,
vous pouvez commencer à lire la documentation de [FastAPI](https://fastapi.tiangolo.com)
et créer un premier squelette d'API avec un endpoint de test.

<br>

### Configuration du projet frontend

> tbd

### Configuration du projet SRE

> tbd
