from rest_example.applications.models import Application
from factory import DjangoModelFactory, Sequence


class ApplicationFactory(DjangoModelFactory):

    title = Sequence(lambda n: 'application-%s' % n)

    class Meta:
        model = Application
        django_get_or_create = ["title"]
