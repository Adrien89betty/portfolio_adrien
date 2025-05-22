# projects/management/commands/fake_projects.py
import random
from django.core.management.base import BaseCommand
from projects.models import Project
from faker import Faker

class Command(BaseCommand):
    help = "Creates 3 fake projects with specified image."

    def handle(self, *args, **options):
        Project.objects.all().delete()
        fake = Faker()
        IMG_FILES = ["img_code.jpg", "img_portfolio.jpg", "img_scrapping.jpg"]

        project1 = Project.objects.create(
                title=fake.sentence(nb_words=2),
                description=fake.paragraph(nb_sentences=5),
                technologies=fake.random_elements(
                    elements=["Python", "Django", "Vue.js", "PostgreSQL", "API", "Scraping"],
                    length=random.randint(2, 6)
                ),
                github_link=fake.url(),
                demo_link=fake.url(),
                image=IMG_FILES[0]
            )
        self.stdout.write(self.style.SUCCESS(f"project « {project1.title} » recorded in database."))

        project2 = Project.objects.create(
                title=fake.sentence(nb_words=2),
                description=fake.paragraph(nb_sentences=5),
                technologies=fake.random_elements(
                    elements=["Python", "Django", "Vue.js", "PostgreSQL", "API", "Scraping"],
                    length=random.randint(2, 6)
                ),
                github_link=fake.url(),
                demo_link=fake.url(),
                image=IMG_FILES[1]
            )
        self.stdout.write(self.style.SUCCESS(f"project « {project2.title} » recorded in database."))

        project3 = Project.objects.create(
                title=fake.sentence(nb_words=2),
                description=fake.paragraph(nb_sentences=5),
                technologies=fake.random_elements(
                    elements=["Python", "Django", "Vue.js", "PostgreSQL", "API", "Scraping"],
                    length=random.randint(2, 6)
                ),
                github_link=fake.url(),
                demo_link=fake.url(),
                image=IMG_FILES[2]
            )
        self.stdout.write(self.style.SUCCESS(f"project « {project3.title} » recorded in database."))
