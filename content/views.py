# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework.authtoken.models import Token
from rest_framework_jwt.settings import api_settings
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from django.http import Http404

# Create your views here.
from django.contrib.auth.models import update_last_login

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
from .filer import Crawler, ThreadingDaemon


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

    except PageNotAnInteger:
        numbers = paginator.page(1)
    except EmptyPage:
        numbers = paginator.page(paginator.num_pages)

    return render(request, 'index.html', {'articles': numbers})

def checkWorthy(code):
    pass
def getExpiryTime(exp_tym):
    #current_tym
    exp=datetime.datetime.strptime(exp_tym,"%Y-%m-%d %H:%M:%S")
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

                    tym=getExpiryTime(t.strftime("%Y-%m-%d %H:%M:%"))

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


    video=Content.objects.get(id=pk)
    return render(request, 'player.html', {'video': video,"status":status,"state":state,"message":message})


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def getMoviePosters(request):
    c=Content.objects.all()
    serializer=ContentSerializer(c,many=True)
    return Response(serializer.data)
class VerifyVoucher(APIView):
    def get(self,request,voucher):
        code = voucher
        session={}

        url = "http://192.168.88.1"
        try:
            url = MovieServer.objects.all()[0]
            url=url.ip
         
        except:
            pass



        l=LocalPermissionClass()
        ex=l.checkIfWatcher(code)
        #exists
        print(ex)
        print("================")
        if ex: #watch code has been logged
            print("checked bro")
            a=l.checkCount(ex)
            print(a)
            if a:
               
                message="Code has been verified.Enjoy"
                state="success"
                session['status'] = 'WATCH'
                session['base_url'] = url
                session['expiry_date']="2100-01-25 11:49:49"
                session['count'] = ex[0].paid_count-ex[0].count # remaining
             
            else:
                session['message']="Dear customer,You Code has been fully utilized.Please purchase another one to enjoy our services"
                session['state']="info"
                session['count']=0 #remaining downloads
                session['status'] = 'POSTER'
             

            #check if code has expired
        else:
            #check remotely this is for new codes sana sana
            r=RemotePermissionClass()
            a=r.verify_code(code)
            if "success" in a['status']:
                session['message']="Code has bee verified"
                session['state']="success"
                session['base_url'] = url
                session['count']=a['paid_count']
                session['expiry_date']=getExpiryTime(a['message']['expire_date'])
                session['status'] = 'WATCH'
                #####
                # Initiate voucherCount
              
                ###
            else:
                session['message']=a['message']
                session['state']="danger"
                session['status'] = 'POSTER'

        print(session)
        return Response(session)



def localVerify(code):
    l=LocalPermissionClass()
    ex=l.checkIfWatcher(code)
    #exists
    session={"message":"Please verify code or purchase code to continue enjoying","status":"POSTER","state":""}
    if ex:
        a=l.checkExpiry(ex)
        url = "http://192.168.88.1"
        try:
            url = MovieServer.objects.all()[0]
            url = url.ip
           
        except:
            pass

        if a:
            session['message']="Code has been verified.Enjoy"
            session['state']="success"
            session['status'] = 'WATCH'
            t=ex[0].code_expiration

            tym=getExpiryTime(t.strftime("%Y-%m-%d %H:%M:%S"))
            session['base_url'] = url
            session['expiry_date']=tym
        else:
            session['message']="Dear customer,You Code has expired.Please purchase another one to enjoy our services"
            session['state']="info"
            session['status'] = 'POSTER'


    return session

class UploadContent(APIView):
    def post(self,request):
        serializer = ContentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(serializer.data)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    def get(self,request):
        data=Content.objects.all()
        serializer = ContentDisplaySerializer(data,many=True)
        return Response(serializer.data)


class UploadContentVerifyView(APIView):
    def get_object(self,id):
        try:
            return Content.objects.get(id=id)
        except Content.DoesNotExist:
            raise Http404

    def get(self,request,id,voucher):
        #check if user has paid,,,,return with a different url  ContentDisplaySerializer
        v=localVerify(voucher)
        data=self.get_object(id)
        if "WATCH" in v['status']:
         
            serializer = ContentSerializer(data)

        else:
            serializer = ContentDisplaySerializer(data)
        return Response({"response":serializer.data,"status":v})

class UploadContentDetailView(APIView):
    def get_object(self,id):
        try:
            return Content.objects.get(id=id)
        except Content.DoesNotExist:
            raise Http404

    def get(self,request,id):
        #check if user has paid,,,,return with a different url  ContentDisplaySerializer

        data=self.get_object(id)
        serializer = ContentSerializer(data)
        return Response(serializer.data)
    def put(self,request,id):
        #check if admin permission
        serializer = ContentSerializer(data=request.data,instance=self.get_object(id))
        return Response(serializer.data)
    def delete(self,request,id):
        #check if admin to delete
        status=self.get_object(id).delete()
        return Response({"status":status})


class SeriesDetailView(APIView):
    def get(self, request, slug):
        data = Content.objects.filter(slug=slug)
        serializer = ContentDisplaySerializer(data, many=True)
        return Response(serializer.data)

class ContentCategoryView(APIView):
    def post(self,request):
        serializer = ContentCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    def get(self,request):
        data=ContentCategory.objects.all()
        serializer = ContentCategorySerializer(data,many=True)
        return Response(serializer.data)

class ContentCategoryDetailView(APIView):
    def get_object(self,id):
        try:
            return Category.objects.get(id=id)
        except Category.DoesNotExist:
            raise Http404

    def get(self,request,id):
        data=self.get_object(id)
        serializer = ContentCategorySerializer(data,many=True)
        return Response(serializer.data)
    def put(self,request,id):
        #check if admin permission
        serializer = ContentCategorySerializer(data=request.data,instance=self.get_object(id))
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    def delete(self,request,id):
        #check if admin to delete
        status=self.get_object(id).delete()
        return Response({"status":status})



        
class ContentSearchCategory(APIView):
    """

    """
    def get(self,request,category):
        data=Content.objects.filter(category__name__icontains=category)
      
        serializer=ContentDisplaySerializer(data,many=True)
        return Response(serializer.data)

class SearchQuery(APIView):
    def get(self,request):

        query = request.GET['query']
    

        term_list = query.strip().split(' ')
        # p =  Project.objects.filter(awardStatus="UNAWARDED")
        p=Content.objects.all()


        q = Q(name__icontains=term_list[0]) | Q(status__icontains=term_list[0]) | Q(category__name__icontains=term_list[0]) | Q(description__icontains=term_list[0]) | Q(director__icontains=term_list[0]) | Q(video_qualify__icontains=term_list[0])

        for term in term_list[1:]:
            q.add((Q(name__icontains=term) | Q(status__icontains=term) | Q(category__name__icontains=term) | Q(description__icontains=term) | Q(director__icontains=term) | Q(video_qualify__icontains=term)), q.connector)
        search= p.filter(q)
        serializer=ContentDisplaySerializer(search,many=True)
        return Response(serializer.data)


class ContentCrawl(APIView):
    def post(self,request):
        #initiate crawling daemon
        run = ThreadingDaemon(request.data['dir'])
      
        return Response({})

        
        #daemonize the crawling process and alert user

class LinkCounter(APIView):
    def post(self,request):
        data=request.data
        voucher = data['voucher']
        try:
            v = Watchers.objects.get(voucher=voucher)
            if v.count ==v.paid_count:
                return Response({"status": "error", "message": "Voucher has been utilized"})
            
            v.count=v.count+1
            v.save()

            return Response({"count":v.count})
        except:
             
            return Response({"status":"error","message":"Voucher does not exist or not verified"})
