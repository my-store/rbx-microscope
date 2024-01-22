@ECHO OFF

ECHO:

ECHO ==============================================
ECHO RBX DIGITAL MICROSCOPE V1.0
ECHO ==============================================
ECHO Creator    : Izzat Alharis
ECHO Created at : Jan 12 2024

ECHO:

TIMEOUT 1 > NUL

@REM ACTIVATE THE VIRTUAL ENVIRONMENT
call .\virt\Scripts\activate.bat
ECHO Virtual environment is activated

TIMEOUT 1 > NUL

@REM EM RUN THE PROGRAM
py app.py

ECHO:

ECHO Closing the app

TIMEOUT 3 > NUL