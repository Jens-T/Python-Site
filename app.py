from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/calculate", methods=["POST"])
def calculate():
    number = float(request.form["number"])
    result = number ** 2
    return f"Result: {result}"

if __name__ == "__main__":
    app.run()
