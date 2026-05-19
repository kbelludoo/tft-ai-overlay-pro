@echo off
title TFT AI Overlay Pro - KbElLuDoO
color 0B

:: Define o arquivo de log
set LOG_FILE=run_log.txt

:: Limpa o log anterior para começar fresco
echo ========================================== > %LOG_FILE%
echo   LOG DE EXECUCAO - %DATE% %TIME% >> %LOG_FILE%
echo ========================================== >> %LOG_FILE%
echo [INFO] Iniciando TFT AI Overlay Pro... >> %LOG_FILE%

:: Mensagem visual para o usuário
echo Carregando sistema... Aguarde.
echo Se esta janela fechar sozinha, verifique o arquivo "%LOG_FILE%" para ver o erro.
echo.

:: Executa o Python e redireciona TUDO (saída e erros) para o log
python main.py >> %LOG_FILE% 2>&1

:: Se o programa fechar inesperadamente (código de erro diferente de 0)
if %errorlevel% neq 0 (
    echo.
    echo [ERRO] O programa fechou inesperadamente!
    echo Por favor, abra o arquivo "%LOG_FILE%" e procure por "Traceback" ou "Error".
    echo.
    pause
) else (
    echo.
    echo [INFO] Programa encerrado normalmente.
    pause
)
