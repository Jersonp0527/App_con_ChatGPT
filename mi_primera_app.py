import streamlit as st

# Título y autor
st.title("Mi primera app")
st.text("Esta app fue elaborada por Jerson Pemberthy Castaño")

# Preguntar el nombre al usuario
nombre_usuario = st.text_input("Por favor, ingresa tu nombre")

# Imprimir mensaje de bienvenida
if nombre_usuario:
    st.write(f"{nombre_usuario}, te doy la bienvenida a mi primera app.")
