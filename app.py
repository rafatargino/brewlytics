import streamlit as st
from sidebar import load_sidebar
from beeranalysis_one import load_beer_analysis_one
from beeranalysis_all import load_beer_analysis_all

#criar funções de carregamento de dados
#@st.cache_data   # decorator para atribuir uma funcionalidade extra para uma função 
#def carregar_cotacoes(empresas):

# Ajustar as margens para deixar a tela mais larga
st.set_page_config(page_title="brewlytics", layout="wide")

# Título inicial
st.write("# 🍻 brewlytics")

# carregando a sidebar com os estilos e descritores
load_sidebar()

# Separando a tela principal em duas coluanas: análise do grupo e análise individual
col_all, col_one = st.columns(2)

# Análise do grupo
load_beer_analysis_all(col_all)

# Análise individual
load_beer_analysis_one(col_one)
