from django.shortcuts import render
from .models import Post

blogs = [
    {
        'author': 'Anam',
        'title': 'Blog Post 1',
        'content': 'First Post content',
        'date_posted': 'August 23, 2021'
    },
    {
        'author': 'Arman',
        'title': 'Blog Post 2',
        'content': 'Second Post content',
        'date_posted': 'August 25, 2021'
    },

]


# for viewing all the blogs
def blogDashboard(request):
    context = {
        'blogs': Post.objects.all()
    }
    return render(request, 'BlogSupport/blog_dashboard.html', context)


# context data will be available in the html file


def addBlog(request):
    return render(request, 'BlogSupport/add_blog.html', {'title': 'Add a Question'})
