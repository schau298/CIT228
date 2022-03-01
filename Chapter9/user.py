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