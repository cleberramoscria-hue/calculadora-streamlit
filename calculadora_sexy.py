"""
🔥 CALCULADORA PREMIUM - VERSÃO 2.0
100% segura | Responsiva | Histórico | Tema escuro/claro
"""

import streamlit as st

# ⚙️ CONFIGURAÇÃO DA PÁGINA
st.set_page_config(
    page_title="Calculadora Premium",
    page_icon="🔥",
    layout="centered",
    initial_sidebar_state="expanded"
)

# 🎨 TEMA CLARO/ESCURO
if "tema" not in st.session_state:
    st.session_state.tema = "escuro"

def alternar_tema():
    st.session_state.tema = "claro" if st.session_state.tema == "escuro" else "escuro"

# 🎨 CSS PERSONALIZADO COM HOVER EFFECT
if st.session_state.tema == "escuro":
    tema_css = """
    .stApp {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
    }
    .stButton > button {
        background: linear-gradient(135deg, #ff6b6b, #ee5a24);
        color: white;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(255,107,107,0.3);
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(255,107,107,0.5);
    }
    .result-box {
        background: linear-gradient(135deg, #0f3460, #1a1a2e);
    }
    """
else:
    tema_css = """
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    .stButton > button {
        background: linear-gradient(135deg, #ff6b6b, #ee5a24);
        color: white;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(255,107,107,0.3);
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(255,107,107,0.5);
    }
    .result-box {
        background: white;
        border: 1px solid #ddd;
    }
    h1, .stMarkdown, .stSelectbox label, .stNumberInput label {
        color: #1a1a2e !important;
    }
    """

st.markdown(f"<style>{tema_css}</style>", unsafe_allow_html=True)

# 📱 HISTÓRICO
if "historico" not in st.session_state:
    st.session_state.historico = []

# 🎯 TÍTULO
st.title("🔥 Calculadora Premium")
st.caption("100% segura | Sem eval() | Design moderno")

# 📊 SIDEBAR
with st.sidebar:
    st.header("🎮 Controles")
    
    # Tema
    st.button("🌙 Claro" if st.session_state.tema == "escuro" else "🌞 Escuro", 
              on_click=alternar_tema, use_container_width=True)
    
    st.header("🔗 Links")
    st.markdown("[🐙 GitHub](https://github.com/cleberramoscria-hue)")
    st.markdown("[💼 LinkedIn](https://www.linkedin.com/in/cleber-ramos-oliveira-00035a397/)")
    st.markdown("[📧 E-mail](mailto:cleber.ramos.cria@gmail.com)")
    
    st.header("📜 Histórico")
    if st.button("🗑️ Limpar histórico", use_container_width=True):
        st.session_state.historico = []
        st.rerun()
    
    for item in reversed(st.session_state.historico[-10:]):
        st.caption(item)

# 🧮 INTERFACE PRINCIPAL
st.markdown("---")

# Operações extras
operacao = st.selectbox(
    "📌 Escolha a operação",
    ["➕ Soma", "➖ Subtração", "✖️ Multiplicação", "➗ Divisão", 
     "🔢 Potência (x^y)", "📐 Raiz Quadrada (√x)", "💯 Porcentagem (%)"]
)

# Números (responsivo)
col1, col2 = st.columns(2)

with col1:
    num1 = st.number_input("Primeiro número", value=0.0, step=1.0, format="%f")

with col2:
    if "Raiz" not in operacao:
        num2 = st.number_input("Segundo número", value=0.0, step=1.0, format="%f")
    else:
        st.markdown("")
        st.markdown("")

# 🎯 FUNÇÃO PARA FORMATAR NÚMEROS (padrão Brasil)
def formatar_numero(valor):
    if valor == int(valor):
        return str(int(valor))
    return f"{valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

# 🚀 CÁLCULO
st.markdown("---")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    calcular = st.button("✨ CALCULAR ✨", use_container_width=True)

if calcular:
    try:
        if operacao == "➕ Soma":
            resultado = num1 + num2
            expressao = f"{formatar_numero(num1)} + {formatar_numero(num2)} = {formatar_numero(resultado)}"
            st.success(f"✅ **{expressao}**")
            
        elif operacao == "➖ Subtração":
            resultado = num1 - num2
            expressao = f"{formatar_numero(num1)} - {formatar_numero(num2)} = {formatar_numero(resultado)}"
            st.success(f"✅ **{expressao}**")
            
        elif operacao == "✖️ Multiplicação":
            resultado = num1 * num2
            expressao = f"{formatar_numero(num1)} × {formatar_numero(num2)} = {formatar_numero(resultado)}"
            st.success(f"✅ **{expressao}**")
            
        elif operacao == "➗ Divisão":
            if num2 == 0:
                st.error("🚨 **ERRO CRÍTICO: Divisão por zero não é permitida!** 🚨")
                st.stop()
            resultado = num1 / num2
            expressao = f"{formatar_numero(num1)} ÷ {formatar_numero(num2)} = {formatar_numero(resultado)}"
            st.success(f"✅ **{expressao}**")
            
        elif operacao == "🔢 Potência (x^y)":
            resultado = num1 ** num2
            expressao = f"{formatar_numero(num1)} ^ {formatar_numero(num2)} = {formatar_numero(resultado)}"
            st.success(f"✅ **{expressao}**")
            
        elif operacao == "📐 Raiz Quadrada (√x)":
            if num1 < 0:
                st.error("🚨 **ERRO: Não existe raiz quadrada de número negativo!** 🚨")
                st.stop()
            resultado = num1 ** 0.5
            expressao = f"√{formatar_numero(num1)} = {formatar_numero(resultado)}"
            st.success(f"✅ **{expressao}**")
            
        elif operacao == "💯 Porcentagem (%)":
            resultado = (num1 * num2) / 100
            expressao = f"{formatar_numero(num2)}% de {formatar_numero(num1)} = {formatar_numero(resultado)}"
            st.success(f"✅ **{expressao}**")
        
        # Adicionar ao histórico
        st.session_state.historico.append(expressao)
        st.balloons()
        
    except Exception as e:
        st.error(f"🚨 **Erro inesperado:** {e}")

# 🦶 RODAPÉ
st.markdown("---")
st.caption("🔒 100% seguro - Nenhum eval() foi usado")
st.caption("🔥 ADS - UNIASSELVI | Cleber Ramos")
