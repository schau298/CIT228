from user import User
from privileges import Privileges
from admin import Admin

user1 = User("Dylan","Schaub","password1","07/06/2002","dylan123","Some College","1234567891")
user2 = User("John","Doe","password2","04/19/1992","john123","High School Diploma","1234560000")
user3 = User("Jane","Doe","password3","08/09/2004","jane123","Some High School","2313432222")
admin1 = Admin("Boss","Man", "adminpassword","01/02/1985","admin123","Doctorate Degree","2910001111", privileges )
user1.greet_user()
user1.describe_user()
print()

user2.greet_user()
user2.describe_user()
print()

user3.greet_user()
user3.describe_user()
print()

admin1.greet_user()
admin1.describe_user()
privileges.show_privileges()
