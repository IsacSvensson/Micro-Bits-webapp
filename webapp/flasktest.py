from flask import Flask

app = Flask(__name__)

@app.route("/<testa>")
def test(testa):
    return 'Hello! You wrote \"%s\"' % testa
app.run()

print("test")