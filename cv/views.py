from django.shortcuts import render
from rest_framework import viewsets
from .models import Skill, Certification, CV
from .serializers import SkillSerializer, CertificationSerializer, CVSerializer

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class CertificationViewSet(viewsets.ModelViewSet):
    queryset = Certification.objects.all()
    serializer_class = CertificationSerializer

class CVViewSet(viewsets.ModelViewSet):
    queryset = CV.objects.all()
    serializer_class = CVSerializer

def cv(request):
    # CV page.
    return render(request, 'cv/cv.html')
