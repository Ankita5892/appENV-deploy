from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():

    return "Hello-Github-demo1, this is Github Action demo"



if __name__ == "__main__":
    app.run()

