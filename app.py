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
    st.warning("Por favor, sube un archivo válido para continuar.")
    st.stop()

modo = st.radio(
    "¿Qué deseas generar?",
    ("Solo fotos", "Informe completo")
)

# --- Procesar según la opción ---
df = pd.read_csv(uploaded_file, index_col=0)

if modo == "Informe completo":
    with st.spinner("✍️ Generando el sociograma..."):
        st.write("Primero, generamos los gráficos...")
        generar_graficos(df)

        st.write("\n✅ Generados todos los gráficos.")

        st.write("Ahora, generamos el informe...")
        informe = generar_informe()

        st.success("✅ Sociograma generado con éxito!")

        st.download_button(
            label="📄 Descargar informe PDF",
            data=informe,
            file_name="Informe_Sociograma.pdf",
            mime="application/pdf"
        )

else:  # Solo fotos
    with st.spinner("🖼️ Generando las fotos..."):
        fotos = generar_graficos(df)

    st.success("✅ Fotos generadas con éxito!")

    # Si generar_fotos devuelve un ZIP o bytes
    st.download_button(
        label="📸 Descargar fotos",
        data=fotos,
        file_name="Fotos_Sociograma.zip",
        mime="application/zip"
    )