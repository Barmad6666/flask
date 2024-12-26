from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.todo import TodoModel
from forms.todo import  TodoForm

class Todo(Resource):

    @jwt_required()
    def post(self):
        todoValidator = TodoForm(request.form)
        if todoValidator.validate():
            user = get_jwt_identity()
            model = TodoModel(request.form,user)
            model.create()
            return {"message": "Todo created successfully."}, 201
        else:
            return {"status": "error", "message": todoValidator.errors}, 400