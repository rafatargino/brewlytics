import json
import streamlit as st

#criar funções de carregamento de dados
@st.cache_data   # decorator para atribuir uma funcionalidade extra para uma função
def load_bjcp_descriptors():
    # Carregar o arquivo JSON
    with open('bjcp_keywords.json', 'r', encoding='utf-8') as arquivo:
        beerstyle_dict = json.load(arquivo)
    #print(beerstyle_dict)
    return beerstyle_dict

def get_beer_style_descriptors(beer_style):
    beerstyle_dict = load_bjcp_descriptors()
    return beerstyle_dict.get(beer_style, {})


def load_beer_analysis_all(coluna):
    
    with coluna:
        st.header("Análise do Grupo")
        st.write("Este é o conteúdo da coluna 1.")
        st.button("Botão 1")


