import streamlit as st

from streamlit_authenticator import Authenticate

from streamlit_option_menu import option_menu

lesDonneesDesComptes = {'usernames' : {'utilisateur' : {'name' : 'utilisateur',

       'password' : 'utilisateurMDP',

       'email' : 'utilisateur@gmail.com',

       'failed_login_attemps' : 0,

       'logged_in' : False,

       'role' : 'utilisateur'},
  
       'root' : {'name' : 'root',

       'password' : 'rootMDP',

       'email' : 'admin@gmail.com',

       'failed_login_attemps' : 0,

       'logged_in' : False,

       'role' : 'administrateur'}}}



authenticator = Authenticate(

     lesDonneesDesComptes,

     'cookie name',   # Le nom du cookie

     'cookie key', # La clé du cookie

      30  # Le nombre de jours avant que le cookie expire

)

authenticator.login()

def accueil() : 

    st.title("Bienvenue sur le contenu réservé aux utilisateurs connectés !")

if st.session_state["authentication_status"] : 

    accueil()

    authenticator.logout("Deconnexion")

elif st.session_state["authentication_status"] is False :

    st.error("L'username ou le password est/sont incorrect(s) !")

elif st.session_state["authentication_status"] is None : 

    st.warning("Les champs 'Username' et 'Password' doivent etre remplies !")

selection = option_menu(

         menu_title = None,

         options = ["Accueil", "Photos"]

)

if selection == "Accueil" :

    st.write("Bienvenue à la page d'accueil !")

elif selection == "Photos" : 

    st.write("Bienvenue sur mon album photo")


