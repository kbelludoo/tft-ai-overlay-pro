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
echo [*] Configurando suporte a Voz (PyAudio)...
:: Tenta instalar usando o modulo Python diretamente, sem depender do comando pipwin
python -c "import pipwin; pipwin.install('pyaudio')" 2>nul
if %errorlevel% neq 0 (
    echo [!] Nao foi possivel instalar PyAudio automaticamente (Comum no Windows).
    echo [!] O modo de voz ficara desativado, mas o resto do app funcionara perfeitamente.
    echo [!] Dica: Se quiser voz, instale manualmente: pip install pipwin ^&^& pipwin install pyaudio
) else (
    echo [+] Suporte a voz instalado com sucesso!
)
echo.
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
