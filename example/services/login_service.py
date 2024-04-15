from example.admin import User


class LoginService:
    def __init__(self,):
        pass
    
    def auth(self, username, password):
        user = User()
        return user.auth(username, password)
        