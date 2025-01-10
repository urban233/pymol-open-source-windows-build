@echo off

:: Define the path to the magick.exe
set MAGICK_PATH=%~dp0..\..\vendor\magick\bin\magick.exe

:: Check if magick.exe exists
if not exist "%MAGICK_PATH%" (
    echo magick.exe not found at "%MAGICK_PATH%". Exiting...
    exit /b 1
)

:: Resize logo.png into multiple sizes
"%MAGICK_PATH%" "%~dp0..\..\alternative_design\convert_to_ico\logo.png" -background none -resize 256x256 "%~dp0..\..\alternative_design\convert_to_ico\logo-256.png"
"%MAGICK_PATH%" "%~dp0..\..\alternative_design\convert_to_ico\logo.png" -background none -resize 128x128 "%~dp0..\..\alternative_design\convert_to_ico\logo-128.png"
"%MAGICK_PATH%" "%~dp0..\..\alternative_design\convert_to_ico\logo.png" -background none -resize 64x64 "%~dp0..\..\alternative_design\convert_to_ico\logo-64.png"
"%MAGICK_PATH%" "%~dp0..\..\alternative_design\convert_to_ico\logo.png" -background none -resize 48x48 "%~dp0..\..\alternative_design\convert_to_ico\logo-48.png"
"%MAGICK_PATH%" "%~dp0..\..\alternative_design\convert_to_ico\logo.png" -background none -resize 32x32 "%~dp0..\..\alternative_design\convert_to_ico\logo-32.png"
"%MAGICK_PATH%" "%~dp0..\..\alternative_design\convert_to_ico\logo.png" -background none -resize 16x16 "%~dp0..\..\alternative_design\convert_to_ico\logo-16.png"

:: Combine all resized images into an .ico file
"%MAGICK_PATH%" "%~dp0..\..\alternative_design\convert_to_ico\logo-256.png" "%~dp0..\..\alternative_design\convert_to_ico\logo-128.png" "%~dp0..\..\alternative_design\convert_to_ico\logo-64.png" "%~dp0..\..\alternative_design\convert_to_ico\logo-48.png" "%~dp0..\..\alternative_design\convert_to_ico\logo-32.png" "%~dp0..\..\alternative_design\convert_to_ico\logo-16.png" "%~dp0..\..\alternative_design\convert_to_ico\logo.ico"

:: Indicate completion
echo Icon creation complete. Saved as "%~dp0..\..\alternative_design\convert_to_ico\logo.ico".
