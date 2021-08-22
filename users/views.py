from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect                                  

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    else :
        return render(request, "users/index.html")

def log_in(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:    
            return render(request, "users/login.html",{
                "message" : "Invalid Credentials!"
            })
    return render(request, "users/login.html")

def log_out(request):
    logout(request)
    return render(request, "users/login.html",{
        "message" : "Logged Out!"
    })
