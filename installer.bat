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
    echo [!] Python nao encontrado. Por favor, instale o Python 3.10+ marcando 'Add to PATH'.
    pause
    start https://www.python.org/downloads/
    exit
)

echo [+] Python detectado!
echo [*] Instalando bibliotecas basicas...
pip install -r requirements.txt --quiet

:: 2. Tentar instalar PyAudio (Opcional, ignora falhas)
echo [*] Tentando instalar suporte a Voz (PyAudio)...
pip install pipwin --quiet >nul 2>&1
pipwin install pyaudio --quiet >nul 2>&1
if %errorlevel% neq 0 (
    echo [!] PyAudio nao instalado (Opcional). O modo de voz pode nao funcionar.
) else (
    echo [+] PyAudio instalado com sucesso!
)

:: 3. Configurar Chaves
echo [*] Abrindo configuracao das chaves...
python config_gui.py
if %errorlevel% neq 0 (
    echo [ERRO] Falha na configuracao.
    pause
    exit
)

:: 4. Criar Atalho com Ícone Aleatório Embutido
echo.
echo [+] Criando atalho na Area de Trabalho com icone aleatorio...

:: Script Python para gerar o atalho com ícone embutido
powershell -Command "Invoke-Expression -Command (Get-Content -Raw '%~dp0create_shortcut.py')"

if exist "%USERPROFILE%\Desktop\TFT Overlay Pro.lnk" (
    echo [+] Atalho criado com sucesso!
) else (
    echo [!] Nao foi possivel criar o atalho automaticamente.
)

echo.
echo ==========================================
echo   INSTALACAO CONCLUIDA!
echo   Va para a Area de Trabalho e clique no icone do Campeao!
echo ==========================================
pause
