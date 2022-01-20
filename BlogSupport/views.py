from django.shortcuts import render
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# for viewing all the blogs
def blogDashboard(request):
    context = {
        'blogs': Post.objects.all()
    }
    return render(request, 'BlogSupport/blog_dashboard.html', context)


# context data will be available in the html file


def addBlog(request):
    return render(request, 'BlogSupport/add_blog.html', {'title': 'Add a Question'})


# class based view

class PostListView(ListView):
    model = Post
    # for list and Detail
    # <app>/<model>_<viewtype>.html -- looking for this templates if it's not the name then use this things
    template_name = 'BlogSupport/blog_dashboard.html'
    context_object_name = 'blogs'
    # context object name in list View is object if we want something else then declare it here
    ordering = ['-datePosted']  # this is for ordering - for newest to oldest


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['postTitle', 'postContent']

    # for create and update
    # <app>/<model>_form.html
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['postTitle', 'postContent']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/blog_dashboard/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
