from enum import Enum

from mongoengine import Document
from mongoengine import EmbeddedDocumentField
from mongoengine.fields import (
    FloatField,
    StringField,
    ListField,
    URLField,
    ObjectIdField,
    ReferenceField,
    EmbeddedDocument,
    EnumField

)


# class Task(EmbeddedDocument):
#     name = StringField()



class Shop(Document):
    meta = {"collection": "shop"}
    ID = ObjectIdField()
    name = StringField()
    address = StringField()

class Status(Enum):
    ACTIVE = 'ACTIVE'
    DEACTIVATED = 'DEACTIVATED'

class Task(EmbeddedDocument):
    name = StringField()
    text = StringField()
    task_strs = ListField(StringField())
    status = EnumField(Status, default=Status.ACTIVE)


class Todo(Document):
    meta = {"collection": "todo"}
    ID = ObjectIdField()
    name = StringField()
    tasks = ListField(EmbeddedDocumentField(Task))


class Bike(Document):
    meta = {"collection": "bike"}
    ID = ObjectIdField()
    name = StringField()
    brand = StringField()
    year = StringField()
    size = ListField(StringField())
    wheel_size = FloatField()
    type = StringField()
