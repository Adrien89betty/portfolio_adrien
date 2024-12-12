from django.urls import path
from . import views

app_name = 'projects'
urlpatterns = [
    # Projects page.
    path('', views.projects, name='projects'),
]
