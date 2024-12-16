from django.test import TestCase
from projects.models import Project


class ProjectModelTest(TestCase):
    def setUp(self):
        self.project = Project.objects.create(
            title="Test Project",
            description="This is a test project description.",
            technologies=["Python", "Django"],
            github_link="https://github.com/example/test_project",
            demo_link="https://example.com/demo",
            image=None,
        )

    def test_project_creation(self):
        self.assertEqual(self.project.title, "Test Project")
        self.assertEqual(self.project.description, "This is a test project description.")
        self.assertListEqual(self.project.technologies, ["Python", "Django"])
        self.assertEqual(self.project.github_link, "https://github.com/example/test_project")
        self.assertEqual(self.project.demo_link, "https://example.com/demo")
        self.assertFalse(self.project.image)
        self.assertIsNotNone(self.project.created_at)

    def test_str_method(self):
        self.assertEqual(str(self.project), "Test Project")

    def test_project_update(self):
        self.project.title = "Updated Project Title"
        self.project.description = "Updated description."
        self.project.save()

        updated_project = Project.objects.get(id=self.project.id)
        self.assertEqual(updated_project.title, "Updated Project Title")
        self.assertEqual(updated_project.description, "Updated description.")

    def test_project_deletion(self):
        project_id = self.project.id
        self.project.delete()

        with self.assertRaises(Project.DoesNotExist):
            Project.objects.get(id=project_id)
