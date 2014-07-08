from django.db import models

# Create your models here.
class User(models.Model):
	username  = models.CharField(max_length=200)
	firstname = models.CharField(max_length=200)
	lastname  = models.CharField(max_length=200)
	password  = models.CharField(max_length=200)
	gender	  = models.CharField(max_length=200)
	email	  = models.CharField(max_length=200)
	dob		  = models.DateTimeField('Date of Birth')

	def __unicode__(self):
		return self.firstname

	def authenticate(self,uname,pwd):
		if User.objects.filter(username=uname,password=pwd).exists():
			return True
		else:
			return False

class Blog(models.Model):
	title		= models.CharField(max_length=200)
	description = models.CharField(max_length=200)
	published	= models.DateTimeField('Date published')
	created_by	= models.CharField(max_length=200)

	def __unicode__(self):
		return self.title
	def getPosts(self):
		return Blog.objects.all()
	def createPost(self,_title,_description,_date,_by):
		a=Blog(title=_title,description=_description,published=_date,created_by=_by)
		a.save()
		return True





