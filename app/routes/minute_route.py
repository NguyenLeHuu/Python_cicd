# app/routes/add_routes.py
from flask import request
from app import minute
from app.controllers.minute_controller import minute_process

@minute.route('/minute', methods=['POST', 'GET'] )
def minute_handler():
    return minute_process(request)
