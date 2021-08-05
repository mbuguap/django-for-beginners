from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import BlogPost


class BlogListView(ListView):
    model = BlogPost
    template_name = 'blog.html'

class BlogDetailView(DetailView): 
    model = BlogPost
    template_name = 'post_detail.html'

class BlogCreateView(CreateView): 
    model = BlogPost
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']    

class BlogUpdateView(UpdateView): 
    model = BlogPost
    template_name = 'post_edit.html'
    fields = ['title', 'body']