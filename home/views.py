from django.shortcuts import render

def index(request):
    # Portfolio homepage.
    return render(request, 'home/index.html')
