from flask import Flask,render_template,request
from models.models import YarukotoList
app = Flask(__name__)


@app.route("/")
@app.route("/index")
def index():
    name = request.args.get("name")
    all_yarukoto = YarukotoList.query.all()
    return render_template("index.html",name=name,all_yarukoto=all_yarukoto)


@app.route("/index",methods=["post"])
def post():
    name = request.form["name"]
    all_yarukoto = YarukotoList.query.all()
    return render_template("index.html",name=name,all_yarukoto=all_yarukoto)



if __name__ == "__main__":
    app.run(debug=True)
