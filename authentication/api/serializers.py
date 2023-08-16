from rest_framework import serializers

class SecurityLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class SecurityForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()

class SecurityVerifyOtpForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.IntegerField()

class SecurityNewPasswordSerializer(serializers.Serializer):
    pass

class SecurityResendOtpSerializer(serializers.Serializer):
    pass