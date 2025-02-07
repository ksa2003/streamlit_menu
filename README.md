## Description

Cette application Streamlit est une interface de connexion avec authentification utilisant `streamlit_authenticator`, ainsi qu'un menu de navigation basé sur `streamlit_option_menu`. Une fois connecté, l'utilisateur peut accéder à un contenu réservé et naviguer entre la page d'accueil et la galerie photo.

## Installation

Avant d'exécuter l'application, assurez-vous d'avoir installé les dépendances nécessaires :

```sh
pip install streamlit streamlit-authenticator streamlit-option-menu
```

## Utilisation

Exécutez l'application avec la commande suivante :

```sh
streamlit run app.py
```

## Fonctionnalités

- **Authentification des utilisateurs** : Utilisation du module `streamlit_authenticator` pour gérer les connexions.
- **Gestion des rôles** : Différenciation entre utilisateurs et administrateurs.
- **Menu de navigation** : Un menu permettant de basculer entre "Accueil" et "Photos".
- **Gestion des erreurs de connexion** : Messages d'avertissement en cas d'erreur d'authentification.

## Structure du Code

```python
import streamlit as st
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu

# Base de données des utilisateurs
lesDonneesDesComptes = {
    'usernames': {
        'utilisateur': {
            'name': 'utilisateur',
            'password': 'utilisateurMDP',
            'email': 'utilisateur@gmail.com',
            'failed_login_attemps': 0,
            'logged_in': False,
            'role': 'utilisateur'
        },
        'root': {
            'name': 'root',
            'password': 'rootMDP',
            'email': 'admin@gmail.com',
            'failed_login_attemps': 0,
            'logged_in': False,
            'role': 'administrateur'
        }
    }
}

# Initialisation de l'authentification
authenticator = Authenticate(
    lesDonneesDesComptes,
    'cookie name',   # Le nom du cookie
    'cookie key',    # La clé du cookie
    30               # Expiration en jours
)

# Connexion de l'utilisateur
authenticator.login()

def accueil():
    st.title("Bienvenue sur le contenu réservé aux utilisateurs connectés !")

# Gestion des sessions utilisateur
if st.session_state["authentication_status"]:
    accueil()
    authenticator.logout("Deconnexion")
elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect(s) !")
elif st.session_state["authentication_status"] is None:
    st.warning("Les champs 'Username' et 'Password' doivent être remplis !")

# Menu de navigation
selection = option_menu(
    menu_title=None,
    options=["Accueil", "Photos"]
)

if selection == "Accueil":
    st.write("Bienvenue à la page d'accueil !")
elif selection == "Photos":
    st.write("Bienvenue sur mon album photo")
```

## Améliorations possibles

- Ajouter une gestion des sessions plus sécurisée avec hachage des mots de passe.
- Intégrer une base de données pour stocker les utilisateurs.
- Ajouter une gestion des rôles plus avancée pour limiter l'accès à certaines pages.

## Auteurs

- **Nom de l'Auteur** - Créateur du projet

## Licence

Ce projet est sous licence libre. Vous pouvez le modifier et le redistribuer selon vos besoins.


