from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


# for viewing all the blogs
def blogDashboard(request):
    context = {
        'blogs': Post.objects.all()
    }
    return render(request, 'BlogSupport/blog_dashboard.html', context)


# context data will be available in the html file

class PostListView(ListView):
    model = Post
    template_name = 'BlogSupport/blog_dashboard.html'
    context_object_name = 'blogs'
    ordering = ['-datePosted']


class PostDetailView(DetailView):
    model = Post



def addBlog(request):
    return render(request, 'BlogSupport/add_blog.html', {'title': 'Add a Question'})
