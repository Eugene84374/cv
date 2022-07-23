from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("picorp.html")

@app.route('/picorp')
def applink():
    return "Hello World!"


if __name__ == "__main__":
    app.run()
