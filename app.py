import streamlit as st

st.set_page_config(page_title="Ruta de Decisión Estadística", page_icon="📊")

# ---------------------------
# Función para recomendar prueba
# ---------------------------
def recomendar_prueba(tipo_variables, relacion, normalidad, grupos, independientes, ordinal):
    # t de Student independiente
    if tipo_variables == "Cuantitativa" and relacion == "Comparar dos grupos" and grupos == 2:
        if normales and independientes:
            return ("t de Student para muestras independientes",
                    "Se recomienda porque tienes dos grupos independientes, la variable es continua "
                    "y los datos cumplen normalidad.")
        else:
            return ("U de Mann-Whitney",
                    "Se usa porque compara dos grupos independientes cuando la variable es continua u ordinal "
                    "y no hay normalidad.")
    
    # t pareada
    if tipo_variables == "Cuantitativa" and relacion == "Comparar dos grupos" and grupos == 2 and not independientes:
        if normales:
            return ("t de Student para muestras relacionadas",
                    "Adecuada porque las mediciones están pareadas y las diferencias siguen una distribución normal.")
        else:
            return ("Wilcoxon",
                    "Es la alternativa no paramétrica para muestras relacionadas sin normalidad.")
    
    # ANOVA
    if tipo_variables == "Cuantitativa" and relacion == "Comparar tres o más grupos" and grupos >= 3:
        if normales and independientes:
            return ("ANOVA de un factor",
                    "Es útil para comparar las medias de tres o más grupos independientes con normalidad.")
        else:
            return ("Kruskal-Wallis",
                    "Se utiliza cuando los grupos son independientes pero los datos no son normales o son ordinales.")
    
    # Chi cuadrada
    if tipo_variables == "Categórica" and relacion == "Asociación":
        return ("Chi-cuadrada",
                "Se usa para determinar si hay relación entre dos variables categóricas.")

    # Correlaciones
    if relacion == "Relación entre dos variables":
        if tipo_variables == "Cuantitativa" and normales:
            return ("Correlación de Pearson",
                    "Adecuada porque ambas variables son continuas y la relación es lineal con normalidad.")
        else:
            return ("Correlación de Spearman",
                    "Se recomienda cuando la relación es monótona o las variables son ordinales o no normales.")
    
    # Regresión
    if relacion == "Predicción":
        return ("Regresión lineal simple",
                "Adecuada para modelar la relación lineal entre una variable dependiente continua "
                "y una independiente predictora.")

    return ("No se pudo determinar", "Las combinaciones no coinciden con una prueba estándar.")


# ---------------------------
# Interfaz
# ---------------------------

st.title("📊 Ruta de Decisión para Seleccionar Pruebas Estadísticas")
st.write("""
Esta herramienta te guiará paso a paso para determinar qué **prueba estadística** 
es adecuada para tu análisis, basándose en características de tus variables, 
tamaño de los grupos, normalidad y tipo de comparación.
""")

st.markdown("---")

st.header("1️⃣ Tipo de variables que estás analizando")
tipo_variables = st.selectbox(
    "Selecciona el tipo de variable dependiente:",
    ["Cuantitativa", "Categórica"]
)

st.header("2️⃣ ¿Qué deseas hacer?")
relacion = st.selectbox(
    "Selecciona el objetivo estadístico:",
    ["Comparar dos grupos", "Comparar tres o más grupos", 
     "Asociación", "Relación entre dos variables", "Predicción"]
)

grupos = 0
independientes = True
ordinal = False
normales = False

if relacion in ["Comparar dos grupos", "Comparar tres o más grupos"]:
    st.header("3️⃣ Número de grupos")
    grupos = st.number_input("¿Cuántos grupos compararás?", min_value=2, value=2)

    st.header("4️⃣ Tipo de diseño")
    indep = st.radio("¿Los grupos son independientes o relacionados?", ["Independientes", "Relacionados"])
    independientes = (indep == "Independientes")

    if tipo_variables == "Cuantitativa":
        st.header("5️⃣ Normalidad")
        norm = st.radio("¿Los datos cumplen normalidad?", ["Sí", "No"])
        normales = (norm == "Sí")
    
    st.header("6️⃣ Nivel de medición")
    ord = st.radio("La variable dependiente es:", ["Continua", "Ordinal"])
    ordinal = (ord == "Ordinal")

elif relacion == "Relación entre dos variables":
    st.header("3️⃣ Normalidad de ambas variables")
    norm = st.radio("¿Ambas variables son normales?", ["Sí", "No"])
    normales = (norm == "Sí")

elif relacion == "Asociación":
    st.info("Se detectó que las variables son categóricas. La prueba adecuada podría ser Chi-cuadrada.")

elif relacion == "Predicción":
    st.info("Este caso dirige hacia **Regresión lineal simple** si la variable dependiente es continua.")

st.markdown("---")

# Botón final para obtener la prueba
if st.button("📌 Obtener recomendación"):
    prueba, explicacion = recomendar_prueba(
        tipo_variables, relacion, normales, grupos, independientes, ordinal
    )

    st.success(f"### ✔ Prueba recomendada: **{prueba}**")
    st.write(f"**¿Por qué?** {explicacion}")
