from rest_framework import serializers
from django.contrib.auth.models import User
from User.models import user


class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "is_superuser", "username", "first_name",
                  "last_name", "email", "is_staff", "is_active", "date_joined", "last_login"]


class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    user = serializers.StringRelatedField(
        read_only=True,
    )

    class Meta:
        model = user
        fields = ["id", "user", "avatar"]