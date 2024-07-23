from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')
#apa ndipo napoandika requests zangu ili zivutwe na urls kwenda kua displayed kwenye browser

from django.shortcuts import render, redirect
from .forms import ProfileForm

def upload_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile_list')
    else:
        form = ProfileForm()
    return render(request, 'upload_profile.html', {'form': form})

def profile_list(request):
    profiles = profile_list.objects.all()
    return render(request, 'profile_list.html', {'profiles': profiles})
