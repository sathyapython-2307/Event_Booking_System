from flask import Flask
from app.routes import register_routes

app = Flask(__name__)
app.secret_key = "secret"
register_routes(app)
