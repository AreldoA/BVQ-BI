import streamlit as st
st.title("Bolsa de Valores Quito BI")
st.sidebar.title("Parámetros")
st.write("Elaborado por: Alex Apolo")
archivo = st.file_uploader("Cargue su archivo")
 

if archivo is not None:

  tabla = pd.read_csv(archivo)

  st.write(tabla)
