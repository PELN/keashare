from django.conf import settings
from django.http import HttpResponseRedirect

# define EXEMPT_URLS = a list of the login_url
EXEMPT_URLS = [settings.LOGIN_URL.lstrip('/')] # remove slash in the start of LOGIN_URL = '/accounts/' - or it won't work
if hasattr(settings, 'LOGIN_EXEMPT_URLS'): # if the settings has LOGIN_EXEMPT_URLS defined
    EXEMPT_URLS += [url for url in settings.LOGIN_EXEMPT_URLS] # then add the urls to EXEMPT_URLS list

class LoginRequiredMiddleware:
    def __init__(self, get_response): # get_response is a function 
        self.get_response = get_response

    def __call__(self, request):
        # execute code for each request before view is called
        response = self.get_response(request)
        # execute code for each request after view is called
        return response
    
    # process_view is called after the request is made and before the view is loaded
    def process_view(self, request, view_func, view_args, view_kwargs):
        path = request.path_info.lstrip('/') # the url the user is currently trying to request
        print(path)
        
        if not request.user.is_authenticated: # if user is not authenticated
            if not path in EXEMPT_URLS: # if path they are currently trying to request does not match any in the list
                return HttpResponseRedirect(settings.LOGIN_URL) # redirect user to the LOGIN_URL in settings