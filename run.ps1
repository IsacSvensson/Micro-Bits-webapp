cd webapp
start-process -WindowStyle hidden python "..\microbit-module\main.py"
start-process -WindowStyle hidden python "..\websocket\websocket.py"
Start-Process -WindowStyle hidden PowerShell -ArgumentList 'flask run --host=0.0.0.0'

$title   = 'Microbit Monitoring Web app is running'
$msg     = 'Do you want to turn off the app?'
$options = '&Yes', '&No'
$default = 1  # 0=Yes, 1=No
$ran = 0

do {
    if ($ran -eq 0) {
        $response = $Host.UI.PromptForChoice($title, $msg, $options, $default)
        $ran = 1
    }
    else {
        $response = Read-Host
        $response = $response.toLower()
    }
} until ($response -eq 0 -or $response -eq 'y')

Stop-Process -name python
cd ..