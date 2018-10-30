from django.urls import path

from . import views


app_name = 'famleague'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login_view'),
    path('login_user/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),
    path('register_user', views.register_user, name='register_user'),
    path('rules/', views.rules, name='rules'),
    path('leader/', views.leader, name='leader'),
    path('lineup/<str:category>/', views.lineup, name='lineup'),
    path('pick_team/<int:team_id>/', views.pick_team, name='pick_team')

]
