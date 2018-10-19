from django.shortcuts import render, reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'famleague/index.html')




def mylogin(request):
    # retrieve the variables from the form submission
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect('famleague:main')
    else:
        pass
        # return an 'invalid login' error message

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('famleague:index'))
    # redirect to a success page.
