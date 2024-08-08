import graphene
from graphene.relay import Node
from graphene_mongo.fields import MongoengineConnectionField
from cards.models import Shop
from cards.models import Todo
from .mutations import CreateTodoMutation
from .types import BikeType, ShopType
from .types import TaskType
from .types import TodoType


class Mutations(graphene.ObjectType):
    create_todo = CreateTodoMutation.Field()

class Query(graphene.ObjectType):
    node = Node.Field()
    # bikes = MongoengineConnectionField(BikeType)

    todos = graphene.List(TodoType)

    def resolve_todos(self, info):
        return Todo.objects.all()


schema = graphene.Schema(query=Query, mutation=Mutations, types=[TodoType, TaskType])
