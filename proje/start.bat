@echo off
set "sourceFolder=%~dp0"
set "exeName=main.exe"
set "startupFolder=%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup"

echo Klasor: %sourceFolder%
echo Uygulama Adi: %exeName%
echo Baslangic Klasoru: %startupFolder%

copy "%sourceFolder%%exeName%" "%startupFolder%"

echo %exeName% dosyasi baslangic klasorune tasindi.
echo Sifreyi olusturduktan sonra programi hatasiz kullanabilirsiniz.

set /p "restartChoice= Bilgisayari simdi yeniden baslatmak ister misiniz? (e / h): "
if /i "%restartChoice%"=="e" (
    shutdown /r /t 0
) else (
    echo Programin duzgun calisabilmesi icin bilgisayari yeniden baslatin.
)

pause
