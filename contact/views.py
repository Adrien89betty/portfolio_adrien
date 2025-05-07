from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import ContactMessage
from .serializers import ContactMessageSerializer
from .forms import ContactMessageForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.core.mail import EmailMessage


class ContactMessageViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all().order_by('-sent_at')
    serializer_class = ContactMessageSerializer


def contact_form(request):
    # Contact form page.
    return render(request, 'contact/contact.html')


def contact_view(request):
    if request.method == "POST":
        form = ContactMessageForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            exp_email = cd['email']
            subject = f"Nouveau message de {cd['name']}"
            body = (
                f"Nom : {cd['name']}\n"
                f"Email : {cd['email']}\n\n"
                f"Message :\n{cd['message']}"
            )
            form.save()
            email = EmailMessage(
                subject=subject,
                body=body,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[settings.CONTACT_RECIPIENT],
                reply_to=[cd['email']],
            )
            email.send(fail_silently=False)
            
            return JsonResponse({"success": True, "message": "Votre message a bien été envoyé !"})
        else:
            return JsonResponse({"success": False, "message": "Veuillez corriger les erreurs du formulaire."})

    return JsonResponse({"success": False, "message": "Méthode non autorisée."})
