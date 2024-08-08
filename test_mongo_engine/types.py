from graphene import relay
from graphene_mongo import MongoengineObjectType
from cards.models import Bike, Shop, Todo
from cards.models import Task


class BikeType(MongoengineObjectType):
    class Meta:
        model = Bike
        interfaces = (relay.Node,)


class ShopType(MongoengineObjectType):
    class Meta:
        model = Shop

class TaskType(MongoengineObjectType):
    class Meta:
        model = Task
class TodoType(MongoengineObjectType):
    class Meta:
        model = Todo
