from rest_example.applications.models import Application
from factory import DjangoModelFactory, Faker


class ApplicationFactory(DjangoModelFactory):

    title = Faker("title")

    class Meta:
        model = Application
        django_get_or_create = ["title"]
