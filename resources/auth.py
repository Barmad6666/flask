from flask import request, render_template, make_response
from flask_restful import Resource
from flask_jwt_extended import create_access_token
from forms.auth import Register
from models.user import UserModel


class Signup(Resource):
    def get():
        return make_response(render_template("signup.html"), 200, {"Content-Type": "text/html"})
    def post(self):
        r=request.form
        validator= Register(r)
        if validator.validate():
            model = UserModel(r)
            if model.Exists():
                return {"status":"error","messages": "User already exists" },400
            else:
                if r["job"]=="seller":
                    if not model.SignupValidate(r["password"],r["repeat_password"],r["email"],r["phone"],r["address"]):
                        return {"status":"error","messages": "Invalid input data1" },400
                    else:
                        model.Save(e=r["email"],p=r["phone"],a=r["address"])
                        return {"status":"success","messages": "User Registered successfully" },200
                elif r["job"]=="buyer":
                    model.Save()
                    return {"status":"success","messages": "User Registered successfully" },200
                else:
                    if not model.SignupValidate(r["password"],r["repeat_password"],r["email"],r["phone"],a_s_p=r["special_password"]):
                        return {"status":"error","messages": "Invalid input data2" },400
                    else:
                        model.Save(e=r["email"],p=r["phone"],a_s_p=r["special_password"])
                        return {"status":"success","messages": "User Registered successfully" },200
        else:
            return {"status":"error","messages": validator.errors}, 400

class Login(Resource):
    def post(self):
        validator= Register(request.form)
        if validator.validate():
            model = UserModel(request.form)
            if model.LoginValidate():
                return {"status":"success","messages": "User logged in successfully", "token": create_access_token(model.username+"_"+model.job,expires_delta=False) },200
            else:
                return {"status":"error","messages": "Invalid username or password" },401
        else:
            return {"status":"error","messages": validator.errors}, 400

