from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Hello Blog 👋</h1><p>This is your first Django app!</p>")
