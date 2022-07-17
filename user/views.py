# Create your views here.

from user.models import Education, Experience, Profile, Skill, WorkStyle
from django.shortcuts import render


def aboutMe(request):
    profile = Profile.objects.get(id='49dc6222-c683-4419-a2c3-d3cc7fd78a9c')

    skills = Skill.objects.filter(profile__name='Virginija')
    education = Education.objects.filter(profile__name='Virginija')
    experiences = Experience.objects.filter(profile__name='Virginija')
    style = WorkStyle.objects.filter(profile__name='Virginija')

    context = {
        'profile': profile,
        'skill': skills,
        'education': education,
        'experience': experiences,
        'style': style,
    }

    return render(request, 'index.html', context)
