from inspect import getmembers
import inspect
import imp


class MemberManager:

    @classmethod
    def validate_member(cls, member):
        member_class = member[1]

        if not inspect.isclass(member_class):
            return False
        
        from .elements import Element
        if not issubclass(member_class, Element):
            return None

        return True

    @classmethod
    def get_member(cls, obj, name: str):
        obj_path = inspect.getfile(obj.__class__)
        module = imp.load_source("__inspected__", obj_path)
        members = [member for member in getmembers(module) if cls.validate_member(member)]

        for member in members:
            if member[0] == name:
                return member[1]
