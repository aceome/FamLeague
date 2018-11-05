from django.shortcuts import render, reverse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from .models import Team
# from . models import TeamScore

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
    return HttpResponseRedirect(reverse('famleague:rules'))



@login_required
def rules(request):
    return render(request, 'famleague/rules.html')


@login_required
def lineup(request, category):
    teams = Team.objects.filter(category=category).order_by('-score_2018')
    user_teams = {'teams': teams, 'category': category}
    return render(request, 'famleague/lineup.html', user_teams)


@login_required
def pick_team(request, team_id):
    # look up the team with that id
    team = Team.objects.get(pk=team_id)
    user = request.user
    flag = False
    for one_team in user.team_set.all():
        if one_team.category == team.category:
            flag = True
    if flag:
        team.users.remove(user)
    # add the team to the user's list of teams
    else:
        team.users.add(user)
    return HttpResponseRedirect(reverse('famleague:lineup', kwargs={'category': 'team'}))


@login_required
def leader(request):
    # get all the teams
    teams = Team.objects.all()
    # create a score list
    team_scores = []
    # iterate over the teams and create a dictionary for table
    for team in teams:
        team_scores.append({
            'team': team.name,
            'score': team.score_2019,
            'category': team.category
        })
    team_scores.sort(key=lambda x: x['score'], reverse=True)
    team_scores.sort(key=lambda x: x['category'])

    # get all the users
    users = User.objects.all()
    user_scores = []
    # iterate over users
    for user in users:
        user_score = 0
        for team in user.team_set.all():
            user_score += team.score_2019
        user_scores.append({'username': user.username, 'score': user_score})
    user_scores.sort(key=lambda x: x['score'], reverse=True)

    context = {'user_scores': user_scores, 'team_scores': team_scores}
    return render(request, 'famleague/leader.html', context)
