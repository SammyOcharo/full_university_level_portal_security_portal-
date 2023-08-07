from django.urls import path
from . import views

urlpatterns = [
    path('security-login/', views.SecurityLoginAPIView.as_view(), name='security-login')
]