@echo off
color 0A
title Instalador TFT AI Overlay Pro
echo ==========================================
echo   TFT AI OVERLAY PRO - Instalador Automatico
echo ==========================================
echo.

:: Verificar Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [!] Python nao encontrado. Por favor, instale o Python 3.11+ marcando 'Add to PATH'.
    pause
    exit
)

echo [+] Python detectado!
echo [*] Instalando bibliotecas basicas...
pip install -r requirements.txt

:: Tentar instalar PyAudio separadamente, mas nao falhar se der erro
echo [*] Tentando instalar suporte a Voz (PyAudio)...
pip install pipwin
pipwin install pyaudio || echo [!] PyAudio nao instalado (Opcional). O modo de voz pode nao funcionar.

echo.
echo [*] Abrindo configuracao das chaves...
python config_gui.py

if %errorlevel% neq 0 (
    echo [ERRO] Falha na configuracao. Tente executar 'python config_gui.py' manualmente.
    pause
    exit
)

echo.
echo [+] Criando atalho na Area de Trabalho...
powershell "$WshShell = New-Object -comObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut('%USERPROFILE%\Desktop\TFT Overlay Pro.lnk'); $Shortcut.TargetPath = '%cd%\run_game.bat'; $Shortcut.WorkingDirectory = '%cd%'; $Shortcut.Save()"

echo.
echo ==========================================
echo   INSTALACAO CONCLUIDA COM SUCESSO!
echo ==========================================
pause
