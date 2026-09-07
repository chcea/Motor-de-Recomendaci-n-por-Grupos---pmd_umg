"""
Motor de Recomendación por Grupos (Amigos en Común)
Interfaz gráfica con Streamlit

Para correrlo:
    1. pip install streamlit
    2. streamlit run app_streamlit.py
"""

import streamlit as st
import pandas as pd

# ---------------------------------------------------------
# 1. DATOS: usuarios representados como conjuntos de intereses
# ---------------------------------------------------------
# (Los mismos del script base - podés reemplazarlos por los de tu grupo)

if "usuarios" not in st.session_state:
    st.session_state.usuarios = {
        "Ana":    {"música", "fútbol", "cine", "lectura"},
        "Luis":   {"fútbol", "videojuegos", "cine", "programación"},
        "Marta":  {"música", "pintura", "lectura", "viajar"},
        "Carlos": {"programación", "videojuegos", "fútbol", "gaming"},
        "Sofía":  {"lectura", "música", "viajar", "cocina"},
    }

usuarios = st.session_state.usuarios


# ---------------------------------------------------------
# 2. OPERACIONES DE CONJUNTOS (mismas del script base)
# ---------------------------------------------------------

def interseccion(a: set, b: set) -> set:
    return a & b


def union_conjuntos(a: set, b: set) -> set:
    return a | b


def diferencia(a: set, b: set) -> set:
    return a - b


def calcular_afinidad(usuarios: dict) -> list:
    resultados = []
    nombres = list(usuarios.keys())
    for i in range(len(nombres)):
        for j in range(i + 1, len(nombres)):
            a, b = nombres[i], nombres[j]
            comunes = interseccion(usuarios[a], usuarios[b])
            resultados.append({
                "Persona A": a,
                "Persona B": b,
                "Afinidad": len(comunes),
                "Intereses en común": ", ".join(sorted(comunes)) if comunes else "—",
            })
    resultados.sort(key=lambda x: x["Afinidad"], reverse=True)
    return resultados


# ---------------------------------------------------------
# 3. INTERFAZ
# ---------------------------------------------------------

st.set_page_config(page_title="Motor de Recomendación", page_icon="🔗", layout="centered")
st.title("🔗 Motor de Recomendación por Grupos")
st.caption("Amigos en común - basado en Teoría de Conjuntos")

# --- Sección: agregar/editar usuarios ---
with st.expander("➕ Agregar o editar un usuario"):
    nombre = st.text_input("Nombre del usuario")
    intereses_texto = st.text_input("Intereses (separados por coma)", placeholder="música, fútbol, cine")
    if st.button("Guardar usuario"):
        if nombre and intereses_texto:
            nuevos_intereses = {i.strip().lower() for i in intereses_texto.split(",") if i.strip()}
            st.session_state.usuarios[nombre] = nuevos_intereses
            st.success(f"Usuario '{nombre}' guardado con {len(nuevos_intereses)} interés(es).")
            st.rerun()
        else:
            st.warning("Completa el nombre y al menos un interés.")

# --- Sección: mostrar usuarios actuales ---
st.subheader("👥 Usuarios registrados")
for nombre, intereses in usuarios.items():
    st.write(f"**{nombre}**: {', '.join(sorted(intereses))}")

# --- Sección: ranking de afinidad (recomendaciones) ---
st.subheader("🏆 Ranking de afinidad (amigos en común)")
if len(usuarios) >= 2:
    tabla = calcular_afinidad(usuarios)
    st.dataframe(pd.DataFrame(tabla), use_container_width=True, hide_index=True)
else:
    st.info("Agrega al menos 2 usuarios para ver el ranking.")

# --- Sección: comparar dos usuarios específicos ---
st.subheader("🔍 Comparar dos usuarios")
if len(usuarios) >= 2:
    col1, col2 = st.columns(2)
    with col1:
        persona_a = st.selectbox("Usuario A", list(usuarios.keys()), key="a")
    with col2:
        persona_b = st.selectbox("Usuario B", list(usuarios.keys()), index=1, key="b")

    if persona_a != persona_b:
        conjunto_a = usuarios[persona_a]
        conjunto_b = usuarios[persona_b]

        st.markdown(f"**Intersección (en común):** {interseccion(conjunto_a, conjunto_b) or '—'}")
        st.markdown(f"**Unión (todos combinados):** {union_conjuntos(conjunto_a, conjunto_b)}")
        st.markdown(f"**{persona_a} → {persona_b} (sugerencias para {persona_a}):** "
                    f"{diferencia(conjunto_b, conjunto_a) or '—'}")
        st.markdown(f"**{persona_b} → {persona_a} (sugerencias para {persona_b}):** "
                    f"{diferencia(conjunto_a, conjunto_b) or '—'}")
    else:
        st.warning("Selecciona dos usuarios diferentes para comparar.")
