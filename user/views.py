# Create your views here.

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

        context = {
            "profile": profile,
            "languages": profile.languages.all(),
            "education": profile.education.all(),
            "experience": profile.experience.all(),
            "style": profile.workstyle.all(),
            "skills": profile.skills,
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
