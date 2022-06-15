from django.shortcuts import render
from blog.models import Project


# Create your views here.
def index(request):
    work = Project.objects.all
    wk = {'work':work} 
    return render(request,'index.html', wk)

def detail(request):
     work = Project.objects.all()
     p = {'work' :work}
     return render(request,'detail.html', p)