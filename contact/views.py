from django.shortcuts import render
from rest_framework import viewsets
from .models import ContactMessage
from .serializers import ContactMessageSerializer

class ContactMessageViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all().order_by('-sent_at')
    serializer_class = ContactMessageSerializer


def contact_form(request):
    # Contact form page.
    return render(request, 'contact/contact.html')
