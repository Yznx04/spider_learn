import random

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = \
    "mysql+pymysql://root:420420@localhost:3306/flask"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class User(db.Model):
    uid = db.Column(db.INTEGER, primary_key=True)
    uname = db.Column(db.String(20), unique=False, nullable=False)
    uemail = db.Column(db.String(40), unique=False, nullable=True)


@app.route("/a/")
def create():
    db.create_all()
    return "<h1>创建数据库成功</h1>"


@app.route('/insert')
def add_user():
    user = User()
    name = "我将有{}个女朋友".format(random.randint(0, 50))
    user.uname = name
    db.session.add(user)
    db.session.commit()
    return "<h1>add sucessful </h1>"


@app.route('/find')
def find_user():
    user = User.query.all()
    for u in user:
        print(u.uname)
    return "ok"


if __name__ == '__main__':
    app.run(debug=True)
