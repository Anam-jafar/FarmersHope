from django.shortcuts import render
from django.http import HttpResponse


# for viewing all the blogs
def blogDashboard(request):
    return render(request, 'BlogSupport/blog_dashboard.html')


def addBlog(request):
    return render(request, 'BlogSupport/add_blog.html')
