import requests
import streamlit as st

BASE_URL = 'https://api.github.com'

def selecionarUsuario(username):
    url = f'{BASE_URL}/users/{username}'
    response = requests.get(url)
    return response

def exibir_perfil(infoUsuario):
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

def ui():
    st.title('Consultar perfis no Github 🤓')

    # Espaçamento para separar o título da seção de entrada do usuário
    st.write("")

    # Organização visual usando uma coluna
    col1, col2 = st.columns([1, 2])

    with col1:
        username = st.text_input('Insira o username de usuário do Github')

    with col2:
        st.image("https://platzi.com.br/blog/wp-content/uploads/2022/04/cover-github-105d8310-41f9-4d9e-91e0-4cbde3d8c645-50decd84-0c17-476c-b8dc-61091d0dd27f-3.webp", width=100)
    
    if st.button('Buscar Perfil'):
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

ui()
