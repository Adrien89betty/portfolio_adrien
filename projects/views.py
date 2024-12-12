from django.shortcuts import render

def projects(request):
    # Projects page.
    return render(request, 'projects/projects.html')
