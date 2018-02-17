from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to Fanswarm!")

def login(request):
    return HttpResponse("This is where someone would login.")

def user_create(request):
    return HttpResponse("This is where a user would create their profile.")

def user_edit(request):
    return HttpResponse("This is where a user would edit their profile.")

def user_display(request):
    return HttpResponse("This is where a user would view their profile.")

def events(request):
    return HttpResponse("This is where a user can view all of the events.")

def event_create(request):
    return HttpResponse("This is where a user would create an event.")

def event_edit(request):
    return HttpResponse("This is where a user would edit an event.")

def event_display(request):
    return HttpResponse("This is where a user would view the event")
