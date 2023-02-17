from flask import Blueprint

from controllers.EventController import index

event = Blueprint('event', __name__)

event.route('/', methods=['GET'])(index)