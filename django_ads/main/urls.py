from .views import other_page, CustomLoginView, CustomLogoutView, profile, ProfileEditView, PasswordEditView
from django.urls import path

from .views import index

app_name = "main"

urlpatterns = [
    path('accounts/logout/', CustomLogoutView.as_view(), name='logout'),
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('accounts/password/edit/', PasswordEditView.as_view(), name='password_edit'),
    path('accounts/profile/edit/', ProfileEditView.as_view(), name='profile_edit'),
    path('accounts/profile/', profile, name='profile'),
    path('<str:page>/', other_page, name='other'),
    path("", index, name='index')
]
