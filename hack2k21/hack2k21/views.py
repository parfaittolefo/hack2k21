from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponseRedirect
import datetime

def home(request):
    current_year = datetime.datetime.now().year
    t=get_template('home.html')
    html=t.render({"year":current_year})
    return HttpResponse(html)

def services(request):
    t=get_template('services/services.html')
    html=t.render()
    return HttpResponse(html)

def projetcs(request):
    t=get_template('projects/projects.html')
    html=t.render()
    return HttpResponse(html)

def blogs(request):
    t=get_template('blog/blogs.html')
    html=t.render()
    return HttpResponse(html)

def post(request):
    t=get_template('blog/post.html')
    html=t.render()
    return HttpResponse(html)


def cv(request):
    t=get_template('cv/cv.html')
    html=t.render()
    return HttpResponse(html)

