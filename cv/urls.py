from django.urls import path
from . import views

app_name = 'cv'
urlpatterns = [
    # CV page.
    path('', views.cv, name='cv'),
]
