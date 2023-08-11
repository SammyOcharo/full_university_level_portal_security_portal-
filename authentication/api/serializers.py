from rest_framework import serializers

class SecurityLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

class SecurityForgotPasswordSerializer(serializers.Serializer):
    pass

class SecurityVerifyOtpForgotPasswordSerializer(serializers.Serializer):
    pass

class SecurityNewPasswordSerializer(serializers.Serializer):
    pass

class SecurityResendOtpSerializer(serializers.Serializer):
    pass