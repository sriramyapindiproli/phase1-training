from User import UserClass

class Login:
    __db = []
    def __init__(self):
        self.print_menu()
    def print_menu(self):
        print("Welcome User")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
    def create_user(self, name, email, password):
        new_user = UserClass(name, email, password)
        self.__db.append(new_user)
        print(self.__db)
        return True
    def validate_user(self, email, password):
        pass

obj = Login()
while True:
    option = input("Enter your choice: ")
    if option == '1':
        name = input("Enter your full name: ")
        email = input("Enter Email: ")
        password = input("create new password: ")
        res = obj.create_user(name,email, password)
        if res == True:
            print("User created successfully")
    elif option == '2':
        pass
    elif option == '3':
        break
    else:
        print("Invalid Input")




