from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import SkillViewSet, CertificationViewSet, CVViewSet

router = DefaultRouter()
router.register(r'skills', SkillViewSet, basename='skill')
router.register(r'certifications', CertificationViewSet, basename='certification')
router.register(r'cv', CVViewSet, basename='cv')

app_name = 'cv'
urlpatterns = [
    # CV page.
    path('', views.cv, name='cv'),
    # API REST urls.
    path('api/', include(router.urls)),
]
