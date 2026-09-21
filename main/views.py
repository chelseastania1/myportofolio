from django.shortcuts import render
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from main.forms import EducationForm, CertificationForm
from main.models import Experience, Education, Certifications


def show_main(request):
    context = {
        "name": "Chelsea Stania Passikha",
        "npm": "2506587876",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "Mahasiswa Sistem Informasi Universitas Indonesia yang tertarik "
            "pada pengembangan perangkat lunak dan pendidikan."
        ),
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Chelsea Stania Passikha",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_education(request):
    json_response = get_education_json(request)

    education = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    education = [education.object for education in education]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Chelsea Stania Passikha",
        "education_list": education,
        "title_query": title_query,
    }
    return render(request, "education.html", context)

def create_education(request):
    form = EducationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Informasi pendidikan berhasil ditambahkan!")
        return redirect("main:show_education")

    context = {
        "name": "Chelsea Stania Passikha",
        "form": form,
    }
    return render(request, "education_form.html", context)

def get_education_json(request):
    title_query = request.GET.get("title", "").strip()
    education = Education.objects.all()

    if title_query:
        education = education.filter(title__icontains=title_query)

    education_json = serializers.serialize("json", education)
    return HttpResponse(education_json, content_type="application/json")

def delete_education(request, education_id):
    education = get_object_or_404(Education, pk=education_id)

    if request.method == "POST":
        education.delete()
        messages.success(request, "Informasi pendidikan berhasil dihapus!")
        return redirect("main:show_education")

    return redirect("main:show_education")

def show_certifications(request):
    json_response = get_certification_json(request)

    certifications = serializers.deserialize(
        "json",
        json_response.content.decode("utf-8"),
    )
    certifications = [certification.object for certification in certifications]
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Chelsea Stania Passikha",
        "certification_list": certifications,
        "title_query": title_query,
    }
    return render(request, "certifications.html", context)

def create_certification(request):
    form = CertificationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Informasi sertifikasi berhasil ditambahkan!")
        return redirect("main:show_certifications")

    context = {
        "name": "Chelsea Stania Passikha",
        "form": form,
    }
    return render(request, "certifications_form.html", context)

def get_certification_json(request):
    title_query = request.GET.get("title", "").strip()
    certifications = Certifications.objects.all()

    if title_query:
        certifications = Certifications.objects.filter(
            title__icontains=title_query
        )

    certifications_json = serializers.serialize("json", certifications)
    return HttpResponse(certifications_json, content_type="application/json")

def delete_certification(request, certification_id):
    certification = get_object_or_404(Certifications, pk=certification_id)

    if request.method == "POST":
        certification.delete()
        messages.success(request, "Informasi sertifikasi berhasil dihapus!")
        return redirect("main:show_certifications")

    return redirect("main:show_certifications")