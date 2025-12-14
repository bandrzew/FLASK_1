from flask import Flask, request, render_template

app = Flask(__name__)


# @app.route("/", methods=["GET", "POST"])
@app.route("/")
def home():
    return "dupa"


if __name__ == "__main__":
    app.run(debug=True, port=5555)
