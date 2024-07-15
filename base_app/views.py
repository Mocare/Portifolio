from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'index.html')
#apa ndipo napoandika requests zangu ili zivutwe na urls kwenda kua displayed kwenye browser

