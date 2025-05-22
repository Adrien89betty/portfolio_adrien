from django.core.management.base import BaseCommand
from contact.models import ContactMessage
from faker import Faker
import random

class Command(BaseCommand):
    help = "Creates fake Contact messages for the database."

    def handle(self, *args, **kwargs):
        fake = Faker()

        for _ in range(20):
            ContactMessage.objects.create(
                name=fake.name(),
                email=fake.ascii_email(),
                message=fake.paragraph(nb_sentences=5),
            )
        self.stdout.write(self.style.SUCCESS("20 fake contact messages has been created."))
