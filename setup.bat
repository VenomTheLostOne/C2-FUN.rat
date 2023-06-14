@echo off

REM Install pyinstaller
pip install pyinstaller

REM Build the executable
pyinstaller --hidden-import webbrowser --hidden-import random --hidden-import time --hidden-import pyautogui --hidden-import ctypes --hidden-import winsound --hidden-import requests --hidden-import PIL --hidden-import io --hidden-import subprocess --hidden-import flask --add-data "templates/index.html;templates/" main.py

REM Prompt the user to run the generated file
set /p run_exe=Do you want to run the generated file? (y/n): 

REM Check the user's response
IF /I "%run_exe%"=="y" (
    REM Run the generated file
    start "" /b "dist\main.exe"
) ELSE (
    REM Exit the script
    exit
)

pause
