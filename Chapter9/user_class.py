class User:
    def __init__(self, first_name, last_name, password, bday, username, education, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.bday = bday
        self.education = education
        self.phone_number = phone_number
        self.login_attempts= 0

    def describe_user(self):
        print(f"The profile {self.username} belongs to {self.first_name} {self.last_name} who's education level is {self.education}.")
        print(f"{self.first_name}'s birthday is {self.bday} and thier phone number is {self.phone_number}.")
        
    def greet_user(self):
        print(f"Welcome back {self.first_name}.")
    
    def increment_login_attempts(self):
            self.login_attempts += 1
    
    def reset_login_attempts(self):
            self.login_attempts = 0


user1 = User("Dylan","Schaub","password1","07,06/2002","dylan123","Some College","1234567891")
user2 = User("John","Doe","password2","04,19/1992","john123","High School Diploma","1234560000")
user3 = User("Jane","Doe","password3","08,09/2004","jane123","Some High School","2313432222")

user1.greet_user()
user1.describe_user()
print()

user2.greet_user()
user2.describe_user()
print()

user3.greet_user()
user3.describe_user()
print()

print("----------------Exercise 9-5----------------------")
print("Calculating Login Attempts...")
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print("Log in attemps: " + str(user1.login_attempts))

print("Login attempts resetting...")
user3.reset_login_attempts()
print("Log in attempts = " + str(user1.login_attempts))