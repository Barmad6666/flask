from flask import Flask
from flask_restful import Api
from resources.auth import Signup, Login
from resources.todo import Todo
import config
from flask_jwt_extended import JWTManager
from resources.product import Product
def main():
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(Signup,"/api/signup")
    api.add_resource(Login,"/api/login")
    api.add_resource(Todo,"/api/todo")
    api.add_resource(Product,"/api/product")
    app.config["JWT_SECRET_KEY"]= config.Secret_Key
    JWTManager(app)
    app.run(debug=True)
if __name__=="__main__":
    main()