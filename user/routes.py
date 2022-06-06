from flask import Blueprint, jsonify
from models import db, User

user_blueprint = Blueprint('user_api_routes', __name__, url_prefix='/api/user')


@user_blueprint.route('/all', methods=['GET'])
def get_all_users():
    # TODO: dandle errors properly
    all_user = User.query.all()
    result = [user.serialize() for user in all_user]
    response = {
        "message": "Returning all users",
        "result": result
    }
    return jsonify(response)


@user_blueprint.route('/', methods=['GET'])
def index():
    return "<h1>Hello</h1>"
