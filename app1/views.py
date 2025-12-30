from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.template.defaultfilters import title
from django.urls import reverse
from django.template.loader import render_to_string
from .models import Post,Author,Tag
from .forms import PostForm
blog_data=[]

def home(request):
    posts = Post.objects.all().order_by("-date")
    context = {
        'title': 'Latest Blog Posts',
        'posts': posts,
        'latest_posts': Post.objects.all().order_by("-date")[:3]
    }

    return render(request, "app1/index.html", context)

def blogs(request):
    try:
        return render(request, "app1/blog.html")
    except KeyError:
        response = render_to_string("app1/404.html")
        return Http404(response)

def create_blog(request):
    posts = Post.objects.all().order_by("-date")

    if request.method == "POST":
        form = PostForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("/")
    else:
        form = PostForm()
    authors = Author.objects.all()
    tags = Tag.objects.all()
    context = {
        'title': 'Create a new blog',
        'form': form,
        'authors': authors,
        'tags': tags,
        'posts': posts,
        'latest_posts': posts[:3]
    }





    return render(request, 'app1/rough.html', context)

def custom_404(request, exception=None,**kwargs):
    return render(request, 'app1/404.html', status=404)

def blog_types(request, blog):
    posts = Post.objects.all().order_by("-date")
    context = {
        'title': 'Latest Blog Posts',
        'posts': posts,

        'latest_posts': Post.objects.all().order_by("-date")[:3]

    }
    try:

        if blog == "family_blogs":
            return render(request, 'app1/family.blogs.html',context)
        elif blog == "business_blogs":
            return render(request, 'app1/business_blogs.html', context)
        elif blog == "sales_blogs":
            return render(request, 'app1/sales.html',context)
        elif blog == "about_blogs":
            return render(request, 'app1/aboutt.html',context)

        else:
            response = render_to_string( "app1/404.html")
            return Http404(response)
    except KeyError:
        response = render_to_string("app1/404.html")
        return Http404(response)