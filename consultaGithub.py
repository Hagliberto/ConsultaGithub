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
    
    st.title('Consulta Github')
    username = st.text_input('Insira o username de usuário do Github')
    
    if st.button('Buscar'):
        response = selecionarUsuario(username)
        if response.status_code == 200:
            infoUsuario = response.json()
            exibir_perfil(infoUsuario)
        elif response.status_code == 404:
            st.error('Usuário não encontrado. Verifique o nome de usuário.')
        else:
            st.error('Ocorreu um erro ao buscar o perfil do usuário. Tente novamente mais tarde.')

ui()
