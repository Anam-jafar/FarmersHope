from django.urls import path
from .views import PostListView, PostDetailView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-dashboard'),
    path('blog/<int:pk>/', PostDetailView.as_view(), name='blog-detail'),
    path('add_blog/', views.addBlog, name='blog-add_blog'),
]
