from django.urls import path
from . import views

urlpatterns = [
    path('security-login/', views.SecurityLoginAPIView.as_view(), name='security-login'),
    path('security-login-approve/', views.SecurityLoginApproveAPIView.as_view(), name='security-login-approve'),
    path('security-forgot-password/', views.SecurityForgotPasswordAPIView.as_view(), name='security-forgot-password-api'),
    path('security-verify-forgot-password/', views.SecurityVerifyOtpForgotPasswordAPIView.as_view(), name='security-verify-forgot-password-api'),
    path('security-new-password/', views.SecurityNewPasswordAPIView.as_view(), name='security-new-password-api'),
    path('security-resend-forgot-password-otp/', views.SecurityResendOtpAPIView.as_view(), name='security-resend-otp-api')
]