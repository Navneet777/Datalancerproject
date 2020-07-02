from django.shortcuts import render ,redirect, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User , auth
from django.contrib import messages
from info.models import Contactus , Marks , BasicInfo , TrandingCourse , WebCourse ,Post
from django.db.models import Q , Count
from django.conf import settings
from info.forms import Contactform , Trainingform
from django.views import generic

def login(request):
    if request.method =="POST":
        name = request.POST['Name']
        password = request.POST['Password']
        user = auth.authenticate(username=name,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('index')

            print("Login Successfully")
        else:
            messages.success(request,'Incorrect Username or Password.')
            return redirect('login')
    return render(request,'login.html')

def Signup(request):
    if request.method =="POST":
        first_name = request.POST['name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cnfpassword = request.POST['password1']
        if password != cnfpassword:
            return HttpResponseRedirect(reverse('Signup'))
        else:
            entry = User.objects.create_user(username=username,email=email,password=password)
            entry.save()
            print("User Created")
            messages.success(request,'User Successfully Created.')
            return redirect('login')
    else:
        return render(request,'signup.html')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/')

def Contactus(request):
    form = Contactform()
    if request.method =="POST":
        form = Contactform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            form = Contactform()
    return render(request,'Contactus.html',{'form':form})

def Edata(request):
    a = Marks.objects.filter(english_marks__gte=33,math_marks__gte=33,science_marks__gte=33)
    b = a.filter(english_marks__in=[33,34])
    s = a.count()
    return render(request,'score.html',{'a':a , 's':s,'b':b })

def courses(request):
    trndcourse = TrandingCourse.objects.all()[:4]
    webcourse = WebCourse.objects.all()[:4]

    return render(request,'courses.html',{'trndcourse':trndcourse,'webcourse':webcourse,  'media_url':settings.MEDIA_URL})

def Training(request):
    form = Trainingform()
    if request.method == "POST" :
        form = Trainingform(request.POST)
        if form.is_valid():
            return redirect('index')
        else:
            form = Trainform()
    return render(request,'training.html',{'form':form})

    return render(request,'training.html')

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')[:5]
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

def blogpost(request):
    allblog = Post.objects.all().order_by('-created_on')
    return render(request,'blogpost.html' , {'allblog': allblog})
