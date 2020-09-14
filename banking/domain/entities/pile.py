
class Pile:
    """
    Represents a set of clients
    In a LIFO structure
    """
    def __init__(self):
        # Let's use a list to implement a Stack(Pile)
        self.items = []

    # Equivalent of the 'inStack' function
    def __contains__(self, client_name):
        return any([client_name == item.name for item in self.items])

    def is_empty(self):
        return self.items == []

    # Equivalent of the 'displayStack' function
    def __str__(self):
        return '\n'.join([str(item) for item in reversed(self.items)])

    # Equivalent of the 'displayStackItem' function
    def displayItem(self, item):
        if item in self.items:
            print(item)
        else:
            print(f"{item} not in this {self.__class__.__name__}")

    # Equivalent of the 'pushInStack' function
    def push(self, item):
        self.items.append(item)

    # Equivalent of the 'popOutStack' function
    def pop(self):
        if self.items:
            return self.items.pop()
        else:
            raise IndexError(f"{self.__class__.__name__} is empty.")