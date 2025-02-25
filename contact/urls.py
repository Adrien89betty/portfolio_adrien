from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import ContactMessageViewSet

router = DefaultRouter()
router.register(r'messages', ContactMessageViewSet, basename='contactmessage')

app_name = 'contact'
urlpatterns = [
    # Contact form.
    path('form', views.contact_form, name='contact_form'),
    path("submit/", views.contact_view, name="contact_submit"),
    # API REST
    path('api/', include(router.urls)),
]
