

class ApiErrors:
    def __init__(self, field, mensage):
        self.field = field
        self.mensage = mensage

    def api_errors_to_list(self,):
        return {"field": self.field, "mensage": self.mensage}
