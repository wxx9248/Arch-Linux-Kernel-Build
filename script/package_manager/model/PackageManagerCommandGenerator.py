# -*- coding: utf-8 -*-
import typing
from enum import auto, IntEnum


class PackageManagerVerb(IntEnum):
    UPDATE = auto()
    UPGRADE = auto()
    INSTALL = auto()
    REMOVE = auto()


class PackageManagerCommandGenerator:
    def __init__(self, name: str, verb_dict: typing.Dict[PackageManagerVerb, str]):
        self.__name = name
        self.__verb_dict = verb_dict

    @property
    def name(self):
        return self.__name

    @property
    def verb_dict(self):
        return self.__verb_dict

    def update(self) -> str:
        return " ".join((self.name, self.verb_dict[PackageManagerVerb.UPDATE]))

    def upgrade(self) -> str:
        return " ".join((self.name, self.verb_dict[PackageManagerVerb.UPGRADE]))

    def install(self, *packages: str) -> str:
        return " ".join((self.name, self.verb_dict[PackageManagerVerb.INSTALL], *packages))

    def remove(self, *packages: str) -> str:
        return " ".join((self.name, self.verb_dict[PackageManagerVerb.REMOVE], *packages))
