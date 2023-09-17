import json
import requests
import streamlit as st
from streamlit_lottie import st_lottie
import os

BASE_URL = 'https://api.github.com'


def load_lottiefile(filepath: str):
    """
    Carrega um arquivo Lottie JSON.

    Args:
        filepath (str): O caminho para o arquivo JSON.

    Returns:
        dict: O conteúdo do arquivo JSON carregado em forma de dicionário.
    """
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f)


def selecionarUsuario(username):
    """
    Seleciona um usuário do GitHub com base no nome de usuário.

    Args:
        username (str): O nome de usuário do GitHub.

    Returns:
        requests.Response: A resposta da API contendo as informações do usuário.
    """
    url = f'{BASE_URL}/users/{username}'
    response = requests.get(url)
    return response


def exibir_perfil(infoUsuario):
    """
    Exibe as informações do perfil de um usuário do GitHub.

    Args:
        infoUsuario (dict): As informações do usuário obtidas da API do GitHub.
    """
    st.markdown(f'''
        <div style="
            border: 2px solid #ccc;
            border-radius: 5px;
            padding: 20px;
            max-width: 300px;
            text-align: center;
            background-color: #f9f9f9;
        ">
            <img src="{infoUsuario['avatar_url']}" alt="Avatar" style="
                max-width: 100%;
                border-radius: 50%;
            ">
            <h5 style="
                font-size: 1.5em;
                color: #333; /* Cor do texto */
            ">{infoUsuario['login']}</h5>
            <p style="
                font-size: 1.2em;
                color: #333; /* Cor do texto */
            ">{infoUsuario['bio']}</p>
            <p style="
                font-size: 1.2em;
                color: #333; /* Cor do texto */
            ">Seguidores: {infoUsuario['followers']}</p>
            <p style="
                font-size: 1.2em;
                color: #333; /* Cor do texto */
            ">Repositórios públicos: {infoUsuario['public_repos']}</p>
            <a href="{infoUsuario['html_url']}" style="
                text-decoration: none;
                background-color: #007BFF;
                color: white;
                padding: 10px 20px;
                border-radius: 5px;
                font-size: 1.2em;
                transition: background-color 0.3s;
            ">Ver Perfil</a>
        </div>
    ''', unsafe_allow_html=True)


def main():
    """
    Função principal que define a interface do Streamlit e controla o fluxo do programa.
    """
    #st.title('Perfil encontrado')

    # Barra lateral para pesquisa
    st.sidebar.title('Consultar perfis no Github')
    username = st.sidebar.text_input('Nome de usuário do GitHub')

    if st.sidebar.button('Buscar Perfil'):
        response = selecionarUsuario(username)
        if response.status_code == 200:
            infoUsuario = response.json()

            # Espaçamento após o botão para separar o perfil exibido
            st.write("")

            # Estilo para destacar as informações do perfil
            exibir_perfil(infoUsuario)
        elif response.status_code == 404:
            st.error('Usuário não encontrado. Verifique o nome de usuário.')
        else:
            st.error('Ocorreu um erro ao buscar o perfil do usuário. Tente novamente mais tarde.')


if __name__ == '__main__':
    main()