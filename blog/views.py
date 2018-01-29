from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .forms import PostForm

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
	# breaks if pk=pk not included, set passed var as the thing that controls which post is got
	#pk is key of each post, a unique identifier
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
	# for when the logged in user wants to add a new blog post
	if request.method == "POST":
		form = PostForm(request.POST)
		# does it have the title and text as required?
		if form.is_valid():
			post = form.save(commit=False)#don't send it off till we've added the stuff below
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_detail', pk=post.pk)
	else:
		form = PostForm()
	return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def post_archive(request):
	# a basic list of posts by date stored in a dictionary
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
	now = timezone.now()

	# creat dic with initial keyes as years, for dics of months as keys for posts
	post_dic = {}
	#months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
	start_year = posts[0].published_date.year
	end_year = posts[len(posts)-1].published_date.year
	for i in range(start_year, end_year + 1):
		post_dic[i] = {}
		for month in range(12, 0, -1):
			post_dic[i][month] = []
	for post in posts:
		post_dic[post.published_date.year][post.published_date.month].append(post)

	return render(request, 'blog/archive.html', {'post': post,'post_dic': post_dic})

