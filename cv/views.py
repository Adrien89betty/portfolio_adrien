from django.shortcuts import render

def cv(request):
    # CV page.
    return render(request, 'cv/cv.html')
