from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

# views take your models and apply a template to them so they are displayed in a certain way in a webpage
# Create your views here.

# when a page is requested django creates a https request object containg meta data about the request 
# which is then passed at the first arr of the view
def post_list(request):
	# create an ordered post list
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	# stuff between {} is what the template (post_list.html) will use to do stuff
	return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
	# breaks if pk=pk not included
	#pk is key of each post, a unique identifier
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post': post})