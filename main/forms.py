from django.forms import ModelForm, TextInput, Textarea, URLInput, NumberInput

from main.models import Education

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