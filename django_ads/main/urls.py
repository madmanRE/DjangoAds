from .views import (
    other_page,
    CustomLoginView,
    CustomLogoutView,
    profile,
    ProfileEditView,
    PasswordEditView,
    RegisterView,
    RegisterDoneView,
    user_activate,
    ProfileDeleteView,
    rubric_bbs,
    bb_detail,
)
from django.urls import path

from .views import index

app_name = "main"

urlpatterns = [
    path("accounts/activate/<str:sign>/", user_activate, name="activate"),
    path("accounts/register/done/", RegisterDoneView.as_view(), name="register_done"),
    path("accounts/register/", RegisterView.as_view(), name="register"),
    path("accounts/logout/", CustomLogoutView.as_view(), name="logout"),
    path("accounts/login/", CustomLoginView.as_view(), name="login"),
    path("accounts/password/edit/", PasswordEditView.as_view(), name="password_edit"),
    path(
        "accounts/profile/delete/", ProfileDeleteView.as_view(), name="profile_delete"
    ),
    path("accounts/profile/edit/", ProfileEditView.as_view(), name="profile_edit"),
    path("accounts/profile/", profile, name="profile"),
    path("<int:rubric_pk>/<int:pk>/", bb_detail, name="bb_detail"),
    path("<int:pk>/", rubric_bbs, name="rubric_bbs"),
    path("<str:page>/", other_page, name="other"),
    path("", index, name="index"),
]
