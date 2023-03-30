from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import RegistrationForm
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

def error(request, exception):
    return render(request, 'pages/error.html')

def error(request):
    return render(request, 'pages/error.html')

def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        #no se goi nhung def tren
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    return render(request, 'pages/register.html', {'form': form})