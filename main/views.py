from django.shortcuts import render
from django.contrib import messages
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required, permission_required
from django.core.exceptions import PermissionDenied
from django.views.decorators.http import require_POST
from main.forms import EducationForm, CertificationForm
from main.models import Experience, Education, Certifications
import datetime


def show_main(request):
    last_login = request.COOKIES.get('last_login', 'Belum ada sesi login / Cookie tidak ditemukan')
    context = {
        "name": "Chelsea Stania Passikha",
        "npm": "2506587876",
        "study_program": "S1 Sistem Informasi",
        "bio": (
            "Mahasiswa Sistem Informasi Universitas Indonesia yang tertarik "
            "pada pengembangan perangkat lunak dan pendidikan."
        ),
        "last_login": last_login,
    }
    return render(request, "index.html", context)


def show_experience(request):
    context = {
        "name": "Chelsea Stania Passikha",
        "experience_list": Experience.objects.all(),
    }
    return render(request, "experience.html", context)

def show_education(request):
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Chelsea Stania Passikha",
        "title_query": title_query,
    }
    return render(request, "education.html", context)

@login_required(login_url="/login/")
def create_education(request):
    if not request.user.is_superuser:
        raise PermissionDenied
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
    education = Education.objects.prefetch_related('starred_by').all()

    if title_query:
        education = education.filter(title__icontains=title_query)

    # Konstruksi data JSON secara manual agar bisa menyisipkan logika Star
    data = []
    for education in education:
        starred_users = education.starred_by.all()
        is_starred = request.user in starred_users if request.user.is_authenticated else False
        starred_by_names = ", ".join([u.username for u in starred_users])

        data.append({
            "pk": str(education.id),
            "fields": {
                "title": education.title,
                "description": education.description,
                "category": education.category,
                "start_year": education.start_year,
                "end_year": education.end_year,
                "star_count": starred_users.count(),
                "is_starred": is_starred,
                "starred_by_names": starred_by_names,

            }
        })

    return JsonResponse(data, safe=False)

@login_required(login_url="/login/")
def delete_education(request, education_id):
    if not request.user.is_superuser:
        raise PermissionDenied
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

@permission_required("main.add_certifications", raise_exception=True)
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

@permission_required("main.change_certifications", raise_exception=True)
def edit_certification(request, certification_id):
    certification = get_object_or_404(Certifications, pk=certification_id)
    form = CertificationForm(request.POST, instance=certification)

    if request.method == "POST":
        form = CertificationForm(request.POST, instance=certification)
    if form.is_valid():
        form.save()
        messages.success(request, "Informasi sertifikasi berhasil diubah!")
        return redirect("main:show_certifications")
    
    else:
        form = CertificationForm(request.POST, instance=certification)

    context = {
        "name": "Chelsea Stania Passikha",
        "form": form,
        "certification": certification,
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

@permission_required("main.delete_certifications", raise_exception=True)
def delete_certification(request, certification_id):
    certification = get_object_or_404(Certifications, pk=certification_id)

    if request.method == "POST":
        certification.delete()
        messages.success(request, "Informasi sertifikasi berhasil dihapus!")
        return redirect("main:show_certifications")

    return redirect("main:show_certifications")

def register(request):
    form = UserCreationForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Akun berhasil dibuat. Silakan login.")
        return redirect("main:login")

    context = {
        "name": "Chelsea Stania Passikha",
        "form": form,
    }
    return render(request, "register.html", context)

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        user = form.get_user()
        login(request, user)
        response = redirect("main:show_main")
        response.set_cookie('last_login', datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        return response

    context = {
        "name": "Chelsea Stania Passikha",
        "form": form,
    }
    return render(request, "login.html", context)

def login_user(request):
    form = AuthenticationForm(request, data=request.POST or None)

    if request.method == "POST" and form.is_valid():
        login(request, form.get_user())
        return redirect("main:show_main")

    context = {
        "name": "Chelsea Stania Passikha",
        "form": form,
    }
    return render(request, "login.html", context)

def logout_user(request):
    logout(request)
    response = redirect("main:show_main")
    response.delete_cookie('last_login')
    return response

@login_required(login_url="/login/")
def toggle_education_star(request, education_id):
    education = get_object_or_404(Education, pk=education_id)

    if request.method == "POST":
        # Kalau akun ini sudah pernah memberi star, batalkan star-nya.
        # Kalau belum, tambahkan star.
        if request.user in education.starred_by.all():
            education.starred_by.remove(request.user)
        else:
            education.starred_by.add(request.user)

    return redirect("main:show_education")

@login_required(login_url="/login/")
def toggle_certification_star(request, certification_id):
    certification = get_object_or_404(Certifications, pk=certification_id)

    if request.method == "POST":
        if request.user in certification.starred_by.all():
            certification.starred_by.remove(request.user)
        else:
            certification.starred_by.add(request.user)

    return redirect("main:show_certifications")

def show_education(request):
    title_query = request.GET.get("title", "").strip()

    context = {
        "name": "Chelsea Stania Passikha",
        "title_query": title_query,
        "form": EducationForm(),
    }
    return render(request, "education.html", context)

@require_POST
def create_education_ajax(request):
    if not request.user.is_superuser:
        return JsonResponse(
            {"message": "Hanya pemilik portofolio yang dapat menambahkan pendidikan."},
            status=403,
        )

    form = EducationForm(request.POST)
    if form.is_valid():
        education = form.save()
        return JsonResponse(
            {"message": "Informasi pendidikan berhasil ditambahkan.", "pk": str(education.id)},
            status=201,
        )

    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)
