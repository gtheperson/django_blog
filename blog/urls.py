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
	# the {% url %} essentially reserves this based on the name, so it generates a url based on the regex, and the passed in var is asigned to the P? (a parameter to pass into the view)
	url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
	# url for adding a new post
	url(r'^post/new/$', views.post_new, name="post_new"),
	url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name="post_edit"),
	# attempt url for archive
	url(r'^archive/$', views.post_archive, name="post_archive"),
]