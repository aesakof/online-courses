from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<em>My Second App</em>")

def help(request):
    help_dict = {"insert_help_here":"Here is your help"}
    return render(request,"AppTwo/help.html",context=help_dict)
