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


def load_sidebar():

    # Exemplo de seletor de estilo de cerveja
    beer_styles = ["21A. American IPA", "20A. American Porter", "21B. Specialty IPA: Belgian IPA"]
    selected_beer_style = st.sidebar.selectbox("Selecione o estilo de cerveja", beer_styles)
    print("Estilo selecionado: ", selected_beer_style)

    # Carregar os descritores do estilo de cerveja selecionado
    one_beerstyle = get_beer_style_descriptors(selected_beer_style)
    #st.sidebar.json(beerstyle_dict)

    # Exibir os descritores
    st.sidebar.write("Descritores do estilo de cerveja selecionado:")

    tags_html = ""
    for avaliacao in one_beerstyle.keys(): 
        tags_html += F"<p style='font-size: 13px;'>{avaliacao}: "
        for grupo in one_beerstyle.get(avaliacao, []):
            if avaliacao == "comparação de estilos":
                tags_html += f"<span style='background-color: #6C757D; color: white; border-radius: 4px 5px; padding: 4px 4px; margin-right: 7px; font-size: 14px; display: inline-block; line-height: 1.1; height: 22px;'>{grupo}</span>"                
            else:
                tags_html += f"<span style='background-color: #B8860B; color: white; border-radius: 4px 5px; padding: 4px 4px; margin-right: 7px; font-size: 14px; display: inline-block; line-height: 1.1; height: 22px;'>{grupo}</span>"
                for descritor in one_beerstyle.get(avaliacao, [])[grupo]:            
                    tags_html += f"<span style='background-color: #FF7F00; color: white; border-radius: 4px 5px; padding: 4px 4px; margin-right: 7px; font-size: 14px; display: inline-block; line-height: 1.1; height: 22px;'>{descritor}</span>"
                    # 007BFF FF7F00

    st.sidebar.markdown(tags_html, unsafe_allow_html=True)




