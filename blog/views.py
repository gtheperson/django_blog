from django.shortcuts import render

# views take your models and apply a template to them so they are displayed in a certain way in a webpage
# Create your views here.

# when a page is requested django creates a https request object containg meta data about the request 
# which is then passed at the first arr of the view
def post_list(request):
	return render(request, 'blog/post_list.html', {})