from app import app
from flask import Blueprint

from app.routes.add_routes import add
from app.routes.minute_route import minute

app.register_blueprint(add)
app.register_blueprint(minute)