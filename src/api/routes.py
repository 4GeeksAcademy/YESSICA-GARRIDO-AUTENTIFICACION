"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User
from api.utils import generate_sitemap, APIException
from flask_cors import CORS
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

api = Blueprint('api', __name__)

# Allow CORS requests to this API
CORS(api)


@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():

    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }

    return jsonify(response_body), 200


@api.route('/registre', methods=['POST'])
def registre():

    email = request.json.get("email")
    password = request.json.get("password")
    if not email or not password:
        return jsonify({"msg": "se requere de un email y de un password"})
    user = User.query.filter_by(email=email).first()
    if user:
        return jsonify({"msg": "usuario ya existente!"})
    new_user = User(email=email, is_active=True)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"msg": "nuevo usuario creado"}), 201


@api.route('/login', methods=['POST'])
def login():

    email = request.json.get("email")
    password = request.json.get("password")
    
    user = User.query.filter_by(email=email).first()
    if not user or not user.check_password(password):
        return jsonify({"msg":"usuario no encontrado"})
    accesso_token=create_access_token(identity=str(user.id))

    return jsonify({"token": accesso_token, "user.id": user.id}), 201

@api.route('/private', methods=['GET'])
@jwt_required()
def private():

    current_user=get_jwt_identity()
    user=User.query.get(current_user)
    if not user:
        return jsonify({"msg":"Usuario no existe en mi base de datos!"})
    return jsonify({"msg" :"Usuario encontrado","usuario": user.serialize()}), 200 