@echo off

rem ----------------------------------------------------------------------------
rem
rem Launch for CLI with python runtime
rem
rem ----------------------------------------------------------------------------

setlocal

set THISDIR=%~dp0

if exist %THISDIR%\venv\ (
    pushd %THISDIR%\
        call "%THISDIR%\venv\Scripts\activate.bat"
        python deconvert_main.py "%~f1"
    popd
)

endlocal
