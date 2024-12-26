from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.product import ProductModel
from forms.product import ProductForm

class Product(Resource):
    @jwt_required()
    def post(self):
        ProductValidator = ProductForm(request.form)
        if ProductValidator.validate():
            username,job=get_jwt_identity().split("_")
            model = ProductModel(request.form, username, job)
            if model.exists():
                return {'message': 'Product already exists!'}, 400
            if model.job== 'buyer':
                return {'message': "buyer can't create products!"}, 401
            model.create()
            return {'message': 'Product created successfully!'}, 201
        else:
            return {'message': 'Product creation failed!'}, 400
        