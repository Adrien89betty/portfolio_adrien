from django.shortcuts import render

def about(request):
    # About page.
    return render(request, 'about/about.html')
