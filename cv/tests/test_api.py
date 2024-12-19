import os
import shutil

from django.conf import settings
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from cv.models import Skill, Certification, CV


class SkillAPITestCase(APITestCase):

    def setUp(self):
        self.skill1 = Skill.objects.create(name="Python", category="Programming")
        self.skill2 = Skill.objects.create(name="Vue.js", category="Framework")
        self.list_url = reverse('cv:skill-list')

    def test_get_skills_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_single_skill(self):
        url = reverse('cv:skill-detail', args=[self.skill1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.skill1.name)

    def test_create_skill(self):
        data = {"name": "Django", "category": "Framework"}
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Skill.objects.count(), 3)

    def test_update_skill(self):
        url = reverse('cv:skill-detail', args=[self.skill1.id])
        updated_data = {"name": "Python Updated", "category": "Programming"}
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.skill1.refresh_from_db()
        self.assertEqual(self.skill1.name, "Python Updated")

    def test_delete_skill(self):
        url = reverse('cv:skill-detail', args=[self.skill1.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Skill.objects.count(), 1)


class CertificationAPITestCase(APITestCase):

    def setUp(self):
        self.certif1 = Certification.objects.create(
            title="PCAP", institution="Python Institute", date_obtained="2024-11-15"
        )
        self.certif2 = Certification.objects.create(
            title="PCEP", institution="Python Institute", date_obtained="2024-11-27"
        )
        self.list_url = reverse('cv:certification-list')

    def test_get_certifications_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_single_certification(self):
        url = reverse('cv:certification-detail', args=[self.certif1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.certif1.title)

    def test_create_certification(self):
        data = {
            "title": "Advanced Python",
            "institution": "OpenAI Academy",
            "date_obtained": "2023-05-10",
            "description": "Advanced certification in Python programming"
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Certification.objects.count(), 3)

    def test_update_certification(self):
        url = reverse('cv:certification-detail', args=[self.certif1.id])
        updated_data = {
            "title": "PCAP Updated",
            "institution": "Python Institute",
            "date_obtained": "2024-11-15",
        }
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.certif1.refresh_from_db()
        self.assertEqual(self.certif1.title, "PCAP Updated")

    def test_delete_certification(self):
        url = reverse('cv:certification-detail', args=[self.certif1.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Certification.objects.count(), 1)


class CVAPITestCase(APITestCase):

    def setUp(self):
        self.cv1 = CV.objects.create(file="cv_files/test1.pdf")
        self.cv2 = CV.objects.create(file="cv_files/test2.pdf")
        self.list_url = reverse('cv:cv-list')

    def test_get_cv_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_single_cv(self):
        url = reverse('cv:cv-detail', args=[self.cv1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        expected_url = f"http://testserver{self.cv1.file.url}"
        self.assertEqual(response.data['file'], expected_url)

    def test_create_cv(self):
        file_path = os.path.join(os.path.dirname(__file__), "assets/test_cv.pdf")
        with open(file_path, 'rb') as pdf:
            response = self.client.post(self.list_url, {"file": pdf}, format='multipart')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            self.assertEqual(CV.objects.count(), 3)

    def test_update_cv(self):
        url = reverse('cv:cv-detail', args=[self.cv1.id])
        file_path = os.path.join(os.path.dirname(__file__), "assets/test_cv.pdf")
        with open(file_path, 'rb') as pdf:
            updated_data = {"file": pdf}
            response = self.client.put(url, updated_data, format='multipart')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.cv1.refresh_from_db()
            self.assertTrue(self.cv1.file.name.startswith("cv_files/"))
            self.assertIn("test_cv", self.cv1.file.name)

    def test_delete_cv(self):
        url = reverse('cv:cv-detail', args=[self.cv1.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(CV.objects.count(), 1)

    def tearDown(self):
        media_path = settings.MEDIA_ROOT
        cv_files_path = os.path.join(media_path, "cv_files")
        if os.path.exists(cv_files_path):
            shutil.rmtree(cv_files_path)
