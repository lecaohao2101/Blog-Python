from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
# request cua nguoi dung
def home(request):
    # response = HttpResponse()
    # response.writelines("<h1>Xin Chao</h1>")
    # response.write("This is app home")
    return render(request, 'pages/home.html')




def contact(request):
    return render(request, 'pages/contact.html')
# def blog(request):
#     return render(request, 'pages/blog.html')
