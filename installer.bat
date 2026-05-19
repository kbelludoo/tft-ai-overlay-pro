@echo off
color 0A
title Instalador TFT AI Overlay Pro
echo ==========================================
echo   TFT AI OVERLAY PRO - Instalador Automatico
echo ==========================================
echo.

:: 1. Verificar Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [!] Python nao encontrado. Baixando instalador...
    curl -o python_installer.exe https://www.python.org/ftp/python/3.11.9/python-3.11.9-amd64.exe
    echo [*] Por favor, instale o Python marcando 'Add to PATH' e reinicie este script.
    pause
    start python_installer.exe
    exit
)

echo [+] Python detectado!

:: 2. Instalar Dependências
echo [*] Instalando bibliotecas basicas...
pip install -r requirements.txt --quiet

:: 3. Tentar instalar PyAudio (Opcional)
echo [*] Tentando instalar suporte a Voz (PyAudio)...
pip install pipwin >nul 2>&1
pipwin install pyaudio >nul 2>&1
if %errorlevel% neq 0 (
    echo [!] PyAudio nao instalado (Opcional). O modo de voz pode nao funcionar.
) else (
    echo [+] PyAudio instalado com sucesso!
)

:: 4. Configurar Chaves
echo [*] Abrindo configuracao das chaves...
python config_gui.py
if %errorlevel% neq 0 (
    echo [ERRO] Falha na configuracao.
    pause
    exit
)

:: 5. Baixar Ícone Aleatório de Campeão
echo [*] Gerando icone aleatorio do campeao...
python -c "import requests, os; url='https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/default/v1/champion-icons/'+str(__import__('random').randint(1,150))+'.png'; r=requests.get(url); open('icon.png','wb').write(r.content)"

:: 6. Criar Atalho com Ícone Personalizado
echo [+] Criando atalho na Area de Trabalho com icone unico...
powershell "$WshShell = New-Object -comObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut('%USERPROFILE%\Desktop\TFT Overlay Pro.lnk'); $Shortcut.TargetPath = '%cd%\run_game.bat'; $Shortcut.WorkingDirectory = '%cd%'; $Shortcut.IconLocation = '%cd%\icon.png'; $Shortcut.Save()"

echo.
echo ==========================================
echo   INSTALACAO CONCLUIDA COM SUCESSO!
echo   Seu icone do campeao foi gerado!
echo   Va para a Area de Trabalho e clique em 'TFT Overlay Pro'
echo ==========================================
pause
