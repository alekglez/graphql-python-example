# -*- coding: utf-8 -*-

from graphene import Field, ObjectType, Schema, String, List, Int

from service.controllers import controller
from service.models import Ticket, Person
from service.mutations import CreateTicket, AddPerson, RemovePerson


class Query(ObjectType):
    health = String()

    @staticmethod
    def resolve_health(root, info):
        return f"OK"

    ticket = Field(Ticket, name=String())

    @staticmethod
    def resolve_ticket(root, info, name):
        return Ticket(
            name="SomeName",
            description="...",
            story_points=3
        )

    person = Field(Person, uid=String())

    @staticmethod
    def resolve_person(root, info, uid):
        return controller.get_by_id(uid)

    people = List(Person, limit=Int(), offset=Int())

    @staticmethod
    def resolve_people(root, info, limit: int = 10, offset: int = 0):
        return controller.get_all(limit, offset)


class Mutations(ObjectType):
    create_ticket = CreateTicket.Field(
        name="create_ticket",
        description="It creates a new Ticket...")

    add_person = AddPerson.Field(
        name="add_person",
        description="It adds a person to the system...")

    remove_person = RemovePerson.Field(
        name="remove_person",
        description="It remove the person from the database...")


schema = Schema(query=Query, mutation=Mutations)
