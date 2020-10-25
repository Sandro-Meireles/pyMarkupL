class EmptyCode(Exception):
    """No code was passed to the element"""
    pass


class InconsistentElement(Exception):
    """Element passed as an attribute cannot be recognized"""
    pass


class ProjectInitError(Exception):
    """error during project init"""
    pass

