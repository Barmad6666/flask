from db import Database
class ProductModel():
    
    def __init__(self,data:dict,username:str,job:str):
        self.db = Database()
        id = self.db.get_last_product_id()
        if id is not None:
            ProductModel.id = id
        else:
            ProductModel.id = 0
        self.name  = data['name']
        self.num_available  = data['num_available']
        self.price  = data['price']
        self.weight  = data['weight']
        self.description = data['description']
        self.image_url  = data['image_url']
        self.category  = None
        self.username = username
        ProductModel.id += 1
        self.id = ProductModel.id 
        self.job=job
    
    def __str__(self):
        return f"{self.name} by {self.username}"
    def create(self):
        self.db.insert_product(self.name,self.num_available,self.price,self.weight,self.description,self.image_url,self.category,self.id,self.username)
    def get_all(self):
        return self.db.find_products()
    def get_by_id(self,id:int):
        return self.db.get_product_by_id(id)
    def delete(self,id:int):
        self.db.delete_product(id)
    def exists(self):
        return self.db.product_exists(self.name,self.username)