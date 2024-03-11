import re


class LoginFormRequest:
        def __init__(self, request):
                self.username = request["username"]
                self.email = request["email"]
                self.password = request["password"]
                self.patterns = {
                        self.username: r'^\S{1,}$',
                        self.password: r'^\S{8,}$',
                        self.email: r'^\S+@\S+\.\S+$'
                }

        def is_valid(self, expression, field):
              pattern = re.compile(expression)
              return re.fullmatch(pattern, field) 
        
