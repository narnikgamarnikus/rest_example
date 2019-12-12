import uuid

from django.db.models import (
	Model,
    CharField,
    TextField,
    PositiveSmallIntegerField,
    ForeignKey,
    CASCADE,
)


class Application(Model):

	title = CharField(max_length=128)
	api_key = CharField(unique=True, max_length=36)

