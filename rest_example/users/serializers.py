from rest_example.users.models import User

from rest_framework.serializers import ModelSerializer


class UserSerializer(ModelSerializer):
    """Serialize a `users.User` instance."""

    class Meta:
        model = User
        fields = ("id", "username")


class UserDetailSerializer(ModelSerializer):
    """Serialize a `users.User` instance."""

    class Meta:
        model = User
        fields = ("id", "username", "email", "first_name", "last_name")
