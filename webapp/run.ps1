$env:FLASK_APP = "microbit_app"
$env:FLASK_ENV = "development" 
start-process python "..\microbit-module\main.py"
start-process python "..\websocket\websocket.py"

flask run --host=0.0.0.0