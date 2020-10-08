$env:FLASK_ENV = "development"
$env:FLASK_APP = "microbit_app"

cd webapp
flask init-db
cd ..