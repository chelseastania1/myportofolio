from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from main.models import Experience
from main.models import Education


class MainTest(TestCase):
    def setUp(self):
        self.experience = Experience.objects.create(
            title="Asisten Dosen PBP",
            description="Membantu mahasiswa memahami pengembangan web.",
            category="part-time",
        )
        self.education = Education.objects.create(
                    title="Universitas Indonesia",
                    description="S1 Ilmu Komputer",
                    category="bachelors",
        )

    def test_main_url_is_accessible(self):
        response = self.client.get(reverse("main:show_main"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")
        self.assertNotContains(response, self.experience.title)
        self.assertContains(response, f'href="{reverse("main:show_experience")}"')

    def test_nonexistent_page_returns_404(self):
        response = self.client.get("/halaman-yang-tidak-ada/")

        self.assertEqual(response.status_code, 404)

    def test_experience_model(self):
        self.assertEqual(str(self.experience), "Asisten Dosen PBP")
        self.assertEqual(self.experience.category, "part-time")
        self.assertTrue(self.experience.is_ongoing)

    def test_experience_page(self):
        response = self.client.get(reverse("main:show_experience"))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "experience.html")
        self.assertContains(response, self.experience.title)
        self.assertContains(response, self.experience.description)
        self.assertContains(response, "Part-Time")
        self.assertContains(response, "Sedang berlangsung")
        self.assertContains(response, f'href="{reverse("main:show_main")}"')

    def test_empty_experience_page(self):
        Experience.objects.all().delete()
        response = self.client.get(reverse("main:show_experience"))

        self.assertContains(response, "Belum ada pengalaman yang ditambahkan.")

    def test_completed_experience(self):
        self.experience.ended_at = timezone.now()
        self.experience.save()
        response = self.client.get(reverse("main:show_experience"))

        self.assertFalse(self.experience.is_ongoing)
        self.assertContains(response, "Selesai")
        self.assertNotContains(response, "Sedang berlangsung")

    def test_education_page(self):
            response = self.client.get(reverse("main:show_education"))
    
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, "education.html")
            self.assertContains(response, self.education.title)
            self.assertContains(response, self.education.description)
            self.assertContains(response, "Bachelor")
            self.assertContains(response, "Sedang berlangsung")
            self.assertContains(response, f'href="{reverse("main:show_main")}"')

    def test_education_model(self):
        self.assertEqual(str(self.education), "Universitas Indonesia")
        self.assertEqual(self.education.category, "bachelors")
        self.assertTrue(self.education.is_ongoing)

    def test_empty_education_page(self):
            Education.objects.all().delete()
            response = self.client.get(reverse("main:show_education"))
            self.assertContains(response, "Riwayat pendidikan belum ditambahkan.")

    def test_completed_education(self):
            self.education.end_year = 2024
            self.education.save()
            response = self.client.get(reverse("main:show_education"))

            self.assertFalse(self.education.is_ongoing)
            self.assertContains(response, "Selesai")
            self.assertNotContains(response, "Sedang berlangsung")