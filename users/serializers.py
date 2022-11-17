from rest_framework import serializers
from .models import UserProfile, Users
from phone_field import PhoneField


class UsersProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


class UserRegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField()

    class Meta:
        model = Users
        fields = ['email', 'username', 'password', 'password2', 'phone']

    def save(self, *args, **kwargs):
        # Создаём объект класса User
        user = Users(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
            phone=self.validated_data['phone'],

        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({password: "Пароль не совпадает"})
        user.set_password(password)
        user.save()
        return user
