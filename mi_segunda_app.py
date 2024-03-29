"""
Este escript permite egecutar una app de conversión de unidades
a través de la plataforma streamlit.
"""
import streamlit as st

"""
FUNCIONES DE CONVERSIÓN.
Cada función de conversión, utiliza la misma estructura
El valor en la unidad original es multiplicado por
el correspondiente factor de conversión para al final retornar
el respectivo resultado.

Args:
    tipo (str): El tipo de conversión deseado.
    valor (float): El valor que se va a convertir.

Returns:
    float: El resultado de la conversión.
"""

# Funciones de conversión para temperatura
def temperatura(conversion, valor):
    if conversion == "Celsius a Fahrenheit":
        return (valor * 9 / 5) + 32
    elif conversion == "Fahrenheit a Celsius":
        return (valor - 32) * 5 / 9
    elif conversion == "Celsius a Kelvin":
        return valor + 273.15
    elif conversion == "Kelvin a Celsius":
        return valor - 273.15

# Funciones de conversión para longitud
def longitud(conversion, valor):
    if conversion == "Pies a metros":
        return valor * 0.3048
    elif conversion == "Metros a pies":
        return valor / 0.3048
    elif conversion == "Pulgadas a centímetros":
        return valor * 2.54
    elif conversion == "Centímetros a pulgadas":
        return valor / 2.54

# Funciones de conversión para peso/masa
def peso_masa(conversion, valor):
    if conversion == "Libras a kilogramos":
        return valor * 0.453592
    elif conversion == "Kilogramos a libras":
        return valor / 0.453592
    elif conversion == "Onzas a gramos":
        return valor * 28.3495
    elif conversion == "Gramos a onzas":
        return valor / 28.3495

# Funciones de conversión para volumen
def volumen(conversion, valor):
    if conversion == "Galones a litros":
        return valor * 3.78541
    elif conversion == "Litros a galones":
        return valor / 3.78541
    elif conversion == "Pulgadas cúbicas a centímetros cúbicos":
        return valor * 16.3871
    elif conversion == "Centímetros cúbicos a pulgadas cúbicas":
        return valor / 16.3871

# Funciones de conversión para tiempo
def tiempo(conversion, valor):
    if conversion == "Horas a minutos":
        return valor * 60
    elif conversion == "Minutos a segundos":
        return valor * 60
    elif conversion == "Días a horas":
        return valor * 24
    elif conversion == "Semanas a días":
        return valor * 7

# Funciones de conversión para velocidad
def velocidad(conversion, valor):
    if conversion == "Millas por hora a kilómetros por hora":
        return valor * 1.60934
    elif conversion == "Kilómetros por hora a metros por segundo":
        return valor * 0.277778
    elif conversion == "Nudos a millas por hora":
        return valor * 1.15078
    elif conversion == "Metros por segundo a pies por segundo":
        return valor * 3.28084

# Funciones de conversión para área
def area(conversion, valor):
    if conversion == "Metros cuadrados a pies cuadrados":
        return valor * 10.7639
    elif conversion == "Pies cuadrados a metros cuadrados":
        return valor / 10.7639
    elif conversion == "Kilómetros cuadrados a millas cuadradas":
        return valor * 0.386102
    elif conversion == "Millas cuadradas a kilómetros cuadrados":
        return valor / 0.386102

# Funciones de conversión para energía
def energia(conversion, valor):
    if conversion == "Julios a calorías":
        return valor * 0.239006
    elif conversion == "Calorías a kilojulios":
        return valor * 0.001
    elif conversion == "Kilovatios-hora a megajulios":
        return valor * 3.6
    elif conversion == "Megajulios a kilovatios-hora":
        return valor / 3.6

# Funciones de conversión para presión
def presion(conversion, valor):
    if conversion == "Pascales a atmósferas":
        return valor * 0.00000986923
    elif conversion == "Atmósferas a pascales":
        return valor * 101325
    elif conversion == "Barras a libras por pulgada cuadrada":
        return valor * 14.5038
    elif conversion == "Libras por pulgada cuadrada a bares":
        return valor / 14.5038

# Funciones de conversión para tamaño de datos
def tamano_datos(conversion, valor):
    if conversion == "Megabytes a gigabytes":
        return valor * 0.001
    elif conversion == "Gigabytes a terabytes":
        return valor * 0.001
    elif conversion == "Kilobytes a megabytes":
        return valor * 0.001
    elif conversion == "Terabytes a petabytes":
        return valor * 0.001

# INTERFAZ DE USUARIO
# Se instancia un objeto title de la clase st
st.title("Conversor Universal")

# Variable que almacena la selección del objeto selectbox de la clase st
categoria = st.selectbox(
    "Selecciona una categoría",
    [
        "Temperatura",
        "Longitud",
        "Peso/Masa",
        "Volumen",
        "Tiempo",
        "Velocidad",
        "Área",
        "Energía",
        "Presión",
        "Tamaño de datos",
    ],
)

