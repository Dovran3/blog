import mysql.connector
from . import app
from flask_login import LoginManager, UserMixin


db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="2606",
    database="mydb"
)

cursor = db.cursor()

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "/auth"


@login_manager.user_loader
def user_loader(username):
    user = UserMixin()
    user.id = username
    return user
