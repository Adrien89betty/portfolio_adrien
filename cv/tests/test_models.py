from django.test import TestCase
from cv.models import Skill, Certification, CV
from datetime import date

class SkillModelTest(TestCase):
    def setUp(self):
        self.skill = Skill.objects.create(
            name="Python",
            category="Programming Language"
        )

    def test_skill_creation(self):
        self.assertEqual(self.skill.name, "Python")
        self.assertEqual(self.skill.category, "Programming Language")

    def test_skill_update(self):
        self.skill.name = "Django"
        self.skill.save()
        updated_skill = Skill.objects.get(id=self.skill.id)
        self.assertEqual(updated_skill.name, "Django")

    def test_skill_deletion(self):
        skill_id = self.skill.id
        self.skill.delete()
        with self.assertRaises(Skill.DoesNotExist):
            Skill.objects.get(id=skill_id)

    def test_str_method(self):
        self.assertEqual(str(self.skill), "Python")


class CertificationModelTest(TestCase):
    def setUp(self):
        self.certification = Certification.objects.create(
            title="Python Developer Certificate",
            institution="Python Institute",
            date_obtained=date(2023, 5, 1),
            description="A certificate for mastering Python programming.",
            logo=None
        )

    def test_certification_creation(self):
        self.assertEqual(self.certification.title, "Python Developer Certificate")
        self.assertEqual(self.certification.institution, "Python Institute")
        self.assertEqual(self.certification.date_obtained, date(2023, 5, 1))
        self.assertEqual(self.certification.description, "A certificate for mastering Python programming.")
        self.assertFalse(self.certification.logo)

    def test_certification_update(self):
        self.certification.title = "Advanced Python Developer Certificate"
        self.certification.save()
        updated_certification = Certification.objects.get(id=self.certification.id)
        self.assertEqual(updated_certification.title, "Advanced Python Developer Certificate")

    def test_certification_deletion(self):
        certification_id = self.certification.id
        self.certification.delete()
        with self.assertRaises(Certification.DoesNotExist):
            Certification.objects.get(id=certification_id)

    def test_str_method(self):
        self.assertEqual(str(self.certification), "Python Developer Certificate")


class CVModelTest(TestCase):
    def setUp(self):
        self.cv = CV.objects.create(
            file="cv_files/test_cv.pdf"
        )

    def test_cv_creation(self):
        self.assertEqual(self.cv.file, "cv_files/test_cv.pdf")
        self.assertIsNotNone(self.cv.updated_at)

    def test_cv_update(self):
        self.cv.file = "cv_files/updated_cv.pdf"
        self.cv.save()
        updated_cv = CV.objects.get(id=self.cv.id)
        self.assertEqual(updated_cv.file, "cv_files/updated_cv.pdf")

    def test_cv_deletion(self):
        cv_id = self.cv.id
        self.cv.delete()
        with self.assertRaises(CV.DoesNotExist):
            CV.objects.get(id=cv_id)

    def test_str_method(self):
        self.assertTrue("CV updated at" in str(self.cv))
