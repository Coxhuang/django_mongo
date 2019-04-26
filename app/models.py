from django.db import models
import mongoengine


class Test(mongoengine.Document):

    name = mongoengine.StringField(
        max_length=128,
    )
    age = mongoengine.IntField(
        default=10,
    )