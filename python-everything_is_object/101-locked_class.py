"""Module that defines LockedClass with restricted attribute creation."""
#!/usr/bin/python3
class LockedClass:
    """Prevents dynamic attributes except 'first_name'."""
    __slots__ = ["first_name"]
