from django.core.management.base import BaseCommand
from cv.models import Certification
from faker import Faker
import random

class Command(BaseCommand):
    help = "Creates fake Certifications for the database."

    def handle(self, *args, **kwargs):
        fake = Faker()

        for _ in range(5):
            Certification.objects.create(
                title=fake.sentence(nb_words=3),
                institution=fake.company(),
                date_obtained=fake.date(),
                description=fake.paragraph(nb_sentences=5),
                logo=None
            )
        self.stdout.write(self.style.SUCCESS("5 fake certifications has been created."))
