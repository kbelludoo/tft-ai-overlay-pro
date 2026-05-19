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

echo [*] Configurando suporte a Voz (Audio)...
echo [LOG] Tentando instalar drivers de audio... >> %LOG_FILE%

:: Tentativa 1: Instalar PyAudio binário direto (funciona na maioria dos Windows)
echo [LOG] Tentativa 1: PyAudio wheel... >> %LOG_FILE%
pip install PyAudio --prefer-binary >> %LOG_FILE% 2>&1
if %errorlevel% equ 0 (
    echo [+] PyAudio instalado com sucesso!
    echo [LOG] PyAudio instalado. >> %LOG_FILE%
    goto AUDIO_DONE
)

:: Tentativa 2: Instalar SoundDevice (Alternativa moderna e leve)
echo [AVISO] PyAudio falhou. Tentando alternativa (SoundDevice)... >> %LOG_FILE%
pip install sounddevice soundfile >> %LOG_FILE% 2>&1
if %errorlevel% equ 0 (
    echo [+] Alternativa SoundDevice instalada! O modo de voz funcionará.
    echo [LOG] SoundDevice instalado como fallback. >> %LOG_FILE%
    goto AUDIO_DONE
)

:: Falha Total
echo [ERRO] Nao foi possivel instalar nenhum driver de audio. >> %LOG_FILE%
echo [!] Aviso: O modo de voz ficara desativado nesta instalacao.
echo [!] Para corrigir manualmente depois, abra o CMD e digite: pip install PyAudio --prefer-binary
goto AUDIO_DONE

:AUDIO_DONE
echo.

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
