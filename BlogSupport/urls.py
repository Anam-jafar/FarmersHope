from django.urls import path
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name='blog-dashboard'),
    path('add_blog/', views.addBlog, name='blog-add_blog'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    # pk is primary key of post object this is the convention
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),

]
