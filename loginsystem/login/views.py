from django.template.loader import get_template
from django.core.context_processors import csrf
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import render
from django.http import HttpResponse
from login.models import User
from login.models import Blog
from django.shortcuts import redirect



# Create your views here.
def index(request):
	name="Login Here"
	return render(request,'login.html',{'name':name})

def login(request):
	uname =	request.POST['username']
	pwd   = request.POST['password']
	userobj= User()
	valid = userobj.authenticate(uname,pwd)
	if valid:
		userData = User.objects.get(username=uname)
		request.session['id']=userData.id
		request.session['username']=userData.username
		request.session['firstname']=userData.firstname
		request.session['lastname']=userData.lastname
		request.session['gender']=userData.gender
		request.session['email']=userData.email	
		return redirect('posts')
	else:
		errormessage="Authentication failed try again"
		return render(request,"login.html",{'errormessage':errormessage})

def register(request):
	return render(request,"signup.html")

def signup(request):
	_username = request.POST['username']
	_firstname= request.POST['firstname']
	_lastname = request.POST['lastname']
	_password = request.POST['pwd']
	_gender	 = request.POST['gender']
	_email    = request.POST['email']
	_dob 	 = request.POST['dob']
	if(_username =='' or _firstname =='' or _password =='' or _gender =='' or _email =='' or  _dob ==''):
		errormessage="Please provide all Mandatory Fields"
		return render(request,"signup.html",{'errormessage':errormessage})
	else:
		a=User(username=_username,firstname=_firstname,lastname=_lastname,password=_password,gender=_gender,email=_email,dob=_dob)
		a.save()
		errormessage="Registered Succesfully Please Login!!!!"
		return render(request,"login.html",{'errormessage':errormessage})

def posts(request):
	blogObj  = Blog()
	allPosts = blogObj.getPosts()
	return render(request,"posts.html",{'allPosts':allPosts})

def createBlog(request):
	return render(request,"create.html")

def saveBlog(request):
	if(request.POST['title']=='' or request.POST['description']=='' or request.POST['Date']=='' or request.POST['Writer']==''):
		errormessage="Please provide all Mandatory Fields"
		return render(request,"create.html",{'errormessage':errormessage})
	else:
		blogObj  = Blog()
		saved	 = blogObj.createPost(request.POST['title'],request.POST['description'],request.POST['Date'],request.POST['Writer'])
		if saved:
			return redirect('posts')
		else:
			return render(request,"create.html")
def show(request,post_id):
    post = Blog.objects.get(pk=post_id)
    return render(request, 'show.html',{'post': post})

def edit(request,post_id):
	post = Blog.objects.get(pk=post_id)
	return render(request, 'edit.html',{'post': post})
def update(request,post_id):
	if(request.POST['title']=='' or request.POST['description']=='' or request.POST['Date']=='' or request.POST['Writer']==''):
		errormessage="Please provide all Mandatory Fields"
		return render(request,"edit.html",{'errormessage':errormessage})
	else:
		Blog.objects.filter(pk=post_id).update(title=request.POST['title'],description=request.POST['description'],published=request.POST['Date'],created_by=request.POST['Writer'])
		return redirect('posts')
def deletePost(request,post_id):
	Blog.objects.filter(pk=post_id).delete()
	return redirect('posts')

