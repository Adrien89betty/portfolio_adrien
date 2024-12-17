from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import ProjectViewSet

router = DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='project')

app_name = 'projects'
urlpatterns = [
    # Projects page.
    path('', views.projects, name='projects'),
    # API REST.
    path('api/', include(router.urls)),
]
