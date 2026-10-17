"""
Mundora RPG — runner Streamlit
------------------------------
Serve o app completo (HTML único) dentro do Streamlit.

Uso:
  cd mundora-streamlit
  pip install -r requirements.txt
  streamlit run streamlit_app.py
"""

from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Mundora RPG",
    page_icon="⚔️",
    layout="wide",
    initial_sidebar_state="collapsed",
)

HTML_FILE = Path(__file__).resolve().parent / "Mundora-RPG-completo.html"

st.markdown(
    """
    <style>
      /* remove padding extra do Streamlit para o jogo ocupar a tela */
      .block-container { padding-top: 0.6rem; padding-bottom: 0; max-width: 100%; }
      header[data-testid="stHeader"] { background: transparent; }
      div[data-testid="stToolbar"] { display: none; }
    </style>
    """,
    unsafe_allow_html=True,
)

if not HTML_FILE.exists():
    st.error(f"Arquivo do jogo não encontrado: `{HTML_FILE.name}`")
    st.info("Coloque `Mundora-RPG-completo.html` na mesma pasta deste script.")
    st.stop()

html = HTML_FILE.read_text(encoding="utf-8", errors="replace")

# Garante viewport móvel caso o HTML original não tenha
if "<meta name=\"viewport\"" not in html.lower():
    html = html.replace(
        "<head>",
        '<head>\n  <meta name="viewport" content="width=device-width, initial-scale=1" />',
        1,
    )

with st.sidebar:
    st.title("⚔️ Mundora RPG")
    st.caption("App embutido no Streamlit")
    st.download_button(
        label="⬇️ Baixar HTML único",
        data=html.encode("utf-8"),
        file_name="Mundora-RPG-completo.html",
        mime="text/html",
    )
    altura = st.slider("Altura da janela do jogo (px)", 600, 1400, 900, 50)
    st.markdown("---")
    st.markdown(
        "O progresso (conta, herói, itens) fica no **navegador** "
        "(localStorage), não no servidor Streamlit."
    )

components.html(html, height=altura, scrolling=True)
