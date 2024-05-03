from django.urls import path

from . import views

app_name = "accounts"

urlpatterns = [
    path("signup/", views.SignUpView.as_view(), name='signup'),
    path("profile/", views.profile, name='profile'),
    path("update/", views.profile_update_view, name='update'),
]