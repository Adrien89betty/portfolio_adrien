from rest_framework import serializers
from .models import Skill, Certification, CV

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = '__all__'

class CertificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certification
        fields = '__all__'

class CVSerializer(serializers.ModelSerializer):
    class Meta:
        model = CV
        fields = '__all__'
