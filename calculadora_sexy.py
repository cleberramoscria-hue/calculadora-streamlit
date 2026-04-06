"""
🔥 CALCULADORA PREMIUM - VERSÃO 2.3
100% segura | Responsiva | Histórico | Tema escuro/claro
SIDEBAR CORRIGIDA!
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

# 🎨 CSS PERSONALIZADO COM SIDEBAR CORRIGIDA
if st.session_state.tema == "escuro":
    tema_css = """
    /* Fundo principal escuro */
    .stApp {
        background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
    }
    
    /* ===== SIDEBAR COMPLETAMENTE ESCURA ===== */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0f0f1a 0%, #1a1a2e 100%) !important;
        border-right: 1px solid rgba(255,255,255,0.1) !important;
    }
    
    [data-testid="stSidebar"] * {
        color: #ffffff !important;
    }
    
    [data-testid="stSidebar"] .stMarkdown,
    [data-testid="stSidebar"] p,
    [data-testid="stSidebar"] span,
    [data-testid="stSidebar"] label,
    [data-testid="stSidebar"] h1,
    [data-testid="stSidebar"] h2,
    [data-testid="stSidebar"] h3,
    [data-testid="stSidebar"] h4,
    [data-testid="stSidebar"] h5,
    [data-testid="stSidebar"] h6 {
        color: #ffffff !important;
    }
    
    /* Botões na sidebar */
    [data-testid="stSidebar"] .stButton button {
        background: linear-gradient(135deg, #ff6b6b, #ee5a24) !important;
        color: white !important;
        border: none !important;
    }
    
    [data-testid="stSidebar"] .stButton button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(255,107,107,0.4);
    }
    
    /* Links na sidebar */
    [data-testid="stSidebar"] a {
        color: #ff6b6b !important;
        text-decoration: none;
    }
    
    [data-testid="stSidebar"] a:hover {
        color: #ff8888 !important;
        text-decoration: underline;
    }
    
    /* ===== FIM SIDEBAR ===== */
    
    /* TODOS os textos BRANCOS no tema escuro */
    h1, h2, h3, h4, h5, h6, p, span, label, .stMarkdown, .stCaption {
        color: #ffffff !important;
    }
    
    /* Título principal */
    h1 {
        color: #ffffff !important;
        text-shadow: 0 0 10px rgba(255,255,255,0.3);
    }
    
    /* Inputs com texto branco */
    .stNumberInput > div > div > input {
        background: rgba(255,255,255,0.1);
        color: white !important;
        border-radius: 10px;
        border: 1px solid rgba(255,255,255,0.3);
    }
    
    .stNumberInput > div > div > input:focus {
        border-color: #ff6b6b !important;
        box-shadow: 0 0 5px rgba(255,107,107,0.5);
    }
    
    /* Selectbox com texto branco */
    .stSelectbox > div > div {
        background: rgba(255,255,255,0.1);
        color: white !important;
        border-radius: 10px;
    }
    
    .stSelectbox label {
        color: white !important;
    }
    
    /* Botão de calcular principal */
    .stButton > button {
        background: linear-gradient(135deg, #ff6b6b, #ee5a24);
        color: white !important;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(255,107,107,0.3);
        font-weight: bold;
        border: none;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(255,107,107,0.5);
    }
    
    /* Resultado sucesso */
    .stAlert[data-baseweb="notification"] {
        background: rgba(0,255,0,0.15) !important;
        border-left: 4px solid #00ff88 !important;
    }
    
    .stAlert p {
        color: #00ff88 !important;
    }
    
    /* Mensagem de erro */
    .stAlert[data-baseweb="notification"]:has(.stAlert) {
        background: rgba(255,0,0,0.15) !important;
        border-left: 4px solid #ff4444 !important;
    }
    
    /* Rodapé */
    footer, .stFooter {
        color: #888888 !important;
    }
    
    /* Divisores */
    hr {
        border-color: rgba(255,255,255,0.1) !important;
    }
    """
else:
    tema_css = """
    /* Fundo claro */
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
    }
    
    /* Sidebar clara */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #ffffff 0%, #f0f2f5 100%) !important;
        border-right: 1px solid #ddd !important;
    }
    
    [data-testid="stSidebar"] * {
        color: #1a1a2e !important;
    }
    
    /* Botões na sidebar */
    [data-testid="stSidebar"] .stButton button {
        background: linear-gradient(135deg, #ff6b6b, #ee5a24) !important;
        color: white !important;
    }
    
    /* Textos escuros no tema claro */
    h1, h2, h3, h4, h5, h6, p, span, label, .stMarkdown {
        color: #1a1a2e !important;
    }
    
    /* Botão de calcular */
    .stButton > button {
        background: linear-gradient(135deg, #ff6b6b, #ee5a24);
        color: white !important;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(255,107,107,0.3);
        font-weight: bold;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 25px rgba(255,107,107,0.5);
    }
    
    /* Inputs */
    .stNumberInput > div > div > input {
        background: white;
        color: #1a1a2e !important;
        border-radius: 10px;
        border: 1px solid #ddd;
    }
    
    /* Selectbox */
    .stSelectbox > div > div {
        background: white;
        color: #1a1a2e !important;
        border-radius: 10px;
    }
    
    /* Links */
    a {
        color: #ee5a24 !important;
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
    st.markdown("## 🎮 Controles")
    
    # Tema
    if st.button("🌙 Tema Escuro" if st.session_state.tema == "claro" else "🌞 Tema Claro", use_container_width=True):
        alternar_tema()
        st.rerun()
    
    st.markdown("---")
    
    st.markdown("## 🔗 Links")
    st.markdown("[🐙 GitHub](https://github.com/cleberramoscria-hue)")
    st.markdown("[💼 LinkedIn](https://www.linkedin.com/in/cleber-ramos-oliveira-00035a397/)")
    st.markdown("[📧 E-mail](mailto:cleber.ramos.cria@gmail.com)")
    
    st.markdown("---")
    
    st.markdown("## 📜 Histórico")
    if st.button("🗑️ Limpar histórico", use_container_width=True):
        st.session_state.historico = []
        st.rerun()
    
    st.markdown("---")
    
    # Mostrar histórico
    if st.session_state.historico:
        for item in reversed(st.session_state.historico[-10:]):
            st.markdown(f"📌 {item}")
    else:
        st.caption("Nenhum cálculo ainda")

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
