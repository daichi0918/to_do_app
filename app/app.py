from flask import Flask,render_template,request
from models.models import YarukotoList
from models.database import db_session
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

@app.route("/add",methods=["post"])
def add():
    title = request.form["title"]
    body = request.form["body"]
    content = YarukotoList(title,body)
    db_session.add(content)
    db_session.commit()
    return index()

@app.route("/delete",methods=["post"])
def delete():
    id_list = request.form.getlist("delete")
    for id in id_list:
        content =YarukotoList.query.filter_by(id=id).first()
        db_session.delete(content)
    db_session.commit()
    return index()

if __name__ == "__main__":
    app.run(debug=True)
