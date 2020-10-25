import functools

class ManageRequire:
    def __init__(self, function):
        self.function = function

    def __call__(self, command):
        if not command.is_manage_command():
            command.help_()
            return

        self.function(command)

    def __get__(self, instance, instancetype):
        return functools.partial(self.__call__, instance)