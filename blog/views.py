from django.shortcuts import render
from .models import Post


# Create your views here.
def listblog(request):
    Data = {'Posts': Post.objects.all().order_by("-date")}
    return render(request, 'blog/blog.html', Data)
