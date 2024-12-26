from db import Database
class TodoModel():
    def __init__(self, data:dict,username:str):
        self.db = Database()
        self.description = data["description"]
        self.title = data["title"]
        self.username = username
    def create(self):
        self.db.insert_todo(self.title, self.description,"pending", self.username)
        return True
    def get_all(self):
        return self.db.get_all_todos(self.username)
    def delete(self, id:int):
        self.db.delete_todo(id)
        return True
    def update(self, id:int, data:dict):
        self.db.update_todo(id, data)