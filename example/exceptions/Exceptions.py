from django.http import HttpResponse
from django.http import JsonResponse
import json
from example.errors.errors import ApiErrors
from ..LoginFormRequest.loginFormRequest import LoginFormRequest



def set_errors(api, list=None):
    if  list == None:
        list_api_errors = []
        list_api_errors.append(api)
    
    api_errors_dict = [api.api_errors_to_list() for api in list_api_errors]
    response = json.dumps(api_errors_dict)
    json_response = json.loads(response)
    
    return json_response
    



def require_post(function):
    def wrapped_view(request, *args, **kwargs):
        
        if request.method != 'POST':
            json_response = set_errors(ApiErrors("field", "Método HTTP Inválido"))
            return HttpResponse(json_response, content_type="application/json", status=405)
        
        elif not request.body:
            json_response = set_errors(ApiErrors("field", "Requisição sem Corpo"))
            return HttpResponse(json_response, content_type="application/json", status=400)

        else:
             body_unicode = request.body.decode('utf-8')  
             body = json.loads(body_unicode) 
              
             login_form = LoginFormRequest(body)
             patterns = login_form.patterns
             list_api_errors = []

             for key in patterns:
                 if not login_form.is_valid(patterns[key][1], key):
                     list_api_errors.append(ApiErrors(patterns[key][0], "Campo Inválido"))
        
             if len(list_api_errors) != 0:
                
                api_errors_dict = [api.api_errors_to_list() for api in list_api_errors]
                response = json.dumps(api_errors_dict)
                json_response = json.loads(response)
                return HttpResponse(json_response, content_type="application/json", status=400)  
        return function(request, *args, **kwargs)
    return wrapped_view


