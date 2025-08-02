#!/usr/bin/python3

"""Module that defines LockedClass with restricted attribute creation."""


class LockedClass:
    """Prevents dynamic attributes except 'first_name'."""
    __slots__ = ["first_name"]
