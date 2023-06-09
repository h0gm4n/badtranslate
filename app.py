from flask import Flask
from flask import render_template, request, redirect
from translator import BadTranslator

app = Flask(__name__)
bt = BadTranslator()

@app.route("/")
def index():

    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    iterations = request.form["iterations"]
    try:
        if not 1 <= int(iterations) <= 100:
            return(redirect("/"))
    except:
        return(redirect("/"))

    sentence = request.form["sentence"]

    tulos = bt.translate(sentence, int(iterations))
    return render_template("index.html", tulos=tulos, sentence=sentence, iterations=iterations)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)



