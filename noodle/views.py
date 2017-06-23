from django.shortcuts import render
from django.http import HttpResponse
from .forms import LoginForm
from django.contrib.auth import authenticate, login

# Create your views here.


def main_page(request):
    return render(request, 'noodle/main_page.html',  {})


def blog_page(request):
    return render(request, 'noodle/blog_page.html',  {})


def login_page(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()

    return render(request, 'noodle/userlogin.html', {'form': form})
