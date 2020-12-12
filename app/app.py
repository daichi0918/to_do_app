from flask import Flask,render_template,request

app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    name = request.args.get("name")
    yarukoto = ["プログラミング","卒論","美容院","ランニング"]
    return render_template("index.html",name=name,yarukoto=yarukoto)


@app.route("/index",methods=["post"])
def post():
    name = request.form["name"]
    yarukoto = ["プログラミング","卒論","美容院","ランニング"]
    return render_template("index.html",name=name,yarukoto=yarukoto)



if __name__ == "__main__":
    app.run(debug=True)
