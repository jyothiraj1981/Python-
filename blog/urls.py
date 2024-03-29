from django.urls import path
from . import views
from . views import PostListView,PostDetailView,PostCreateView

urlpatterns = [
    #path('', views.home,name='blog-home'),
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>', PostDetailView.as_view(), name='blog-detail'),
    path('post/new/', PostCreateView.as_view(), name='blog-create'),
    path('about', views.about,name='blog-about'),

]
