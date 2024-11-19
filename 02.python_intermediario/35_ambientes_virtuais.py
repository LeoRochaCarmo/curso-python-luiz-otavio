# Ambientes virtuais em Python (venv)
# Um ambiente virtual carrega toda a sua instalação
# do Python para uma pasta no caminho escolhido.
# Ao ativar um ambiente virtual, a instalação do
# ambiente virtual será usada.
# venv é o módulo que vamos usar para
# criar ambientes virtuais.
# Você pode dar o nome que preferir para um
# ambiente virtual, mas os mais comuns são:
# venv env .venv .env

#%%
# COMANDO PARA CRIAR AMBIENTE VIRTUAL (POWERSHELL)

# python -m venv venv (segundo venv é o nome dado ao ambiente)

#%%
# COMANDO PARA ATIVAR E DESATIVAR AMBIENTE VIRTUAL (POWERSHELL)

# .\venv\Scripts\activate OU venv\Scripts\activate

#%%
# COMANDO PARA SABER A ORIGEM DO PYTHON (POWERSHELL)

# gcm python -Syntax

#%%
# ATUALIZAR O PIP (Package installer for Python)

# python -m pip install pip --upgrade

#%%
# INSTALAR E DESINSTALAR BIBLIOTECAS

# pip install nome_da_biblioteca
# pip uninstall nome_da_biblioteca

# %%
# COMANDO PARA LISTAR OS PACOTES

# pip index versions nome_da_biblioteca

#%%
# INSTALAR VERSÃO ESPECÍFICA DE UM PACOTE

# pip install nome_da_biblioteca == número_da_versão

#%%
# EXIBIR PACOTES INSTALADOS E SUAS VERSÕES

# pip freeze

#%% 
# CRIAR ARQUIVO PARA DOCUMENTAR AS DEPENDÊNCIAS DO PROJETO

# pip freeze > requirements.txt

#%% 
# INSTALAR PACOTES A PARTIR DO ARQUIVO

# pip install -r requirements.txt

# %%
