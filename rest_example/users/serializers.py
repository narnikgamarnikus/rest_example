from rc.users.models import User

from rest_framework.serializers import ModelSerializer


class UserSerializer(ModelSerializer):
    """Serialize a `users.User` instance."""

    class Meta:
        model = User
        fields = ("id", "username")