"""
SELECCIÓN DE CATEGORIA

Para cada clase o categoria de conversión se hace lo siguiente

1. Se comprueba el valor seleccionado en la textbox para así 
instanciar la función de conversión adecuada
2. Se crea un nuevo objeto selectbox del a clase st, este para
seleccionar el tipo de conversión
3. Se pide que se ingrese el valor a convertir en un nuevo objeto
number_input de la clase st
4. Se almacena el resultado de la conversión invocando la respectiva
finción
5. Se escribe el resultado en un objeto write de la clase st
"""

if categoria == "Temperatura":
    conversion_temperatura = st.selectbox(
        "Selecciona el tipo de conversión",
        [
            "Celsius a Fahrenheit",
            "Fahrenheit a Celsius",
            "Celsius a Kelvin",
            "Kelvin a Celsius",
        ],
    )
    valor = st.number_input("Ingresa el valor a convertir")
    resultado = temperatura(conversion_temperatura, valor)
    st.write(f"El resultado es: {resultado}")

elif categoria == "Longitud":
    conversion_longitud = st.selectbox(
        "Selecciona el tipo de conversión",
        [
            "Pies a metros",
            "Metros a pies",
            "Pulgadas a centímetros",
            "Centímetros a pulgadas",
        ],
    )
    valor = st.number_input("Ingresa el valor a convertir")
    resultado = longitud(conversion_longitud, valor)
    st.write(f"El resultado es: {resultado}")

elif categoria == "Peso/Masa":
    conversion_peso = st.selectbox(
        "Selecciona el tipo de conversión",
        [
            "Libras a kilogramos",
            "Kilogramos a libras",
            "Onzas a gramos",
            "Gramos a onzas",
        ],
    )
    valor = st.number_input("Ingresa el valor a convertir")
    resultado = peso_masa(conversion_peso, valor)
    st.write(f"El resultado es: {resultado}")

elif categoria == "Volumen":
    conversion_volumen = st.selectbox(
        "Selecciona el tipo de conversión",
        [
            "Galones a litros",
            "Litros a galones",
            "Pulgadas cúbicas a centímetros cúbicos",
            "Centímetros cúbicos a pulgadas cúbicas",
        ],
    )
    valor = st.number_input("Ingresa el valor a convertir")
    resultado = volumen(conversion_volumen, valor)
    st.write(f"El resultado es: {resultado}")

elif categoria == "Tiempo":
    conversion_tiempo = st.selectbox(
        "Selecciona el tipo de conversión",
        ["Horas a minutos", "Minutos a segundos", "Días a horas", "Semanas a días"],
    )
    valor = st.number_input("Ingresa el valor a convertir")
    resultado = tiempo(conversion_tiempo, valor)
    st.write(f"El resultado es: {resultado}")

elif categoria == "Velocidad":
    conversion_velocidad = st.selectbox(
        "Selecciona el tipo de conversión",
        [
            "Millas por hora a kilómetros por hora",
            "Kilómetros por hora a metros por segundo",
            "Nudos a millas por hora",
            "Metros por segundo a pies por segundo",
        ],
    )
    valor = st.number_input("Ingresa el valor a convertir")
    resultado = velocidad(conversion_velocidad, valor)
    st.write(f"El resultado es: {resultado}")

elif categoria == "Área":
    conversion_area = st.selectbox(
        "Selecciona el tipo de conversión",
        [
            "Metros cuadrados a pies cuadrados",
            "Pies cuadrados a metros cuadrados",
            "Kilómetros cuadrados a millas cuadradas",
            "Millas cuadradas a kilómetros cuadrados",
        ],
    )
    valor = st.number_input("Ingresa el valor a convertir")
    resultado = area(conversion_area, valor)
    st.write(f"El resultado es: {resultado}")

elif categoria == "Energía":
    conversion_energia = st.selectbox(
        "Selecciona el tipo de conversión",
        [
            "Julios a calorías",
            "Calorías a kilojulios",
            "Kilovatios-hora a megajulios",
            "Megajulios a kilovatios-hora",
        ],
    )
    valor = st.number_input("Ingresa el valor a convertir")
    resultado = energia(conversion_energia, valor)
    st.write(f"El resultado es: {resultado}")

elif categoria == "Presión":
    conversion_presion = st.selectbox(
        "Selecciona el tipo de conversión",
        [
            "Pascales a atmósferas",
            "Atmósferas a pascales",
            "Barras a libras por pulgada cuadrada",
            "Libras por pulgada cuadrada a bares",
        ],
    )
    valor = st.number_input("Ingresa el valor a convertir")
    resultado = presion(conversion_presion, valor)
    st.write(f"El resultado es: {resultado}")

elif categoria == "Tamaño de datos":
    conversion_datos = st.selectbox(
        "Selecciona el tipo de conversión",
        [
            "Megabytes a gigabytes",
            "Gigabytes a terabytes",
            "Kilobytes a megabytes",
            "Terabytes a petabytes",
        ],
    )
    valor = st.number_input("Ingresa el valor a convertir")
    resultado = tamano_datos(conversion_datos, valor)
    st.write(f"El resultado es: {resultado}")
