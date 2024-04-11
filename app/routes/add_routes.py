# app/routes/add_routes.py
from flask import request
from app import add
from app.controllers.add_controller import add_process

@add.route('/add', methods=['POST', 'GET'] )
def add_handler():
    return add_process(request)
