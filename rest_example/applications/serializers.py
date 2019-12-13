from rest_framework.serializers import ModelSerializer, ReadOnlyField
from rest_example.applications.models import Application


class ApplicationSerializer(ModelSerializer):

    api_key = ReadOnlyField()

    class Meta:
        model = Application
        fields = "__all__"
