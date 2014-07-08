from django.conf.urls import patterns, url

from login import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^/login/$',views.login,name='login'),
    url(r'^/register/$',views.register,name='register'),
    url(r'^/signup/$',views.signup,name='signup'),
    url(r'^/posts/$',views.posts,name='posts'),
    url(r'^/create/$',views.createBlog,name='createBlog'),
     url(r'^/save/$',views.saveBlog,name='saveBlog'),
     url(r'^/show/(?P<post_id>\d+)/$',views.show,name='show'),
     url(r'^/edit/(?P<post_id>\d+)/$',views.edit,name='edit'),
     url(r'^/update/(?P<post_id>\d+)/$',views.update,name='update'),
     url(r'^/delete/(?P<post_id>\d+)/$',views.deletePost,name='deletePost'),
)