import contextlib
import io
import streamlit as st
from ALVA_40_problemas_CORREGIDO import resolver_problema

st.set_page_config(
    page_title="ALVA | Asistente Matemático Técnico",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Estilo visual de la aplicación
st.markdown("""
<style>
:root { --alva-navy: #172554; --alva-purple: #6d5dfc; --alva-cyan: #38bdf8; }
.stApp { background: linear-gradient(135deg, #f7f8ff 0%, #eef7ff 55%, #f7f2ff 100%); }
[data-testid="stHeader"] { background: rgba(0,0,0,0); }
.block-container { padding-top: 1.7rem; padding-bottom: 3rem; max-width: 1180px; }
.alva-hero {
  background: linear-gradient(120deg, #172554 0%, #4338ca 58%, #0e7490 100%);
  padding: 2rem 2.2rem; border-radius: 24px; color: white;
  box-shadow: 0 14px 35px rgba(37, 49, 120, .18); margin-bottom: 1.3rem;
}
.alva-kicker { color: #bae6fd; font-size: .82rem; letter-spacing: .16em; font-weight: 800; text-transform: uppercase; }
.alva-title { color: white; font-size: 2.8rem; line-height: 1.05; font-weight: 850; margin: .35rem 0 .5rem 0; }
.alva-subtitle { color: #e0e7ff; font-size: 1.05rem; margin: 0; }
.info-card { background: white; border: 1px solid #e2e8f0; border-radius: 18px; padding: 1rem 1.15rem; box-shadow: 0 5px 18px rgba(30, 41, 59, .05); min-height: 105px; }
.info-label { color: #64748b; font-size: .82rem; font-weight: 700; }
.info-value { color: #172554; font-size: 1.75rem; font-weight: 850; margin-top: .18rem; }
.section-title { color: #172554; font-weight: 800; font-size: 1.25rem; margin: .35rem 0 .4rem 0; }
.result-card { background: white; border: 1px solid #dbeafe; border-left: 6px solid #6d5dfc; border-radius: 18px; padding: 1.15rem 1.25rem; }
.small-muted { color: #64748b; font-size: .9rem; }
.stButton > button { border: 0; border-radius: 12px; background: linear-gradient(90deg, #5b50e8, #0e9ac0); color: white; font-weight: 800; padding: .65rem 1.1rem; }
.stButton > button:hover { border: 0; color: white; filter: brightness(1.06); }
[data-testid="stSidebar"] { background: #f0f3ff; }
[data-testid="stMetric"] { background: white; border: 1px solid #e2e8f0; padding: 14px 16px; border-radius: 16px; }
</style>
""", unsafe_allow_html=True)

TEMAS = [
    ("Razones y proporciones", 1, 4),
    ("Conversiones y regla de tres", 5, 9),
    ("Ecuaciones lineales", 10, 13),
    ("Ley de Ohm y circuitos", 14, 18),
    ("Gráficas y funciones", 19, 23),
    ("Sistemas de ecuaciones", 24, 27),
    ("Proporcionalidad directa e inversa", 28, 31),
    ("Sucesiones y patrones", 32, 34),
    ("Fórmulas con varias variables", 35, 37),
    ("Ecuaciones cuadráticas y aplicaciones", 38, 40),
]

TITULOS = {
    1: "Proporción de piezas", 2: "Escala de un plano", 3: "Mezcla para un proceso", 4: "Engranajes",
    5: "Conversión de longitud", 6: "Conversión de corriente", 7: "Tiempo de producción", 8: "Conversión de potencia", 9: "Conversión de temperatura",
    10: "Costo de materiales", 11: "Longitud de un cable", 12: "Producción diaria", 13: "Temperatura de un horno",
    14: "Corriente eléctrica", 15: "Resistencia", 16: "Voltaje", 17: "Potencia eléctrica", 18: "Resistencias en serie",
    19: "Producción por hora", 20: "Distancia recorrida", 21: "Costo de fabricación", 22: "Interpretación de una gráfica", 23: "Función de temperatura",
    24: "Compra de componentes", 25: "Motores", 26: "Edades de dos técnicos", 27: "Resistencias",
    28: "Proporcionalidad directa", 29: "Proporcionalidad inversa", 30: "Velocidad y tiempo", 31: "Personal de producción",
    32: "Producción", 33: "Patrón de programación", 34: "Mantenimiento",
    35: "Área de una pieza", 36: "Volumen de una caja", 37: "Potencia eléctrica",
    38: "Área de una pieza", 39: "Trayectoria de un objeto", 40: "Diseño de un área de trabajo",
}

# Encabezado
st.markdown("""
<div class="alva-hero">
  <div class="alva-kicker">Proyecto escolar · Dossier matemático</div>
  <div class="alva-title">🤖 ALVA</div>
  <p class="alva-subtitle">Asistente Matemático Técnico · Resuelve, consulta y comprende 40 problemas.</p>
</div>
""", unsafe_allow_html=True)

# Indicadores
c1, c2, c3 = st.columns(3)
for col, label, value in [
    (c1, "PROBLEMAS DISPONIBLES", "40"),
    (c2, "TEMAS", "10"),
    (c3, "TIPO DE AYUDA", "Procedimiento + resultado"),
]:
    with col:
        st.markdown(f'<div class="info-card"><div class="info-label">{label}</div><div class="info-value">{value}</div></div>', unsafe_allow_html=True)

st.write("")
st.markdown('<div class="section-title">🔎 Explora el dossier</div>', unsafe_allow_html=True)
st.markdown('<div class="small-muted">Selecciona un tema y después el problema que deseas resolver.</div>', unsafe_allow_html=True)

with st.sidebar:
    st.markdown("# 🤖 ALVA")
    st.caption("Asistente Matemático Técnico")
    st.divider()
    st.markdown("### Navegación")
    tema_nombres = [t[0] for t in TEMAS]
    tema_elegido = st.selectbox("Selecciona un tema", tema_nombres)
    tema_actual = next(t for t in TEMAS if t[0] == tema_elegido)
    numeros = list(range(tema_actual[1], tema_actual[2] + 1))
    problema = st.selectbox(
        "Selecciona un problema",
        numeros,
        format_func=lambda n: f"Problema {n:02d} · {TITULOS[n]}",
    )
    st.divider()
    st.caption("ALVA · Dossier de 40 problemas")

# Panel principal de selección
left, right = st.columns([1.35, 1], gap="large")
with left:
    st.markdown(f"### Problema {problema:02d}")
    st.markdown(f"**{TITULOS[problema]}**")
    st.info(f"Tema: {tema_elegido}")
    resolver = st.button("✨ Resolver problema", use_container_width=True)
with right:
    st.markdown("### ¿Cómo funciona?")
    st.markdown("1. Elige el tema.\n2. Selecciona uno de sus problemas.\n3. Pulsa **Resolver problema**.\n4. Consulta el procedimiento y la respuesta.")

if resolver:
    salida = io.StringIO()
    with contextlib.redirect_stdout(salida):
        resolver_problema(problema)
    st.session_state["alva_resultado"] = salida.getvalue().strip()
    st.session_state["alva_problema"] = problema

if st.session_state.get("alva_resultado"):
    if st.session_state.get("alva_problema") == problema:
        st.write("")
        st.markdown('<div class="section-title">📘 Desarrollo del problema</div>', unsafe_allow_html=True)
        st.markdown('<div class="result-card">', unsafe_allow_html=True)
        st.success("¡Problema resuelto!")
        st.code(st.session_state["alva_resultado"], language="text")
        st.markdown('</div>', unsafe_allow_html=True)
        st.download_button(
            "⬇️ Descargar procedimiento",
            data=st.session_state["alva_resultado"] + "\n",
            file_name=f"ALVA_problema_{problema:02d}.txt",
            mime="text/plain",
        )

with st.expander("📚 Ver los 10 temas del dossier"):
    for nombre, inicio, fin in TEMAS:
        st.write(f"**{inicio:02d}–{fin:02d}.** {nombre}")

st.divider()
st.caption("ALVA · Herramienta educativa para practicar matemáticas aplicadas a contextos técnicos.")
