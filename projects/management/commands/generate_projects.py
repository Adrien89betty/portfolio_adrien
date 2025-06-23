# projects/management/commands/fake_projects.py
import random
from django.core.management.base import BaseCommand
from projects.models import Project
from faker import Faker

class Command(BaseCommand):
    help = "Creates projects with specified image."

    def handle(self, *args, **options):
        Project.objects.all().delete()
        fake = Faker()
        IMG_FILES = ["img_code.jpg", "img_portfolio.jpg", "img_scrapping.jpg"]

        project1 = Project.objects.create(
                title="Ce Portfolio",
                description="""Ce portfolio est un site web personnel conçu pour présenter mon profil de développeur full stack, mes compétences techniques, mes projets réalisés ainsi qu’un moyen de me contacter et il est entièrement responsive.

                Sur le plan de l’architecture, le site repose sur une séparation entre le back-end et le front-end. Le back-end est développé avec Django et expose les données via des API REST construites avec Django REST Framework.

                Les données sont stockées dans une base de données PostgreSQL, robuste et adaptée à la production et sont ensuite récupérées dynamiquement par le front-end, développé avec Vue.js (intégré via CDN), qui s’occupe du rendu côté client.

                Cette approche permet une grande flexibilité, une meilleure scalabilité et une séparation claire des responsabilités dans le code.""",
                technologies=["Python", "Django", "Django REST Framework", "JavaScript", "Vue.js", "HTML5", "CSS3", "PostgreSQL", "Git", "Heroku"],
                github_link="https://github.com/Adrien89betty/portfolio_adrien",
                demo_link="https://www.adrienleveille.com/",
                image=IMG_FILES[1]
            )
        self.stdout.write(self.style.SUCCESS(f"project « {project1.title} » recorded in database."))

        project2 = Project.objects.create(
                title="Smart Scraper",
                description="""Smart Scraper est un projet de scraping web modulaire développé avec Scrapy et Scrapy-Playwright.

                Conçu pour extraire les données produits des sites e-commerce, il est configurable via des fichiers JSON validés avec Pydantic.

                Il se compose d'un spider principal qui extrait les données détaillées des produits et d'un spider auxiliaire qui extrait les URLs de détails d produit depuis une page de collection de produits.

                De plus, un script utilitaire est fourni pour convertir les objets JSON de la sortie du spider auxiliaire en une liste Python d'URLs adaptées aux fichiers de configuration JSON.""",
                technologies=["Python", "Scrapy", "Playwright", "JSON", "Xpath", "JSON-LD"],
                github_link="https://github.com/Adrien89betty/smart-scraping",
                demo_link="https://www.adrienleveille.com/#projects-section",
                image=IMG_FILES[2]
            )
        self.stdout.write(self.style.SUCCESS(f"project « {project2.title} » recorded in database."))

        project3 = Project.objects.create(
                title="Un autre ;-)",
                description="Le projet sera visible prochainement",
                technologies=["..."],
                github_link=fake.url(),
                demo_link=fake.url(),
                image=IMG_FILES[0]
            )
        self.stdout.write(self.style.SUCCESS(f"project « {project3.title} » recorded in database."))
