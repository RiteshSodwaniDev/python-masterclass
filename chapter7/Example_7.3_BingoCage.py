import random

class BingoCage:

    def __init__(self,items=None):
        self._items=list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('Pick from empty Bingcage')
    def __call__(self):
        return self.pick()



bingo=BingoCage(range(3))
print(bingo.pick())

print(bingo())


print(callable(bingo))
