# Create your views here.
from urllib.parse import urlsplit

from django.shortcuts import redirect, render
from django.utils import translation
from django.utils.translation import activate

from user.models import Profile


class PortfolioAbout:
    @classmethod
    def set_language(cls, request):
        language = translation.get_language_from_request(request)
        return redirect(language)

    @classmethod
    def main(cls, request):
        profile = Profile.objects.get(name="Aurimas")
        base_url = cls.get_base_url(request.build_absolute_uri())

        context = {
            "profile": profile,
            "languages": profile.languages.all(),
            "education": profile.education.all(),
            "experience": profile.experience.all(),
            "style": profile.workstyle.all(),
            "skills": profile.skills,
            "base_url": base_url,
        }

        return render(request, "index.html", context)

    @classmethod
    def main_en(cls, request):
        activate('en')
        return cls.main(request)

    @classmethod
    def main_lt(cls, request):
        activate('lt')
        return cls.main(request)

    @staticmethod
    def get_base_url(url):
        result = urlsplit(url)
        base_url = result.scheme + "://" + result.netloc
        return base_url
