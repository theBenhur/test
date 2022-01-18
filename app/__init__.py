from flask import Flask

app=Flask(__name__)

from app.blueprints.auth import auth
app.register_blueprint(app)