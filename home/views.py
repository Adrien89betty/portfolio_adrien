from django.shortcuts import render
from contact.forms import ContactMessageForm

def index(request):
    # Portfolio homepage.
    form = ContactMessageForm()
    return render(request, 'home/index.html', {"form": form})
