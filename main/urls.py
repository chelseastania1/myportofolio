from django.urls import path

from main.views import (show_main, 
                        show_experience, 
                        show_education, 
                        create_education, 
                        get_education_json, 
                        delete_education,
                        show_certifications,
                        create_certification,
                        delete_certification,
                        get_certification_json,
                        register,
                        login_user,
                        logout_user, 
                        toggle_star
                        )

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("education/", show_education, name="show_education"),
    path("certifications/", show_certifications, name="show_certifications"),
    path("certifications/add/", create_certification, name="create_certification"),
    path("api/certifications/", get_certification_json, name="get_certification_json"),
    path("certifications/<uuid:certification_id>/delete/",delete_certification,name="delete_certification"),
    path("education/add/", create_education, name="create_education"),
    path("api/education/", get_education_json, name="get_education_json"),
    path("education/<uuid:education_id>/delete/",delete_education,name="delete_education"),
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("projects/<uuid:project_id>/star/", toggle_star, name="toggle_star",),
]