from flask import Blueprint

from controllers.UserController import index, signup, show, update, destroy

user = Blueprint('user', __name__)

user.route('/', methods=['GET'])(index)
user.route('/signup', methods=['POST'])(signup)
user.route('/<int:user_id>', methods=['GET'])(show)
user.route('/<int:user_id>/edit', methods=['POST'])(update)
user.route('/<int:user_id>', methods=['DELETE'])(destroy)
