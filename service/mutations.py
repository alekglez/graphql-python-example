# -*- coding: utf-8 -*-

from datetime import datetime, timedelta
from graphene import Mutation, String, Int, Field
from service.models import Person

from .controllers import controller


class CreateTicket(Mutation):
    class Input:
        name = String()
        description = String()
        story_points = Int()

    expected_dateline = String()

    @staticmethod
    def mutate(root, info, name, description, story_points):
        expected_dateline = datetime.utcnow() + timedelta(days=story_points)
        return CreateTicket(expected_dateline.strftime("%Y-%m-%d %H:%M:%S"))


class AddPerson(Mutation):
    class Input:
        full_name = String()
        age = Int()

    person = Field(lambda: Person)

    @staticmethod
    def mutate(root, info, full_name, age):
        return AddPerson(controller.add_person(full_name=full_name, age=age))


class RemovePerson(Mutation):
    class Input:
        uid = String()

    person = Field(lambda: Person)

    @staticmethod
    def mutate(root, info, uid):
        return RemovePerson(controller.remove_person(uid))
