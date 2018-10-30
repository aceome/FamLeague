from django.shortcuts import render, reverse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from .models import Team

from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    teams = request.user.team_set.all().order_by('category')
    user_teams = {'teams': teams}
    return render(request, 'famleague/index.html', user_teams)

def login_view(request):
    return render(request, 'famleague/login.html')

# receives the form submission
def login_user(request):
    # retrieve the variables from the form submission
    username = request.POST['username'].capitalize()
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



def register_user(request):
    username = request.POST['username'].capitalize()
    email = request.POST['email']
    password = request.POST['password']
    user = User.objects.create_user(username, email, password)
    login(request, user)
    return HttpResponseRedirect(reverse('famleague:index'))



@login_required
def rules(request):
    return render(request, 'famleague/rules.html')


@login_required
def lineup(request, category):
    teams = Team.objects.filter(category=category).order_by('-score_2018')
    user_teams = {'teams': teams, 'category': category}
    # a_btn = request.user.POST('a_btn')
    return render(request, 'famleague/lineup.html', user_teams)


@login_required
def pick_team(request, team_id):
    # look up the team with that id
    id = request.POST['id']
    team_id = Team.objects.get(pk=id)
    # the user is request.user
    user = request.user
    # add the team to the user's list of teams
    user.team_id.save()
    return HttpResponseRedirect(reverse('famleague:lineup', kwargs={'lineup': 'category'}))




@login_required
def leader(request):
    return render(request, 'famleague/leader.html')
