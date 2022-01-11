from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogDashboard, name='blog-dashboard'),
    path('add_blog/', views.addBlog, name='blog-add_blog'),
]
