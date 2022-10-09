# TP - 01: Welcome aboard !
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

### Vous êtes Backend engineer

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
[SQLModel](https://sqlmodel.tiangolo.com). Le stocakge des données sera réalisé sur la base de donnée relationnelle [MySQL](https://www.mysql.com), et les mises à jour de schéma seront réalisées via l'outil de gestion de migration de votre choix<sup>1</sup>.

<br>

> <sup>1</sup> Le choix de l'outil de migration doit être fait en accord avec le SRE de votre
> équipe, qui le mettra en oeuvre dans la partie delivery.

<br>

### Vous êtes Frontend engineer

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

### Vous êtes Site reliability engineer

<br>

- Définir et implémenter les différentes process d'intégration continue.
- Définir et implémenter les différentes process de delivery.
- Définir et implémenter les resources d'infrastructure.
- Etre garant de la qualité globale du projet.
