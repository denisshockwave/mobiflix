# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import permissions
from .models import *
from django.shortcuts import render
from .myserializers import *
from .mobflixPermissions import *
from django.db.models import Q
# Create your views here.
from .filter import MovieFilter
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views import generic
import datetime
class IndexView(generic.ListView):
    model = Content
    template_name = 'index.html'
    context_object_name = 'movies'
    paginate_by = 12
    queryset =  Content.objects.all()

def home(request):
    content=""
    if request.method == "POST":
        if request.POST.get("search"):
            content=Content.objects.filter(Q(name__icontains=request.POST['query'])| Q(description__icontains=request.POST['query']))
    else:
        content =Content.objects.all()

    page = request.GET.get('page', 1)

    paginator = Paginator(content, 2)
    try:
        numbers = paginator.page(page)
        print numbers
    except PageNotAnInteger:
        numbers = paginator.page(1)
    except EmptyPage:
        numbers = paginator.page(paginator.num_pages)

    print "habesha"
    for n in numbers:
        print n.name
    return render(request, 'index.html', {'articles': numbers})

def checkWorthy(code):
    pass
def getExpiryTime(exp_tym):
    #current_tym
    exp=datetime.datetime.strptime(exp_tym,"%Y-%m-%dT%H:%M:%SZ")
    a=datetime.datetime.strftime(exp, '%Y-%m-%d %H:%M:%S')
    return a
def checkSessionTime(req):
    current_tym=datetime.datetime.now()
    if "expiry_date" in req.session:
        if current_tym >datetime.datetime.strptime(req.session['expiry_date'],'%Y-%m-%d %H:%M:%S'):
            req.session['status']="POSTER"
        else:
            pass #go on ..do nothing
    else:
        pass

def watch(request,pk):
    #check if the user is allowed to watch this video
    status="POSTER"
    state=""
    message=""
    if request.method == "POST":
        if request.POST.get("submit_code"):
            code=request.POST['code']

            l=LocalPermissionClass()
            ex=l.checkIfWatcher(code)
            #exists
            if ex:
                a=l.checkExpiry(ex)
                if a:
                    message="Code has been verified.Enjoy"
                    state="success"
                    request.session['status'] = 'WATCH'
                    t=ex[0].code_expiration
                    print "herer"
                    tym=getExpiryTime(t.strftime("%Y-%m-%dT%H:%M:%SZ"))
                    print tym
                    request.session['expiry_date']=tym
                else:
                    message="Dear customer,You Code has expired.Please purchase another one to enjoy our services"
                    state="info"
                    request.session['status'] = 'POSTER'

                #check if code has expired
            else:
                #check remotely this is for new codes sana sana
                r=RemotePermissionClass()
                a=r.verify_code(code)
                if "success" in a['status']:
                    message="Code has bee verified"
                    state="success"

                    request.session['expiry_date']=getExpiryTime(a['message']['expire_date'])
                    request.session['status'] = 'WATCH'
                else:
                    message=a['message']
                    state="danger"
                    request.session['status'] = 'POSTER'



    if "status" in request.session:
        checkSessionTime(request)
        status=request.session['status']

    print status
    video=Content.objects.get(id=pk)
    return render(request, 'player.html', {'video': video,"status":status,"state":state,"message":message})


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def getMoviePosters(request):
    c=Content.objects.all()
    serializer=ContentSerializer(c,many=True)
    return Response(serializer.data)
