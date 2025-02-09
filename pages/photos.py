import streamlit as st

def run():
    st.title("Bienvenue sur mon album photo")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.header("A cat")
        st.image("https://static.streamlit.io/examples/cat.jpg")

    with col2:
        st.header("A dog")
        st.image("https://static.streamlit.io/examples/dog.jpg")

    with col3:
        st.header("An owl")
        st.image("https://static.streamlit.io/examples/owl.jpg")

# On va s'assurer que la page fonctionne si elle est executée directement
if __name__ == "__main__" : 
    
    run()


