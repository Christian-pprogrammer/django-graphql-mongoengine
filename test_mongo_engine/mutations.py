from enum import Enum

import graphene
from cards.models import Todo
from .types import TodoType

class TaskInput(graphene.InputObjectType):
    name = graphene.String()
    text = graphene.String()
    task_strs = graphene.List(graphene.String)

class CreateTodoMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        tasks = graphene.List(TaskInput)

    todo = graphene.Field(TodoType)

    def mutate(self, info, name, tasks):

        my_todo = Todo(name=name, tasks=tasks)
        my_todo.save()
        return CreateTodoMutation(todo=my_todo)