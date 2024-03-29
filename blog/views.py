from django.shortcuts import render
from . models import Post
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
   ListView,
   DetailView,
   CreateView
)

# Create your views here.

#def home(request):
#	context = {
#	    'posts':Post.objects.all()
#	}
#	return render(request,'blog/home.html',context)

class PostListView(ListView):
   model = Post
   template_name = 'blog/home.html'
   #blog/post_list.html
   #<app_name>/model_viewtype
   
   context_object_name = 'posts'
   ordering = ['-date_posted']

class PostDetailView(DetailView):
   model = Post

class PostCreateView(LoginRequiredMixin,CreateView):
   model = Post
   fields = ['Title','content']

   def form_valid(self,form):
      form.instance.author = self.request.user
      return super().form_valid(form)
  

def about(request):
	return render(request, 'blog/about.html',{'Title' : 'About'})

