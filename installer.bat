@echo off
color 0A
title Instalador TFT AI Overlay Pro
echo ==========================================
echo   TFT AI OVERLAY PRO - Instalador Blindado
echo ==========================================
echo.

:: 1. Detectar Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [ERRO] Python nao encontrado!
    echo Por favor, instale o Python 3.10+ marcando 'Add to PATH'.
    pause
    exit
)
echo [+] Python detectado: 
python --version

:: 2. Instalar Dependências (Ignora erros leves)
echo [*] Instalando bibliotecas...
pip install -r requirements.txt --quiet --upgrade
if %errorlevel% neq 0 (
    echo [!] Aviso: Algumas bibliotecas podem ter falhado, tentando continuar...
)

:: 3. Tentar Instalar PyAudio (Opcional - Se falhar, nao para)
echo [*] Tentando instalar suporte a Voz (PyAudio)...
pip install pipwin --quiet
pipwin install pyaudio --quiet 2>nul
if %errorlevel% neq 0 (
    echo [!] PyAudio nao instalado (Normal em alguns PCs). O modo de voz sera desativado.
) else (
    echo [+] PyAudio instalado com sucesso!
)

:: 4. Baixar Ícone Aleatório (Com proteção de erro)
echo [*] Gerando icone aleatorio do campeao...
python -c "import requests, random, os; url=f'https://ddragon.leagueoflegends.com/cdn/img/champion/splash/{random.randint(1,160)}_0.jpg'; r=requests.get(url, timeout=5); open('icon_temp.jpg','wb').write(r.content); print('Icone baixado!')" 2>nul
if %errorlevel% neq 0 (
    echo [!] Falha ao baixar icone. Usando padrao...
    echo. > icon_temp.jpg
)

:: 5. Rodar Configuração Gráfica
echo [*] Abrindo configuracao das chaves...
start /wait python config_gui.py

if %errorlevel% neq 0 (
    echo [ERRO] Configuracao cancelada ou falhou.
    pause
    exit
)

:: 6. Criar Atalho na Área de Trabalho
echo [*] Criando atalho na Area de Trabalho...
set "DESKTOP=%USERPROFILE%\Desktop"
powershell "$WshShell = New-Object -comObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut('%DESKTOP%\TFT Overlay Pro.lnk'); $Shortcut.TargetPath = '%cd%\run_game.bat'; $Shortcut.WorkingDirectory = '%cd%'; $Shortcut.IconLocation = '%cd%\icon_temp.jpg'; $Shortcut.Save()"

echo.
echo ==========================================
echo   INSTALACAO CONCLUIDA!
echo   Verifique sua Area de Trabalho.
echo ==========================================
pause
