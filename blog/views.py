from django.shortcuts import render
from . models import Post

posts=[
    {
       'author': 'John',
       'Title' : 'Post 1',
       'content':'This is the first post content',
       'date_posted': 'March 23,2023'
    },

    {
       'author': 'Tom',
       'Title' : 'Post 2',
       'content':'This is the second post content',
       'date_posted': 'March 24,2023'
    }

]

# Create your views here.

def home(request):
	context = {
	    'posts':Post.objects.all()
	}
	return render(request,'blog/home.html',context)

def about(request):
	return render(request, 'blog/about.html',{'Title' : 'About'})