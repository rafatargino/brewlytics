import streamlit as st
from sidebar import load_sidebar

#criar funções de carregamento de dados
#@st.cache_data   # decorator para atribuir uma funcionalidade extra para uma função 
#def carregar_cotacoes(empresas):

# criar a interface do streamlit
st.write("""
# 🍻 brewlytics

""") # pode formatar com markdown

# sidebar 
# --------------------------------------------------------------------------------

load_sidebar()



# --------------------------------------------------------------------------------


