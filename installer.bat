@echo off
color 0A
title Instalador TFT AI Overlay Pro - KbElLuDoO
set LOG_FILE=install_log.txt

:: Limpa log anterior e inicia novo
echo ========================================== > %LOG_FILE%
echo   LOG DE INSTALACAO - %DATE% %TIME% >> %LOG_FILE%
echo ========================================== >> %LOG_FILE%

echo Iniciando instalacao... Aguarde.
echo [LOG] Iniciando processo de instalacao... >> %LOG_FILE%

:: 1. Verificar Python
echo [*] Verificando Python...
python --version >> %LOG_FILE% 2>&1
if %errorlevel% neq 0 (
    echo [ERRO] Python nao encontrado! >> %LOG_FILE%
    echo [!] Python nao detectado. Por favor, instale o Python 3.10+ marcando 'Add to PATH'.
    echo [!] Veja o log em install_log.txt para detalhes.
    pause
    exit /b 1
)
echo [+] Python detectado. >> %LOG_FILE%

:: 2. Instalar Dependências Principais
echo [*] Instalando bibliotecas principais...
echo [LOG] Iniciando pip install... >> %LOG_FILE%
pip install -r requirements.txt >> %LOG_FILE% 2>&1
if %errorlevel% neq 0 (
    echo [ERRO] Falha ao instalar bibliotecas principais. >> %LOG_FILE%
    echo [!] Erro ao instalar dependencias. Verifique o arquivo install_log.txt.
    pause
    exit /b 1
)
echo [+] Bibliotecas principais instaladas. >> %LOG_FILE%

:: 3. Tentar Instalar PyAudio (Com tratamento de erro robusto)
echo [*] Tentando instalar suporte a Voz (PyAudio)...
echo [LOG] Tentando instalar PyAudio... >> %LOG_FILE%

:: Tenta usar o módulo python diretamente
python -c "import pipwin; pipwin.install('pyaudio')" >> %LOG_FILE% 2>&1
if %errorlevel% neq 0 (
    echo [AVISO] Falha na instalacao automatica do PyAudio. >> %LOG_FILE%
    echo [!] Nao foi possivel instalar PyAudio automaticamente.
    echo [!] O modo de voz ficara desativado, mas o jogo funcionara.
    echo [!] Para tentar corrigir manualmente depois, rode: python -m pipwin install pyaudio
) else (
    echo [+] PyAudio instalado com sucesso! >> %LOG_FILE%
)

:: 4. Rodar Configuração GUI
echo [*] Abrindo configuracao das chaves...
echo [LOG] Iniciando config_gui.py... >> %LOG_FILE%
start /wait python config_gui.py >> %LOG_FILE% 2>&1

if %errorlevel% neq 0 (
    echo [ERRO] Falha ao abrir configuracao ou usuario cancelou. >> %LOG_FILE%
    echo [!] Erro na configuracao inicial. Verifique install_log.txt.
    pause
    exit /b 1
)

:: 5. Criar Atalho
echo [*] Criando atalho na Area de Trabalho...
echo [LOG] Criando atalho... >> %LOG_FILE%
powershell "$WshShell = New-Object -comObject WScript.Shell; $Shortcut = $WshShell.CreateShortcut('%USERPROFILE%\Desktop\TFT Overlay Pro.lnk'); $Shortcut.TargetPath = '%cd%\run_game.bat'; $Shortcut.WorkingDirectory = '%cd%'; $Shortcut.Save()" >> %LOG_FILE% 2>&1

echo.
echo ==========================================
echo   INSTALACAO CONCLUIDA!
echo   Um atalho foi criado na sua Area de Trabalho.
echo   Se houve erros, veja o arquivo: install_log.txt
echo ==========================================
echo [LOG] Instalacao concluida com sucesso. >> %LOG_FILE%
pause
