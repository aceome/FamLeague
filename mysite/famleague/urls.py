from django.urls import path

from . import views


app_name = 'famleague'
urlpatterns = [
    path('', views.index, name='index'),
    # path('check_out/', views.check_out, name='check_out'),
    # path('check_in/', views.check_in, name='check_in')

]