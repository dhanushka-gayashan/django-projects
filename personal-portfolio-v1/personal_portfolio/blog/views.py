from django.shortcuts import render, get_object_or_404
from . import models


# Create your views here.
def all_blogs(request):
    blogs = models.Blog.objects.order_by('-date')
    context = {
        'blogs': blogs
    }
    return render(request, 'blog/all_blogs.html', context=context)


def detail(request, blog_id):
    blog = get_object_or_404(models.Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog})

