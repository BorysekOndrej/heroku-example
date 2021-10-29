from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/<name>")
def hello_there(name: str = "General Kenobi"):
    return f"<p>Hello there, {name}!</p>"

if __name__ == '__main__':
    app.run(threaded=True, port=5000)
