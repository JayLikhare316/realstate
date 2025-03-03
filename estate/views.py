from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    profileobj=AgentProfile.objects.all()
    context = {'profileobj':profileobj}
    return render(request,'index.html',context)

def about(request):
    profileobj=TeamProfile.objects.all()
    context = {'profileobj':profileobj}
    return render(request, 'about.html', context)

def contact(request):
    return render(request, 'contact.html')

def bloggrid(request):
    return render(request, 'blog-grid.html')

def propertygrid(request):
    return render(request, 'property-grid.html')

def propertysingle(request):
    return render(request, 'property-single.html')

def blogsingle(request):
    return render(request, 'blog-single.html')

def agentsgrid(request):
    return render(request, 'agents-grid.html')

def agentsingle(request):
    return render(request, 'agent-single.html')