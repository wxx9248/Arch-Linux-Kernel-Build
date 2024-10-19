# -*- coding: utf-8 -*-
import typing

from .common import DistroType, ArchType

OVERRIDE_DICT: typing.Dict[typing.Tuple[DistroType, ArchType], str] = {}


def get_docker_image_tag(distro: DistroType, arch: ArchType) -> str:
    if (distro, arch) in OVERRIDE_DICT:
        return OVERRIDE_DICT[(distro, arch)]

    tag_builder = []

    if arch[0] != "":
        tag_builder.append(arch[0])

    if arch[1] != "":
        tag_builder.append(arch[1])

    if len(tag_builder) != 0:
        tag_builder.append("/")

    tag_builder.append(distro[0])

    if distro[1] != "":
        tag_builder.append(":")
        tag_builder.append(distro[1])

    return "".join(tag_builder)
