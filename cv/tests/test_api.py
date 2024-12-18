from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from cv.models import Skill, Certification

class SkillAPITestCase(APITestCase):

    def setUp(self):
        self.skill1 = Skill.objects.create(name="Python", category="Programming")
        self.skill2 = Skill.objects.create(name="VUE.js", category="Framework")
        self.list_url = reverse('cv:skill-list')

        self.valid_data = {
            "name": "Django",
            "category": "Framework"
        }

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
        updated_data = self.valid_data.copy()
        updated_data['name'] = "Skill1 Updated."
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.skill1.refresh_from_db()
        self.assertEqual(self.skill1.name, "Skill1 Updated.")

    def test_delete_skill(self):
        url = reverse('cv:skill-detail', args=[self.skill1.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Skill.objects.count(), 1)


class CertificationAPITestCase(APITestCase):

    def setUp(self):
        self.certif1 = Certification.objects.create(
            title="PCAP",
            institution="Python Institute",
            date_obtained="2024-11-15",
            description="Some description about it.",
            logo=None
        )
        self.certif2 = Certification.objects.create(
            title="PCEP",
            institution="Python Institute",
            date_obtained="2024-11-27",
            description="Some description about it.",
            logo=None
        )
        self.list_url = reverse('cv:certification-list')
        self.valid_data = {
            "title": "CERTIF",
            "institution": "Best Python devs",
            "date_obtained": "2022-04-8",
            "description": "This is a short description"
        }

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
            "title": "CERTIF",
            "institution": "Best Python devs",
            "date_obtained": "2022-04-8",
            "description": "This is a short description"
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Certification.objects.count(), 3)

    def test_update_certification(self):
        url = reverse('cv:certification-detail', args=[self.certif1.id])
        updated_data = self.valid_data.copy()
        updated_data['title'] = "Certif1 Updated."
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.certif1.refresh_from_db()
        self.assertEqual(self.certif1.title, "Certif1 Updated.")

    def test_delete_certification(self):
        url = reverse('cv:certification-detail', args=[self.certif1.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Certification.objects.count(), 1)
