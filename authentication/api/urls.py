from django.urls import path
from . import views

urlpatterns = [
    path('security-login/', views.SecurityLoginAPIView.as_view(), name='security-login'),
    path('security-login-approve/', views.SecurityLoginApproveAPIView.as_view(), name='security-login-approve'),
]