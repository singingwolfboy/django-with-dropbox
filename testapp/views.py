from django.shortcuts import render

def index(request):
    print(request.user)
    return render(request, "index.html")
