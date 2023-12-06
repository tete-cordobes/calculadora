import streamlit as st

# URL del logo
logo_url = "https://yinyangseo.com/wp-content/uploads/2022/06/Recurso-26.png"

# Mostrar el logo en la parte superior de la aplicación
st.image(logo_url, width=150)

# Título de la aplicación
st.title('Calculadora YingYangSeo')

# Sidebar para las entradas de números
with st.sidebar:
    st.header("Entradas")
    num1 = st.selectbox('Introduce el primer número', range(1, 10))
    num2 = st.selectbox('Introduce el segundo número', range(1, 10))

    # Opciones para operaciones
    operation = st.selectbox('Elige una operación', ['Sumar', 'Restar', 'Multiplicar', 'Dividir'])

# Función para realizar las operaciones
def calculate(num1, num2, operation):
    if operation == 'Sumar':
        return num1 + num2
    elif operation == 'Restar':
        return num1 - num2
    elif operation == 'Multiplicar':
        return num1 * num2
    elif operation == 'Dividir':
        if num2 != 0:
            return num1 / num2
        else:
            return 'Error: División por cero'

# Mostrar el resultado
if st.button('Calcular'):
    result = calculate(num1, num2, operation)
    st.header('Resultado:')
    st.success(f'{result}')
