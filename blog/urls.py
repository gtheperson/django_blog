# look here for blog url processing

# get the url
from django.conf.urls import url
#import views from the currernt directory
from . import views

# url patterns just like one created in mysite dir, keeping the blog stuff here and redirecting from mysite url is neater
urlpatterns = [
	# this matches an empty string, which 127.0.0.8 etc is, and tells it to use a view named postlist for this url
	# it also names the url, all urls should be given simple names
	url(r'^$', views.post_list, name = 'post_list'),
	url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
]