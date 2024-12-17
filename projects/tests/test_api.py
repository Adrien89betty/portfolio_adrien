from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from projects.models import Project

class ProjectAPITestCase(APITestCase):

    def setUp(self):
        self.project1 = Project.objects.create(
            title="Projet 1",
            description="Description du projet 1",
            technologies=["Python", "Django"],
            github_link="https://github.com/projet1",
            demo_link="https://demo1.com"
        )
        self.project2 = Project.objects.create(
            title="Projet 2",
            description="Description du projet 2",
            technologies=["Vue.js", "API REST"],
            github_link="https://github.com/projet2",
            demo_link="https://demo2.com"
        )
        self.valid_data = {
            "title": "API REST project",
            "description": "API creation with DRF.",
            "technologies": ["Django", "DRF", "PostgreSQL"],
            "github_link": "https://github.com/projet-api",
            "demo_link": "https://demo-projet.com",
            "image": None
        }
        self.invalid_data = {
            "title": "",  # empty field
            "description": "Projet invalide",
            "technologies": ["Test"],
            "github_link": "invalid_url",
            "demo_link": "invalid_demo"
        }
        self.list_url = reverse('projects:project-list')

    def test_get_projects_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_single_project(self):
        url = reverse('projects:project-detail', args=[self.project1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.project1.title)

    def test_create_valid_project(self):
        response = self.client.post(self.list_url, self.valid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Project.objects.count(), 3)

    def test_create_invalid_project(self):
        response = self.client.post(self.list_url, self.invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_project(self):
        url = reverse('projects:project-detail', args=[self.project1.id])
        updated_data = self.valid_data.copy()
        updated_data['title'] = "Projet 1 Modifié"
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.project1.refresh_from_db()
        self.assertEqual(self.project1.title, "Projet 1 Modifié")

    def test_delete_project(self):
        url = reverse('projects:project-detail', args=[self.project2.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Project.objects.count(), 1)
