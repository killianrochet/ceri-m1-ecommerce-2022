# 01: Welcome aboard !

<br>

> Bonjour à tous ! Je m'appelle _Jean Cloud Vinil_, propriétaire d'une boutique d'achat
> neuf et occasion de disque vinyle de tout genre musicaux ! Comme beaucoup, mon activité
> a été grandement impactée par la crise sanitaire et mon entourage m'a fortement conseillé
> d'ouvrir une boutique en ligne afin d'augmenter ma visibilité et surtout, mon chiffre
> d'affaire.

<br>

<p align="center">
    <img src="https://media4.giphy.com/media/z9lZMI5UDdI08/giphy.gif?cid=ecf05e47e5vqzwqu9sn3q84ho241j3dx1ltfww3yttnr85oh&rid=giphy.gif&ct=g">
</p>
<p align="center">
    <em>Grosse démonstration de soft skills, par Jean Cloud Vinil</em>
</p>

## Constitution des équipes

<br>

Dans cette simulation incroyablement réaliste, vous allez représenter une agence de service
numérique en charge de mettre en oeuvre la boutique en ligne de notre cher ami _Jean Cloud_.
Votre équipe doit être constitué de 3 personnes, afin d'assurer les rôles suivants:

<br>

| Rôle                      | Responsabilités                                                       |
| ------------------------- | --------------------------------------------------------------------- |
| Backend engineer          | Database schema design, backend implementation and testing            |
| Frontend engineer         | Web application implementation and testing                            |
| Site reliability engineer | Manage infrastructure, continous integration and deployment processes |

<br>

### ✨ Vous êtes Backend engineer

<br>

Votre rôle est de developper l'intégralité de la partie backend du projet, selon
les axes suivants:

<br>

- Définir et faire évoluer un schéma de base de donnée.
- Définir en collaboration avec le Frontend engineer, différentes APIs.
- Implémenter et tester les différents APIs.

<br>

Les différentes APIs seront mises en oeuvre en [Python](https://www.python.org),
via le framework [FastAPI](https://fastapi.tiangolo.com) et l'ORM
[SQLModel](https://sqlmodel.tiangolo.com). Le stockage des données sera réalisés sur la base de donnée relationnelle [MySQL](https://www.mysql.com), et les mises à jour de schéma seront réalisées via l'outil de gestion de migration de votre choix<sup>1</sup>.

<br>

> <sup>1</sup> Le choix de l'outil de migration doit être fait en accord avec le SRE de votre
> équipe, qui le mettra en oeuvre dans la partie delivery.

<br>

### 🎨 Vous êtes Frontend engineer

<br>

Votre rôle est de developper l'intégralité de la partie frontend du projet, selon
les axes suivants:

<br>

- Définir l'identité visuelle de la marque de _Jean Cloud_ et la mettre en oeuvre.
- Définir et faire évoluer les différentes vues de l'application web.
- Implémenter et tester l'application web.

<br>

L'application web devra être conçu avec le framework [VueJS](https://vuejs.org),
avec un approche la plus modulaire possible en terme de vues et de composants.
L'état de l'application sera maintenu via l'évolution de _VueX_:
[Pinia](https://pinia.vuejs.org).

<br>

### 🔧 Vous êtes Site reliability engineer

<br>

Votre rôle couvrira différents aspects liées au SRE, incluant:

- Définir et implémenter les différents process d'intégration continue.
- Définir et implémenter un process de continuous delivery.
- Définir et implémenter les resources d'infrastructure.
- Etre garant de la qualité globale du projet.

<br>

Le projet sera déployé sur [Google Cloud Platform](https://cloud.google.com), et maintenu
via l'outil de configuration as code [Terraform](https://www.terraform.io).
