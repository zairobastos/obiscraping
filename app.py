import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="OBI - Rotulação de Questões", page_icon="🤓", layout="wide")

selected2 = option_menu(None, ["Início", "Extração de Dados", "Questões", 'Resultados'], 
    icons=['house', 'file-earmark-break', "list-task", 'graph-up'], 
    menu_icon="cast", default_index=0, orientation="horizontal")

#Icones Bootstrap
st.markdown(
    """
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap-icons/1.5.0/font/bootstrap-icons.min.css">
    """,
    unsafe_allow_html=True
)


if selected2 == "Início": 
	st.markdown("<br>", unsafe_allow_html=True)
	st.markdown('<h2><i class="bi bi-house"></i>  OBI - Início</h2>', unsafe_allow_html=True)

if selected2 == "Extração de Dados":
	st.markdown("<br>", unsafe_allow_html=True)
	st.markdown('<h2><i class="bi bi-file-earmark-break"></i>  Extração de Dados</h2>', unsafe_allow_html=True)
	
	col1, col2, col3, col4 = st.columns(4)
	col1.text_input("Nome da questão", placeholder="questão 01")
	col2.number_input("Nível da questão", value=1, min_value=1, max_value=3)
	col3.number_input("Ano da questão", value=2022, min_value=2022, max_value=2024)
	col4.number_input("Fase da questão", value=1, min_value=1, max_value=3)

	st.markdown("<br>", unsafe_allow_html=True)

	st.text_area("", placeholder="Texto da questão", height=400)
	st.markdown("<br>", unsafe_allow_html=True)
	st.markdown(
    """
    <style>
    .custom-button {
        background-color: #ff4b4b;
        color: white;
        padding: 0.5rem 1rem;
        font-size: 1.25rem;
        font-weight: bold;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        width: 50%;
		height: 50px;
        text-align: center;
        display: block;
        transition: background-color 0.3s;
    }
    .custom-button:hover {
        background-color: #cc3c3c;
    }
    </style>
    """, 
    unsafe_allow_html=True
)

	# Cria o botão personalizado com HTML e CSS
	st.markdown('<div align="center"><button class="custom-button">Gerar Análise da Questão</button></div>', unsafe_allow_html=True)

if selected2 == "Questões":
	st.markdown("<br>", unsafe_allow_html=True)
	st.markdown('<h2><i class="bi bi-list-task"></i>  Questões</h2>', unsafe_allow_html=True)



if selected2 == "Resultados":
	st.markdown("<br>", unsafe_allow_html=True)
	st.markdown('<h2><i class="bi bi-graph-up"></i>  Resultados</h2>', unsafe_allow_html=True)