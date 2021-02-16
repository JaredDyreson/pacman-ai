class UniqueList():
    def __init__(self, container=[]):
        self.container = container

    def union(self, other: list):
        if(not isinstance(other, list)):
            raise ValueError
        return [x for x in self.container if x not in other]
    def __add__(self, other):
        self.container.extend(self.union(other))
        return self.container

a = UniqueList([1, 2, 3])
b, c = [], []
e = a + b
print(e)
