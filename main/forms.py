from django.forms import ModelForm, TextInput, Textarea, URLInput, NumberInput
from django import forms

from main.models import Education, Certifications

class EducationForm(ModelForm):
    class Meta:
        model = Education
        fields = [
            "title",
            "description",
            "category",
            "start_year",
            "end_year",
        ]

        labels = {
            "title": "Nama Lembaga Pendidikan",
            "description": "Deskripsi Riwayat Pendidikan",
            "category": "Kategori Pendidikan",
            "start_year": "Tahun Mulai",
            "end_year": "Tahun Selesai",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Universitas Indonesia",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Program Studi Ilmu Komputer",
                    "rows": 3,
                }
            ),
            "category": TextInput(
                attrs={
                    "placeholder": "bachelors",
                }
            ),
            "start_year": NumberInput(
                attrs={
                    "placeholder": "2021",
                }
            ),
            "end_year": NumberInput(
                attrs={
                    "placeholder": "2025",
                }
            ),
        }

class CertificationForm(forms.ModelForm):
    class Meta:
        model = Certifications
        fields = [
            "title",
            "description",
            "issued_at",
            "expires_at",
        ]

        labels = {
            "title": "Nama Sertifikasi",
            "description": "Deskripsi Sertifikasi",
            "issued_at": "Tanggal Mulai Berlaku",
            "expires_at": "Berlaku Hingga",
        }

        widgets = {
            "title": TextInput(
                attrs={
                    "placeholder": "Nama Sertifikasi",
                    "maxlength": 255,
                }
            ),
            "description": Textarea(
                attrs={
                    "placeholder": "Deskripsi Sertifikasi",
                    "rows": 3,
                }
            ),
            "issued_at": forms.DateInput(
            format="%Y-%m-%d",
            attrs={"type": "date"},
            ),

            "expires_at": forms.DateInput(
            format="%Y-%m-%d",
            attrs={"type": "date"},
            ),
        }