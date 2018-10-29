from django.shortcuts import render, reverse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from .models import Team

from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    teams = request.user.team_set.all()
    user_teams = {'teams': teams}
    return render(request, 'famleague/index.html', user_teams)

def login_view(request):
    return render(request, 'famleague/login.html')

# receives the form submission
def login_user(request):
    # retrieve the variables from the form submission
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse('famleague:index'))
    else:
        return HttpResponseRedirect(reverse('famleague:login_view'))


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('famleague:login_view'))
    # redirect to a success page.


def register_user(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    user = User.objects.create_user(username, email, password)
    login(request, user)
    return HttpResponseRedirect(reverse('famleague:index'))


def register(request):
    return render(request, 'famleague/.html')


@login_required
def rules(request):
    return render(request, 'famleague/rules.html')


@login_required
def lineup(request, category):
    teams = Team.objects.filter(category=category)
    user_teams = {'teams': teams, 'category': category}

    return render(request, 'famleague/lineup.html', user_teams)


@login_required
def leader(request):
    return render(request, 'famleague/leader.html')
