import re
from django.conf import settings
from django.http import HttpResponseRedirect

EXEMPT_URLS = [re.compile(settings.LOGIN_URL.lstrip('/'))]
if hasattr(settings, 'LOGIN_EXEMPT_URLS'):
    EXEMPT_URLS += [re.compile(url) for url in settings.LOGIN_EXEMPT_URLS]

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    # load page via view functions, but before that it runs middleware process_view
    def process_view(self, request, view_func, view_args, view_kwargs):
        assert hasattr(request, 'user') # check if user exists
        path = request.path_info.lstrip('/')
        print(path)
        # if user is not auth, redirect them
        if not request.user.is_authenticated:
            if not any(url.match(path) for url in EXEMPT_URLS):
                return HttpResponseRedirect(settings.LOGIN_URL)

# redirects to login even for admin page - more secure
# login as admin and access admin page through url