from db import Database
import hashlib
class UserModel():
    def __init__(self, data:dict[str,str]):
        self.username=data["username"]
        self.password=hashlib.md5(data["password"].encode()).hexdigest()
        self.db=Database()
        self.job=data["job"]
    def Save(self,e=False,p=False,a=False,a_s_p=False):
        self.db.insert_user(self.username,self.password,self.job,e,p,a,a_s_p)
    def SignupValidate(self,p1,p2,email=False,phone=False,address=False,a_s_p=False):
        if p1==p2:
            if self.job=="buyer":
                return True
            elif self.job=="seller":
                if email and phone and address:
                    return True
            elif self.job=="admin":
                if email and phone and a_s_p :
                    return True
        return False
    def LoginValidate(self):
        result=self.db.find_user(self.username)
        if result:
            if result["password"]==self.password and result["job"]==self.job :
                return True
            return False
        return False
    def Exists(self):
        result=self.db.find_user(self.username)
        if result:
            return True
        return False

