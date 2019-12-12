import uuid

from django.db.models import Model, CharField


class Application(Model):

    title = CharField(max_length=128)
    api_key = CharField(unique=True, max_length=36)

    def generate_new_api_key(self):
        api_key = str(uuid.uuid4())
        return api_key.replace("-", "")
