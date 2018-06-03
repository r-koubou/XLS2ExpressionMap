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
        python convert_gui_main.py
    popd
)

endlocal
