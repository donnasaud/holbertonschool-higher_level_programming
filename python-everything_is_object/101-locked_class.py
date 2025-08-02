"""Defines a class LockedClass that only allows 'first_name' attribute."""
#!/usr/bin/python3
class LockedClass:
    __slots__ = ['first_name']

