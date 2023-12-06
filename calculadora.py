
import streamlit as st

# Título de la aplicación
st.title('Calculadora Básica')

# Entradas para los números
num1 = st.number_input('Introduce el primer número', format='%f')
num2 = st.number_input('Introduce el segundo número', format='%f')

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
    st.success(f'El resultado es: {result}')
