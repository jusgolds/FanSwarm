from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to Fanswarm!")

def login(request):
    return HttpResponse("This is where someone would login.")
