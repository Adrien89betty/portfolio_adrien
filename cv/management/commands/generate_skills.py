from django.core.management.base import BaseCommand
from cv.models import Skill


class Command(BaseCommand):
    help = "Generates skills."

    def handle(self, *args, **options):
        Skill.objects.all().delete()
        SKILLS = [
            {"name": "Python", "category": "Hard", "logo": "logo_python.svg"},
            {"name": "Django", "category": "Hard", "logo": "logo_dj.svg"},
            {"name": "HTML 5", "category": "Hard", "logo": "logo_html.svg"},
            {"name": "CSS 3", "category": "Hard", "logo": "logo_css.svg"},
            {"name": "Ruby", "category": "Hard", "logo": "logo_ruby.svg"},
            {"name": "JavaScript", "category": "Hard", "logo": "logo_js.svg"},
            {"name": "Vue.js", "category": "Hard", "logo": "logo_vue.svg"},
            {"name": "PostgreSQL", "category": "Hard", "logo": "logo_postgre.svg"},
            {"name": "SQL", "category": "Hard", "logo": "logo_sql.svg"},
            {"name": "Git", "category": "Hard", "logo": "logo_git.svg"},
            {"name": "Terminal", "category": "Hard", "logo": "logo_terminal.svg"},
            {"name": "VSCode", "category": "Hard", "logo": "logo_vscode.svg"},
            {"name": "Mac OS X", "category": "Hard", "logo": "logo_osx.svg"},
        ]

        for entry in SKILLS:
            # Create skill
            skill = Skill.objects.create(
                name=entry["name"],
                category=entry["category"],
                logo=entry["logo"],
            )

            self.stdout.write(self.style.SUCCESS(f"Skill « {skill.name} » recorded in database."))
