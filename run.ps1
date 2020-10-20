$title1   = 'Microbit Monitoring Web app is starting'
$msg1     = 'Do you want to display web-app, microbit-module and websocket server?'
$options = '&Yes', '&No'
$default = 1  # 0=Yes, 1=No
$ran = 0

$env:FLASK_ENV = "development"
$env:FLASK_APP = "microbit_app"
$env:FLASK_DEBUG = "true"

do {
    if ($ran -eq 0) {
        $response = $Host.UI.PromptForChoice($title1, $msg1, $options, $default)
        $ran = 1
    }
    else {
        $response = Read-Host
        $response = $response.toLower()
    }
} until (($response -eq 0 -or $response -eq 'y') -or ($response -eq 1 -or $response -eq 'n'))

cd webapp
if ($response -eq 1 -or $response -eq 'n') {
    start-process -WindowStyle hidden python "..\microbit-module\main.py"
    start-process -WindowStyle hidden python "..\websocket\websocket.py"
    Start-Process -WindowStyle hidden PowerShell -ArgumentList "waitress-serve --port=5000 --call 'microbit_app:create_app'"
}
else{
    start-process python "..\microbit-module\main.py"
    start-process python "..\websocket\websocket.py"
    Start-Process PowerShell -ArgumentList "waitress-serve --port=5000 --call 'microbit_app:create_app'"
}
$title2   = 'Microbit Monitoring Web app is running'
$msg2     = 'Do you want to turn off the app?'
$ran = 0

Write-Host "`n===================================================================`n==================================================================="

do {
    if ($ran -eq 0) {
        $response = $Host.UI.PromptForChoice($title2, $msg2, $options, $default)
        $ran = 1
    }
    else {
        $response = Read-Host
        $response = $response.toLower()
    }
} until ($response -eq 0 -or $response -eq 'y')

Stop-Process -name python
cd ..