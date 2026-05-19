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
    echo [!] Python nao encontrado. Baixando instalador...
    curl -o python_installer.exe https://www.python.org/ftp/python/3.11.9/python-3.11.9-amd64.exe
    echo [*] Por favor, instale o Python marcando 'Add to PATH' e reinicie este script.
    pause
    start python_installer.exe
    exit
)

echo [+] Python detectado!
echo [*] Instalando dependencias...
pip install -r requirements.txt --quiet

echo [*] Configurando chaves de API...
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
echo   INSTALACAO CONCLUIDA COM SUCESSO!
echo   Va para a Area de Trabalho e clique em 'TFT Overlay Pro'
echo ==========================================
pause