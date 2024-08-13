# from django.shortcuts import render

# # Create your views here.

# def index(request):
#     return render(request,'index.html')
# #apa ndipo napoandika requests zangu ili zivutwe na urls kwenda kua displayed kwenye browser
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Profile, SocialLink, Service, Education, Experience, Skill, Project, Testimonial
from .forms import ContactForm

def index(request):
    profile = get_object_or_404(Profile, pk=1)  # Assuming you have a profile with ID 1
    social_links = profile.social_links.all()
    services = profile.services.all()
    education_list = profile.education.all()
    experience_list = profile.experience.all()
    skills = profile.skills.all()
    projects = profile.projects.all()
    testimonials = profile.testimonials.all()
    
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Process form data here
            return redirect('index')
    else:
        form = ContactForm()

    context = {
        'profile': profile,
        'social_links': social_links,
        'services': services,
        'education_list': education_list,
        'experience_list': experience_list,
        'skills': skills,
        'projects': projects,
        'testimonials': testimonials,
        'form': form
    }
    return render(request, 'index.html', context)
