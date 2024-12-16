from django.test import TestCase
from django.urls import reverse

class AboutViewTest(TestCase):
    def test_about_view_status_code(self):
        response = self.client.get(reverse('about:about'))
        self.assertEqual(response.status_code, 200)

    def test_about_view_template_used(self):
        response = self.client.get(reverse('home:index'))
        self.assertTemplateUsed(response, 'home/index.html')
