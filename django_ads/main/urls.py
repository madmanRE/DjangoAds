from .views import other_page, CustomLoginView
from django.urls import path

from .views import index

app_name = "main"

urlpatterns = [
    path('accounts/login/', CustomLoginView.as_view(), name='login'),
    path('<str:page>/', other_page, name='other'),
    path("", index, name='index')
]
