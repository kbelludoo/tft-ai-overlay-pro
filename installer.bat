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
    echo [!] Python nao encontrado!
    echo [*] Baixando instalador do Python...
    curl -o python_installer.exe https://www.python.org/ftp/python/3.11.9/python-3.11.9-amd64.exe
    echo [*] INSTALE O PYTHON MARCANDO A CAIXA "Add Python to PATH" e depois rode este arquivo novamente.
    pause
    start python_installer.exe
    exit
)

echo [+] Python detectado!
echo [*] Instalando bibliotecas basicas...
pip install --upgrade pip
pip install -r requirements.txt

:: 2. Tentar instalar PyAudio (Pode falhar, mas nao para o script)
echo [*] Tentando instalar suporte a Voz (PyAudio)...
pip install pipwin
pipwin install pyaudio
if %errorlevel% neq 0 (
    echo [!] Nao foi possivel instalar PyAudio automaticamente.
    echo [!] O modo de voz pode nao funcionar, mas o resto do app funcionara.
)

echo.
echo [*] Abrindo configuracao das chaves...
python config_gui.py
if %errorlevel% neq 0 (
    echo [ERRO] Falha na configuracao. Verifique se preencheu as chaves.
    pause
    exit
)

echo.
echo [+] Criando atalho na Area de Trabalho...
powershell "$WshShell = New-Object -comObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut('%USERPROFILE%\Desktop\TFT Overlay Pro.lnk'); $Shortcut.TargetPath = '%cd%\run_game.bat'; $Shortcut.WorkingDirectory = '%cd%'; $Shortcut.Save()"

echo.
echo ==========================================
echo   INSTALACAO CONCLUIDA!
echo   Va para a Area de Trabalho e clique em 'TFT Overlay Pro'
echo ==========================================
pause
