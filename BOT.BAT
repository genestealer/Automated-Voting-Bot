@echo off
setlocal enabledelayedexpansion

:loop
set "psiphonRunning="
for /f "tokens=*" %%i in ('tasklist /NH /FI "IMAGENAME eq psiphon3.exe"') do (
    set "psiphonRunning=1"
    taskkill /T /F /IM psiphon3.exe
)

for /f "tokens=*" %%i in ('tasklist /NH /FI "IMAGENAME eq psiphon-tunnel-core.exe"') do (
    set "psiphonRunning=1"
    taskkill /T /F /IM psiphon-tunnel-core.exe
)

set "firefoxRunning="
for /f "tokens=*" %%i in ('tasklist /NH /FI "IMAGENAME eq firefox.exe"') do (
    set "firefoxRunning=1"
    taskkill /T /F /IM firefox.exe
)

if defined psiphonRunning (
    echo "Closing Psiphon..."
    timeout /t 5 /nobreak
    taskkill /F /IM psiphon3.exe
    taskkill /F /IM psiphon-tunnel-core.exe
) else (
    echo "Psiphon is not running."
)

if defined firefoxRunning (
    echo "Closing Firefox..."
    timeout /t 5 /nobreak
    taskkill /F /IM firefox.exe
) else (
    echo "Firefox is not running."
)

echo "STARTING..."
start psiphon3.exe
timeout /t 6 /nobreak

echo "[!] Starting the Voting process..."
python vote.py
timeout /t 3 /nobreak

echo "[+] Voting done."

timeout /t 3 /nobreak

echo " Killing the VPN..."
taskkill /T /F /IM psiphon3.exe
taskkill /T /F /IM psiphon-tunnel-core.exe

goto loop
