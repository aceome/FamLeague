from django.shortcuts import render, reverse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required

# Create your views here.
# @login_required
def index(request):
    return render(request, 'famleague/index.html')


def mylogin(request):
    # retrieve the variables from the form submission
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('famleague:main'))
    else:
        return HttpResponse('That is not a valid Login.')
        # return an 'invalid login' error message

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('famleague:index'))
    # redirect to a success page.


def register(request):
    return render(request, 'famleague/register.html')


def main(request):
    return render(request, 'famleague/main.html')

def rules(request):
    return render(request, 'famleague/rules.html')

def lineup(request):
    return render(request, 'famleague/lineup.html')

def leader(request):
    return render(request, 'famleague/leader.html')