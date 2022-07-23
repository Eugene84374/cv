from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/picorp')
def applink():
    return render_template("picorp.html") 


if __name__ == "__main__":
    app.run()
