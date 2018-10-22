from django.urls import path

from . import views


app_name = 'famleague'
urlpatterns = [
    path('', views.index, name='index'),
    path('index/', views.mylogin, name='mylogin'),
    path('index/', views.logout_view, name='logout_view'),
    path('register/', views.register, name='register'),
    path('main/', views.main, name='main'),
    path('rules/', views.rules, name='rules'),
    path('leader/', views.leader, name='leader'),
    path('lineup/', views.lineup, name='lineup')

]
