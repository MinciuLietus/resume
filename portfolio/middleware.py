from django.shortcuts import redirect
from django.utils import translation


class LanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        language = translation.get_language_from_request(request)
        if language:
            return self.get_response(request)
        else:
            # Redirect to a language-specific page
            return redirect('set_language', permanent=True)
