@echo off

REM Install Python
echo Installing Python...
curl https://www.python.org/ftp/python/3.11.4/python-3.11.4-amd64.exe -o python_installer.exe
python_installer.exe /quiet InstallAllUsers=1 PrependPath=1

REM Install required modules
echo Installing required modules...
pip install webbrowser
pip install random
pip install time
pip install pyautogui
pip install ctypes
pip install winsound
pip install requests
pip install pillow
pip install io
pip install subprocess
pip install flask

REM Install pyinstaller
echo Installing pyinstaller...
pip install pyinstaller

REM Build the executable
echo Building the executable...
pyinstaller --hidden-import webbrowser --hidden-import random --hidden-import time --hidden-import pyautogui --hidden-import ctypes --hidden-import winsound --hidden-import requests --hidden-import PIL --hidden-import io --hidden-import subprocess --hidden-import flask --add-data "templates/index.html;templates/" main.py

REM Prompt the user to run the generated file
set /p run_exe=Do you want to run the generated file? (y/n): 

REM Check the user's response
IF /I "%run_exe%"=="y" (
    REM Run the generated file
    start "" /b "dist\main\main.exe"
) ELSE (
    REM Exit the script
    exit
)

pause
