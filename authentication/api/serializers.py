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
    email = serializers.EmailField()
    new_password = serializers.CharField(style={'input_type': 'password'}, trim_whitespace=False)
    confirm_new_password = serializers.CharField(style={'input_type': 'password'}, trim_whitespace=False)

class SecurityResendOtpSerializer(serializers.Serializer):
   email = serializers.EmailField()