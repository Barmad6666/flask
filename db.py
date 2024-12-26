import config
class Database():
    def __init__(self) :
        self.mongo = config.Mongo_Client
        self.db = self.mongo["PROG1"]
        self.users = self.db["users"]
        self.todos = self.db["todos"]
        self.products = self.db["products"]
    def insert_user(self, username, password,j,e=None,p=None,a=None,a_s_p=None):
        self.users.insert_one({"username":username,"password":password,"job":j,"email":e,"phone":p,"address":a,"admin_special_password":a_s_p})
    def insert_todo(self, title, description, status, username):
        self.todos.insert_one({"title":title,"description":description,"status":status,"from":username})
    def find_user(self, username):
        return self.users.find_one({"username":username})
    def find_todos(self, username):
        return self.todos.find({"from":username})
    def update_todo(self, _id, title, description, status):
        self.todos.update_one({"_id":_id},{"$set":{"title":title,"description":description,"status":status}})
    def delete_todo(self, _id):
        self.todos.delete_one({"_id":_id})
    def delete_user(self, username):
        self.users.delete_one({"username":username})
    def delete_all_todos(self):
        self.todos.delete_many({})
    def update_password(self, username, password):
        self.users.update_one({"username":username},{"$set":{"password":password}})
    def update_username(self, old_username, new_username):
        self.users.update_one({"username":old_username},{"$set":{"username":new_username}})

    def insert_product(self, name,num_available,  price , weight ,description ,image_url ,category, id, username):
        self.products.insert_one({"name":name,"num_available":num_available,"price":price,"weight":weight,"description":description,"image_url":image_url,"category":category,"id":id,"from":username})
    def find_product(self, name):
        return self.products.find_one({"name":name})
    def find_products(self, username):
        return self.products.find({"from":username})
    def delete_product(self, name):
        self.products.delete_one({"name":name})
    def delete_all_products(self):
        self.products.delete_many({})
    def update_product_num_available(self, name, num_available):
        self.products.update_one({"name":name},{"$set":{"num_available":num_available}})
    def update_product_price(self, name, price):
        self.products.update_one({"name":name},{"$set":{"price":price}})
    def update_product_image_url(self, name, image_url):
        self.products.update_one({"name":name},{"$set":{"image_url":image_url}})
    def update_product_category(self, name, category):
        self.products.update_one({"name":name},{"$set":{"category":category}})
    def update_product_description(self, name, description):
        self.products.update_one({"name":name},{"$set":{"description":description}})
    def update_product_name(self, old_name, new_name):
        self.products.update_one({"name":old_name},{"$set":{"name":new_name}})
    def get_product_by_id(self, id):   
        return self.products.find_one({"id":id})
    def get_last_product_id(self):
        try:
            return self.products.find().sort("_id",-1).limit(1)[0]["id"]
        except:
            return None
    def product_exists(self, name, username):
        return self.products.find_one({"name":name,"from":username})!= None
    