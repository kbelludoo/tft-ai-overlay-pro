@echo off
color 0A
title Instalador TFT AI Overlay Pro - KbElLuDoO
set LOG_FILE=install_log.txt

echo ========================================== > %LOG_FILE%
echo   LOG DE INSTALACAO - %DATE% %TIME% >> %LOG_FILE%
echo ========================================== >> %LOG_FILE%

echo Iniciando instalacao... Aguarde.
echo [LOG] Iniciando processo de instalacao... >> %LOG_FILE%

:: 1. Verificar Python
python --version >> %LOG_FILE% 2>&1
if %errorlevel% neq 0 (
    echo [ERRO] Python nao encontrado! Instale o Python 3.10+ marcando 'Add to PATH'.
    pause
    exit /b 1
)
echo [+] Python detectado. >> %LOG_FILE%

:: 2. Instalar Dependências Principais
echo [*] Instalando bibliotecas principais...
pip install -r requirements.txt >> %LOG_FILE% 2>&1
if %errorlevel% neq 0 (
    echo [ERRO] Falha critica nas bibliotecas principais. Verifique install_log.txt.
    pause
    exit /b 1
)
echo [+] Bibliotecas principais instaladas. >> %LOG_FILE%

:: 3. Tentar PyAudio (Método Alternativo Seguro)
echo [*] Tentando configurar audio (Opcional)...
:: Tenta instalar direto via pip primeiro (mais seguro no Python 3.14)
pip install pyaudio >> %LOG_FILE% 2>&1
if %errorlevel% neq 0 (
    echo [AVISO] PyAudio nao instalado automaticamente. Modo de voz desativado. >> %LOG_FILE%
    echo [!] Audio nao configurado (Comum no Windows). O jogo funcionara sem voz.
) else (
    echo [+] Audio configurado com sucesso! >> %LOG_FILE%
)

:: 4. Rodar Configuração GUI
echo [*] Abrindo configuracao das chaves...
start /wait python config_gui.py
if %errorlevel% neq 0 (
    echo [ERRO] Configuracao cancelada ou falhou. >> %LOG_FILE%
    pause
    exit /b 1
)

:: 5. Criar Atalho
echo [*] Criando atalho na Area de Trabalho...
powershell "$WshShell = New-Object -comObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut('%USERPROFILE%\Desktop\TFT Overlay Pro.lnk'); $Shortcut.TargetPath = '%cd%\run_game.bat'; $Shortcut.WorkingDirectory = '%cd%'; $Shortcut.Save()"

echo.
echo ==========================================
echo   INSTALACAO CONCLUIDA!
echo   Va para a Area de Trabalho e clique no icone.
echo   Se houver problemas, veja o arquivo: error_log.txt na pasta do jogo.
echo ==========================================
pause
