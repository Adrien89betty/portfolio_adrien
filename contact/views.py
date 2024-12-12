from django.shortcuts import render

def contact_form(request):
    # Contact form page.
    return render(request, 'contact/contact.html')
