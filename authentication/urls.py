from django.urls import path
from .views import UserRegisterView

urlpatterns = [path("auth/", UserRegisterView.as_view(), name="user-register-view")]
