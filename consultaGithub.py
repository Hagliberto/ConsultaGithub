import requests
import streamlit as st

BASE_URL = 'https://api.github.com'

def selecionarUsuario(username):
    url = f'{BASE_URL}/users/{username}'
    response = requests.get(url)
    return response

def exibir_perfil(infoUsuario):
    st.markdown(f'''
        <div class="card" style="width: 18rem;">
            <img src="{infoUsuario['avatar_url']}" class="card-img-top" alt="...">
            <div class="card-body">
                <h5 class="card-title">{infoUsuario['login']}</h5>
                <p class="card-text">{infoUsuario['bio']}</p>
                <p class="card-text">Seguidores: {infoUsuario['followers']}</p>
                <p class="card-text">Repositórios públicos: {infoUsuario['public_repos']}</p>
                <a href="{infoUsuario['html_url']} " style="color: white; text-decoration: none;" class="btn btn-primary">Ver Perfil</a>
            </div>
        </div>
    ''', unsafe_allow_html=True)

def ui():
    st.markdown('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous">', unsafe_allow_html=True)
    
    st.title('Consultar perfis no Github')

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
            st.markdown('<h2>Perfil do Usuário</h2>', unsafe_allow_html=True)
            exibir_perfil(infoUsuario)
        elif response.status_code == 404:
            st.error('Usuário não encontrado. Verifique o nome de usuário.')
        else:
            st.error('Ocorreu um erro ao buscar o perfil do usuário. Tente novamente mais tarde.')

ui()
