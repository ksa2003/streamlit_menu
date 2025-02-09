import streamlit as st
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu

# Données des comptes utilisateurs
lesDonneesDesComptes = {
    'usernames': {
        'utilisateur': {
            'name': 'Utilisateur',
            'password': 'MDP',
            'email': 'user@gmail.com',
            'failed_login_attemps': 0,
            'logged_in': False,
            'role': 'utilisateur'
        },
        'root': {
            'name': 'root',
            'password': '2357',
            'email': 'admin@gmail.com',
            'failed_login_attemps': 0,
            'logged_in': False,
            'role': 'administrateur'
        }
    }
}

# Authentification
authenticator = Authenticate(
    lesDonneesDesComptes,
    'cookie_name',   # Nom du cookie
    'cookie_key',    # Clé du cookie
    30               # Expiration du cookie (jours)
)

authenticator.login()

# Si l'utilisateur est authentifié, on affiche le menu
if st.session_state["authentication_status"]:
    
    # Afficher le menu uniquement si l'utilisateur est connecté
    selection = option_menu(
        menu_title=None,
        options=["Accueil", "Photos"]
    )

    if selection == "Accueil":
        st.title("Bienvenue à la page d'accueil !")
    
    elif selection == "Photos":
        import pages.photos
        pages.photos.run()

    # Ajouter un bouton de déconnexion
    authenticator.logout("Déconnexion")

elif st.session_state["authentication_status"] is False:
    st.error("Le nom d'utilisateur et/ou le mot de passe est/sont incorrect(s) ! Pour vous connecter, vous pouvez saisir 'Utilisateur' à 'Username' et 'MDP' à 'Password'.")

elif st.session_state["authentication_status"] is None:
    st.warning("Veuillez saisir un nom d'utilisateur et un mot de passe pour vous connecter.")
