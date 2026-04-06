"""
🔥 CALCULADORA  - Versão Premium
100% segura, sem eval(), com design moderno
"""

import streamlit as st

# ⚙️ CONFIGURAÇÃO DA PÁGINA
st.set_page_config(
    page_title="Calculadora Sexy",
    page_icon="🔥",
    layout="centered",
    initial_sidebar_state="expanded"
)

# 🎨 CSS PERSONALIZADO
st.markdown("""
<style>
    /* Fundo gradiente */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Título */
    h1 {
        text-align: center;
        color: white;
        font-size: 3rem;
        margin-bottom: 0;
    }
    
    /* Subtítulo */
    .subtitle {
        text-align: center;
        color: rgba(255,255,255,0.8);
        margin-bottom: 2rem;
    }
    
    /* Cards */
    .stButton > button {
        background: linear-gradient(135deg, #ff6b6b, #ee5a24);
        color: white;
        font-size: 18px;
        font-weight: bold;
        border-radius: 30px;
        padding: 10px 20px;
        transition: all 0.3s;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 20px rgba(0,0,0,0.3);
    }
    
    /* Resultado */
    .success-box {
        background: linear-gradient(135deg, rgba(0,255,136,0.2), rgba(0,255,136,0.05));
        border-left: 4px solid #00ff88;
        padding: 20px;
        border-radius: 15px;
        margin: 20px 0;
        text-align: center;
    }
    
    .result-number {
        font-size: 48px;
        font-weight: bold;
        color: #00ff88;
        margin: 10px 0;
    }
    
    /* Sidebar */
    .css-1d391kg {
        background: rgba(0,0,0,0.3);
        backdrop-filter: blur(10px);
    }
    
    /* Inputs */
    .stNumberInput > div > div > input {
        background: rgba(255,255,255,0.1);
        color: white;
        border-radius: 15px;
        font-size: 24px;
        text-align: center;
    }
    
    .stSelectbox > div > div {
        background: rgba(255,255,255,0.1);
        color: white;
        border-radius: 15px;
    }
</style>
""", unsafe_allow_html=True)

# 🎯 TÍTULO
st.markdown("""
<h1>🔥 CALCULADORA SEXY 🔥</h1>
<p class="subtitle">Design moderno | 100% segura | Sem eval()</p>
""", unsafe_allow_html=True)

# 📱 SIDEBAR
with st.sidebar:
    st.markdown("### 🚀 **Sobre o Projeto**")
    st.markdown("""
    ✅ **100% segura** (sem eval())  
    ✅ **Validação de inputs**  
    ✅ **Tratamento de erros**  
    ✅ **Design premium**  
    """)
    
    st.markdown("---")
    
    st.markdown("### 🔗 **Links**")
    st.markdown("[🐙 GitHub](https://github.com/cleberramoscria-hue)")
    st.markdown("[💼 LinkedIn](https://www.linkedin.com/in/cleber-ramos-oliveira-00035a397/)")
    st.markdown("[📧 E-mail](mailto:cleber.ramos.cria@gmail.com)")
    
    st.markdown("---")
    
    st.caption("🔒 Projeto seguro - ADS UNIASSELVI")

# 📊 INTERFACE PRINCIPAL
st.markdown("---")

# Operação
operacao = st.selectbox(
    "📌 **Escolha a operação**",
    ["➕ Soma", "➖ Subtração", "✖️ Multiplicação", "➗ Divisão"]
)

# Números
col1, col2 = st.columns(2)

with col1:
    st.markdown("🔵 **Primeiro número**")
    num1 = st.number_input("", key="num1", value=0.0, step=1.0, label_visibility="collapsed")

with col2:
    st.markdown("🔴 **Segundo número**")
    num2 = st.number_input("", key="num2", value=0.0, step=1.0, label_visibility="collapsed")

# Botão calcular
st.markdown("---")

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    calcular = st.button("✨ CALCULAR ✨", use_container_width=True)

# 📈 RESULTADO
if calcular:
    
    if operacao == "➕ Soma":
        resultado = num1 + num2
        operador = "+"
        st.markdown(f"""
        <div class="success-box">
            <div style="font-size: 18px; color: #00ff88;">✅ RESULTADO</div>
            <div class="result-number">{num1} {operador} {num2} = {resultado}</div>
            <div style="font-size: 12px;">Cálculo seguro (sem eval())</div>
        </div>
        """, unsafe_allow_html=True)
        st.balloons()
        
    elif operacao == "➖ Subtração":
        resultado = num1 - num2
        operador = "-"
        st.markdown(f"""
        <div class="success-box">
            <div style="font-size: 18px; color: #00ff88;">✅ RESULTADO</div>
            <div class="result-number">{num1} {operador} {num2} = {resultado}</div>
            <div style="font-size: 12px;">Cálculo seguro (sem eval())</div>
        </div>
        """, unsafe_allow_html=True)
        st.balloons()
        
    elif operacao == "✖️ Multiplicação":
        resultado = num1 * num2
        operador = "×"
        st.markdown(f"""
        <div class="success-box">
            <div style="font-size: 18px; color: #00ff88;">✅ RESULTADO</div>
            <div class="result-number">{num1} {operador} {num2} = {resultado}</div>
            <div style="font-size: 12px;">Cálculo seguro (sem eval())</div>
        </div>
        """, unsafe_allow_html=True)
        st.balloons()
        
    elif operacao == "➗ Divisão":
        if num2 == 0:
            st.error("🚨 **ERRO: Divisão por zero não é permitida!** 🚨")
        else:
            resultado = num1 / num2
            operador = "÷"
            st.markdown(f"""
            <div class="success-box">
                <div style="font-size: 18px; color: #00ff88;">✅ RESULTADO</div>
                <div class="result-number">{num1} {operador} {num2} = {resultado}</div>
                <div style="font-size: 12px;">Cálculo seguro (sem eval())</div>
            </div>
            """, unsafe_allow_html=True)
            st.balloons()

# Rodapé
st.markdown("---")
st.caption("🔥 Desenvolvido com Streamlit | ADS - UNIASSELVI | 100% seguro")
