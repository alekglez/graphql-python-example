# -*- coding: utf-8 -*-

from random import randint
from typing import Dict
from uuid import uuid4

from service.models import Person


class DataController:
    people: Dict[str, Person] = {}

    def __init__(self):
        for x in range(10):
            uuid_ = str(uuid4())
            self.people[uuid_] = Person(
                uuid=uuid_,
                full_name=f"some_name_{x}",
                age=randint(25, 50)
            )

    def add_person(self, full_name: str, age: int):
        uuid_ = str(uuid4())

        record = Person(
            uuid=uuid_,
            full_name=full_name,
            age=age
        )

        self.people[uuid_] = record
        return record

    def get_by_id(self, uuid_: str):
        return self.people.get(uuid_, None)

    def get_all(self, limit: int = 10, offset: int = 0):
        data = list(self.people.values())
        end, size = limit + offset, len(data)
        return data[offset:end if end < size else size]

    def remove_person(self, uuid_: str):
        return self.people.pop(uuid_, None)


controller = DataController()
