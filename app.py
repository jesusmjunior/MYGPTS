import streamlit as st
import json
from graphviz import Digraph

st.set_page_config(
    page_title="📲 MY GPTs — Catálogo Interativo",
    layout="wide"
)

st.title("📲 MY GPTs — Catálogo Interativo de Inteligências Pessoais")
st.markdown("""
Organizado por Ramos de Atividade (S(s))  
Cada GPT é uma Entidade Funcional (T(a)) com:

- Nome (núcleo nominal/verbal)  
- Pertencimento lógico-fuzzy (γ)  
- Breve descrição funcional
""")

# Carregar catálogo JSON
def carregar_catalogo():
    with open("gpt_catalogo1.json", "r", encoding="utf-8") as f:
        return json.load(f)

catalogo = carregar_catalogo()

# Título principal do catálogo
st.header(f"🔷 P(p): {catalogo['titulo']}")

# Inicializar grafo
grafo = Digraph("Grafo GPTs", format="png")
grafo.attr(rankdir='LR', size='10')
grafo.node("root", "📲 My GPTs", shape='folder', style='filled', fillcolor='lightblue')

# Filtro de pertinência γ fuzzy
gamma_min, gamma_max = st.slider("Filtrar por γ (Pertencimento Semântico)", 0.6, 1.0, (0.75, 1.0), step=0.01)

# Visualização por subsequência S(s)
for s in catalogo['estrutura']:
    s_id = s['subsequencia']
    st.subheader(f"📁 S(s): {s_id}")
    grafo.node(s_id, f"S(s): {s_id}", shape='component', style='filled', fillcolor='orange')
    grafo.edge("root", s_id)

    for gpt in s['gpts']:
        if gamma_min <= gpt['pertencimento'] <= gamma_max:
            gpt_id = f"T(a)-{gpt['id']}"
            gpt_label = f"{gpt_id}\n{gpt['nome']}\nγ = {gpt['pertencimento']}"
            grafo.node(gpt_id, gpt_label, shape='note', style='filled', fillcolor='lightgrey')
            grafo.edge(s_id, gpt_id)
            
            with st.container():
                st.markdown(f"### 🔹 {gpt['nome']}")
                st.markdown(f"**T(a):** Entidade Funcional")
                st.markdown(f"**γ (Pertencimento):** {gpt['pertencimento']:.2f}")
                st.progress(gpt['pertencimento'])

# Visualização gráfica
st.subheader("🧠 Visualização Semântica em Grafo")
st.graphviz_chart(grafo)

# Exportar JSON
st.download_button(
    label="📥 Baixar Catálogo JSON",
    data=json.dumps(catalogo, ensure_ascii=False, indent=2),
    file_name="gpt_catalogo1.json",
    mime="application/json"
)

# Rodapé
st.markdown("""
---
📌 Powered by Lógica Modular Fuzzy α → θ  
🧩 T(a) → S(s) → P(p) com pesos γ (pertencimento semântico)  
📤 Desenvolvido para gestão e visualização dos seus GPTs pessoais
""")
