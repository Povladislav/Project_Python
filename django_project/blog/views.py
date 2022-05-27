from django.shortcuts import render,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from .models import Post
import logging

logger = logging.getLogger('main')
class PostListView(ListView):
    paginate_by = 5

    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-data_posted']




class UserPostListView(ListView):
    paginate_by = 5
    logger.info('cheking users')
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    def get_queryset(self):
        user = get_object_or_404(User,username = self.kwargs.get('username'))
        return   Post.objects.filter(author = user).order_by('-data_posted')


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        context['url'] = self.kwargs.get('username')
        return  context



class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    logger.info('creating post!')
    fields = ['title','content']


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = '/'
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})