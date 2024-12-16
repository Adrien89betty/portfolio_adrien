from django.test import TestCase
from contact.models import ContactMessage
from datetime import datetime

class ContactMessageModelTest(TestCase):
    def setUp(self):
        self.contact_message = ContactMessage.objects.create(
            name="John Doe",
            email="johndoe@example.com",
            message="This is a test message."
        )

    def test_contact_message_creation(self):
        self.assertEqual(self.contact_message.name, "John Doe")
        self.assertEqual(self.contact_message.email, "johndoe@example.com")
        self.assertEqual(self.contact_message.message, "This is a test message.")
        self.assertIsNotNone(self.contact_message.sent_at)

    def test_contact_message_update(self):
        self.contact_message.message = "Updated message."
        self.contact_message.save()
        updated_message = ContactMessage.objects.get(id=self.contact_message.id)
        self.assertEqual(updated_message.message, "Updated message.")

    def test_contact_message_deletion(self):
        contact_message_id = self.contact_message.id
        self.contact_message.delete()
        with self.assertRaises(ContactMessage.DoesNotExist):
            ContactMessage.objects.get(id=contact_message_id)

    def test_str_method(self):
        expected_str = f"Message from John Doe on {self.contact_message.sent_at}"
        self.assertEqual(str(self.contact_message), expected_str)
