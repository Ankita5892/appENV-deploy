from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():

    return "Hello-Github, today 30-11-2021"



if __name__ == "__main__":
    app.run()

