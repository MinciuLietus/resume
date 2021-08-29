# Create your views here.

from user.models import Education, Experience, Profile, User, Skill, WorkStyle
from django.shortcuts import render, redirect
from django.http import HttpResponse

def aboutMe(request):

    profile = Profile.objects.filter()[0:].get()

    skills = Skill.objects.all()
    education = Education.objects.all()
    profs = Profile.objects.all()
    experiences = Experience.objects.all()
    style = WorkStyle.objects.all()

    context = {'profile': profile, 'skill': skills, 'education': education, 'profs': profs, 'experience': experiences, 'style': style}

    

    return render(request, 'index.html', context)
