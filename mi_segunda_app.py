import streamlit as st

# Funciones de conversión
def temperatura(conversion, valor):
    if conversion == "Celsius a Fahrenheit":
        return (valor * 9/5) + 32
    elif conversion == "Fahrenheit a Celsius":
        return (valor - 32) * 5/9
    elif conversion == "Celsius a Kelvin":
        return valor + 273.15
    elif conversion == "Kelvin a Celsius":
        return valor - 273.15

def longitud(conversion, valor):
    if conversion == "Pies a metros":
        return valor * 0.3048
    elif conversion == "Metros a pies":
        return valor / 0.3048
    elif conversion == "Pulgadas a centímetros":
        return valor * 2.54
    elif conversion == "Centímetros a pulgadas":
        return valor / 2.54

# Define más funciones de conversión para las otras categorías...

# Interfaz de usuario
st.title("Conversor Universal")

categoria = st.selectbox("Selecciona una categoría", [
    "Temperatura",
    "Longitud"
    # Agrega aquí las otras categorías...
])

if categoria == "Temperatura":
    conversion_temperatura = st.selectbox("Selecciona el tipo de conversión", [
        "Celsius a Fahrenheit",
        "Fahrenheit a Celsius",
        "Celsius a Kelvin",
        "Kelvin a Celsius"
    ])
    valor = st.number_input("Ingresa el valor a convertir")
    resultado = temperatura(conversion_temperatura, valor)
    st.write(f"El resultado es: {resultado}")

elif categoria == "Longitud":
    conversion_longitud = st.selectbox("Selecciona el tipo de conversión", [
        "Pies a metros",
        "Metros a pies",
        "Pulgadas a centímetros",
        "Centímetros a pulgadas"
    ])
    valor = st.number_input("Ingresa el valor a convertir")
    resultado = longitud(conversion_longitud, valor)
    st.write(f"El resultado es: {resultado}")

# Agrega más bloques de código para las otras categorías...
