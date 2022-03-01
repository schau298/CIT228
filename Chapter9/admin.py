from user import User
from privileges import Privileges

class Admin(User):
    def __init__(self,first_name,last_name,bday,username,education,phone_number,password,permissions):
        super().__init__(first_name,last_name,bday,username,education,phone_number,password)
        self.privileges=Privileges(permissions)