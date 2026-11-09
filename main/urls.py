from django.urls import path

from main import views
from django.urls import include, path

app_name = "main"

urlpatterns = [
    path("", views.show_main, name="show_main"),
    path("experience/", views.show_experience, name="show_experience"),
    path("education/", views.show_education, name="show_education"),
    path("certifications/", views.show_certifications, name="show_certifications"),
    path("certifications/add/", views.create_certification, name="create_certification"),
    path("certifications/<uuid:certification_id>/edit/", views.edit_certification, name="edit_certification"),
    path("api/certifications/", views.get_certification_json, name="get_certification_json"),
    path("certifications/<uuid:certification_id>/delete/",views.delete_certification,name="delete_certification"),
    path("education/add/", views.create_education, name="create_education"),
    path("api/education/", views.get_education_json, name="get_education_json"),
    path("education/<uuid:education_id>/delete/",views.delete_education,name="delete_education"),
    path("register/", views.register, name="register"),
    path("login/", views.login_user, name="login"),
    path("logout/", views.logout_user, name="logout"),
    path("education/<uuid:education_id>/star/", views.toggle_education_star, name="toggle_education_star",),
    path("certifications/<uuid:certification_id>/star/", views.toggle_certification_star, name="toggle_certification_star",),
    path("education/add-ajax/", views.create_education_ajax, name="create_education_ajax"),
    path("certifications/add-ajax/", views.create_certification_ajax, name="create_certification_ajax"),
    path("api/v1/", include("main.api_urls")),
    path("api-auth/", include("rest_framework.urls")),
]