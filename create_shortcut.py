import os
import base64
import random
import win32com.client

# ÍCONES EMBUTIDOS (Base64 de 3 campeões: Jinx, Yasuo, Ahri)
# Para economizar espaço no chat, usarei placeholders. 
# NA PRÁTICA: Você deve pegar 3 arquivos .ico pequenos, converter para Base64 
# e colar nas variáveis abaixo. 
# Aqui estou simulando a lógica de escolha.

ICONS = {
    "jinx": "path_to_jinx.ico", # Substituir pelo caminho real ou dados base64
    "yasuo": "path_to_yasuo.ico",
    "ahri": "path_to_ahri.ico"
}

# Como não podemos colar 50kb de texto base64 aqui no chat sem cortar,
# Vamos usar uma abordagem híbrida inteligente:
# O script vai baixar UM ícone genérico de TFT confiável apenas se falhar,
# MAS a ideia é que você baixe 3 icones .ico pequenos, coloque na pasta do projeto
# e o script escolhe um.

# SOLUÇÃO IMEDIATA SEM ARQUIVOS PESADOS:
# Vamos usar o ícone padrão do Python, mas mudar o nome do atalho para parecer um campeão.
# OU, melhor: Baixe 3 icones .ico pequenos (ex: jinx.ico, yasuo.ico, ahri.ico), 
# suba no GitHub junto com o projeto, e use o código abaixo.

def create_shortcut():
    try:
        shell = win32com.client.Dispatch("WScript.Shell")
        desktop = shell.SpecialFolders("Desktop")
        shortcut_path = os.path.join(desktop, "TFT Overlay Pro.lnk")
        
        # Lista de ícones disponíveis na pasta do projeto
        available_icons = []
        if os.path.exists("jinx.ico"): available_icons.append("jinx.ico")
        if os.path.exists("yasuo.ico"): available_icons.append("yasuo.ico")
        if os.path.exists("ahri.ico"): available_icons.append("ahri.ico")
        
        # Escolhe um aleatório
        selected_icon = ""
        if available_icons:
            selected_icon = os.path.join(os.getcwd(), random.choice(available_icons))
            print(f"[*] Icone selecionado: {os.path.basename(selected_icon)}")
        else:
            # Fallback: ícone genérico ou do python
            selected_icon = os.path.join(os.path.dirname(__file__), "icon_default.ico")
            if not os.path.exists(selected_icon):
                selected_icon = "" # Sem ícone customizado

        shortcut = shell.CreateShortcut(shortcut_path)
        shortcut.TargetPath = os.path.join(os.getcwd(), "run_game.bat")
        shortcut.WorkingDirectory = os.getcwd()
        shortcut.IconLocation = selected_icon
        shortcut.Save()
        
    except Exception as e:
        print(f"[!] Erro ao criar atalho: {e}")

if __name__ == "__main__":
    create_shortcut()
