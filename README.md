# Application Web d’échange de compétences

## Description

Ce projet est une application web développée avec le framework Django.
Elle permet à des utilisateurs d’échanger des compétences afin de s’entraider pour réaliser différentes activités.

Un utilisateur peut :

* afficher ses compétences

* créer une demande d’aide pour une activité 

* consulter les demandes correspondant à ses compétences

* se proposer pour aider un autre utilisateur

Le système permet ainsi de mettre en relation des personnes souhaitant échanger des compétences.

## Fonctionnalités

### Visiteur (non connecté)

Un visiteur peut :

* consulter la liste des compétences disponibles

* voir les prochains créneaux d’aide programmés

Les utilisateurs impliqués dans ces créneaux ne sont pas affichés.

## Utilisateur connecté

Un utilisateur connecté peut :

* définir les **compétences qu’il possède**
* créer une **demande d’aide**
* consulter les **demandes correspondant à ses compétences**
* se proposer pour **aider un autre utilisateur**
* consulter **ses propres demandes d’aide**

Lorsqu’une aide est acceptée, les utilisateurs peuvent se contacter via leur **adresse email**.

## Technologies utilisées

* Python
* Django
* HTML
* CSS
* Bootstrap

## Structure du projet
```
app/
    admin.py
    apps.py
    models.py
    views.py
    urls.py
    forms.py
    tests.py
    migrations/
    templates/
        app/
            home.html
            skills.html
            create_request.html
            my_skills.html
            request_available.html
            my_requests.html
mysite/
templates/
    base.html
    registration/
        login.html

manage.py
```

## Modèles de données

L’application repose sur plusieurs modèles :

* **Skill** : représente une compétence
* **Profil** : profil utilisateur contenant les compétences
* **RequestHelp** : demande d’aide pour une activité
* **OfferHelp** : proposition d’aide d’un utilisateur

## Installation du projet

### 1. Cloner le projet

```
git clone <url_du_projet>
cd projet_echang_competences
```

### 2. Créer un environnement virtuel

```
python -m venv venv
```

### 3. Activer l’environnement

```
venv\Scripts\activate
```

### 4. Installer Django

```
pip install Django==5.2.12
```
## Configuration de la base de données

Appliquer les migrations :

```
python manage.py makemigrations
python manage.py migrate
```
Créer un administrateur :

```
python manage.py createsuperuser
```

## Lancer le serveur

```
python manage.py runserver
```
Puis ouvrir dans le navigateur :

```
http://127.0.0.1:8000/app/
```

## Interface d'administration

L’administration est accessible via :

```
http://127.0.0.1:8000/admin/
```
Elle permet de gérer :

* les utilisateurs
* les compétences
* les demandes d’aide
* les propositions d’aide

