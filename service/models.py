# -*- coding: utf-8 -*-

from graphene import String, Int, ObjectType


class Ticket(ObjectType):
    name = String()
    description = String()
    story_points = Int()


class Person(ObjectType):
    uuid = String()
    full_name = String()
    age = Int()
