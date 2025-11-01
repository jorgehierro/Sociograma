import pandas as pd
from utils import *

import streamlit as st

st.set_page_config(page_title="sociogramIA", page_icon="📊", layout="centered")

st.title("📊 sociogramIA")
st.write("Generador de sociogramas a partir de matrices")

uploaded_file = st.file_uploader(
    "📂 Arrastra o sube el archivo .csv (.xlsx estará disponible próximamente)",
    type=["csv"]
)

if not uploaded_file:
    print('Por favor, sube un archivo válido para continuar.')
else:
    with st.spinner("✍️ Generando el sociograma..."):

        df = pd.read_csv(uploaded_file, index_col=0)

        st.write("Primero, generamos los gráficos...")
        generar_graficos(df)

        st.write("\n Generados todos los gráficos.")

        st.write("Ahora, generamos el informe...")
        generar_informe()

        st.success("✅ Sociograma generado con éxito!")