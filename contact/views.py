from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import ContactMessage
from .serializers import ContactMessageSerializer
from .forms import ContactMessageForm

class ContactMessageViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all().order_by('-sent_at')
    serializer_class = ContactMessageSerializer


def contact_form(request):
    # Contact form page.
    return render(request, 'contact/contact.html')


def contact_view(request):
    form = ContactMessageForm()

    if request.method == "POST":
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home:index")

    return render(request, "contact/contact.html", {"form": form})
