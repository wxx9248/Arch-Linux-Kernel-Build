# -*- coding: utf-8 -*-
import typing

# Distro(platform_specific, version)
DistroType: typing.TypeAlias = typing.Tuple[str, str]
# Arch(arch, variant)
ArchType: typing.TypeAlias = typing.Tuple[str, str]

distro_dict: typing.Dict[str, DistroType] = {
    "archlinux": ("archlinux", ""),
}

arch_dict: typing.Dict[str, ArchType] = {
    "amd64": ("amd64", "")
}


def get_distro_from_string(distro_string: str) -> DistroType:
    if distro_string not in distro_dict:
        raise NotImplementedError(f"Unsupported distro: {distro_string}")

    return distro_dict[distro_string]


def get_arch_from_string(arch_string: str) -> ArchType:
    if arch_string not in arch_dict:
        raise NotImplementedError(f"Unsupported arch: {arch_string}")

    return arch_dict[arch_string]
