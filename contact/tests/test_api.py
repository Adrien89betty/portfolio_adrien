from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from contact.models import ContactMessage


class ContactMessageAPITestCase(APITestCase):

    def setUp(self):
        self.message1 = ContactMessage.objects.create(
            name="John Doe",
            email="john.doe@example.com",
            message="This is a test message."
        )
        self.message2 = ContactMessage.objects.create(
            name="Jane Doe",
            email="jane.doe@example.com",
            message="Another test message."
        )
        self.list_url = reverse('contact:contactmessage-list')

    def test_get_contact_messages_list(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_single_contact_message(self):
        url = reverse('contact:contactmessage-detail', args=[self.message1.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.message1.name)
        self.assertEqual(response.data['email'], self.message1.email)
        self.assertEqual(response.data['message'], self.message1.message)

    def test_create_contact_message(self):
        data = {
            "name": "Alice",
            "email": "alice@example.com",
            "message": "This is Alice's message."
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ContactMessage.objects.count(), 3)

    def test_update_contact_message(self):
        url = reverse('contact:contactmessage-detail', args=[self.message1.id])
        updated_data = {
            "name": "John Updated",
            "email": "john.updated@example.com",
            "message": "Updated test message."
        }
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.message1.refresh_from_db()
        self.assertEqual(self.message1.name, "John Updated")
        self.assertEqual(self.message1.email, "john.updated@example.com")
        self.assertEqual(self.message1.message, "Updated test message.")

    def test_delete_contact_message(self):
        url = reverse('contact:contactmessage-detail', args=[self.message1.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(ContactMessage.objects.count(), 1)
