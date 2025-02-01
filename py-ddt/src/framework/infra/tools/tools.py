import string


class Tools:
    """
    Tools is an entity that...
    TODO: documentation for Tools.py
    """
    def __init__(self):
        print(r'Tools.py')

    def filter(self, data: string):
        if data is None:
            raise ValueError("data can not be None")
        return f"Tools.py, filter(${data})"
