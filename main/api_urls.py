from django.urls import path
from main import api_views

app_name = "api"
urlpatterns = [
    path("education/", api_views.education_list, name="education-list"),
    path("education/<uuid:education_id>/", api_views.education_detail, name="education-detail"),
    path("education/<uuid:education_id>/star/", api_views.education_star, name="education-star"),
    path("certifications/", api_views.certification_list, name="certification-list"),
    path("certifications/<uuid:certification_id>/", api_views.certification_detail, name="certification-detail"),
    path("certifications/<uuid:certification_id>/star/", api_views.certification_star, name="certification-star"),
]