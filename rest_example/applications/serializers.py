from rest_framework.serializers import ModelSerializer

from rest_example.applications.models import Application


class ApplicationSerializer(ModelSerializer):
    class Meta:
        model = Application
        fields = "__all__"
