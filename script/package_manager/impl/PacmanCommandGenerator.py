# -*- coding: utf-8 -*-
from package_manager.model import PackageManagerCommandGenerator, PackageManagerVerb


class PacmanCommandGenerator(PackageManagerCommandGenerator):
    def __init__(self):
        super().__init__("pacman", {
            PackageManagerVerb.UPDATE: "-Sy --noconfirm",
            PackageManagerVerb.UPGRADE: "-Su --noconfirm",
            PackageManagerVerb.INSTALL: "-S --noconfirm",
            PackageManagerVerb.REMOVE: "-R --noconfirm"
        })
