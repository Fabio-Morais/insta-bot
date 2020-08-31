import os


class Login_info:
    info = []
    def __init__(self):
        self.read_file()

    def read_file(self):
        try:
            f = open(os.path.dirname(__file__) + "/../login_info.txt", "r")
            user_pass = f.readlines()
            if len(user_pass) < 1:
                raise FileNotFoundError
            for i in range(0, len(user_pass)-1, 1):
                if len(user_pass[i]) > 1 and len(user_pass[i+1]) > 1:
                    self.info.append({'username':user_pass[i].split('"')[1].strip(), 'password':user_pass[i+1].split('"')[1].strip()})
            f.close()
        except FileNotFoundError:
            f = open(os.path.dirname(__file__) + "/../login_info.txt", "w+")
            template = 'username="usernameExample"\npassword="passwordExample"'
            f.write(template)
            f.close()

