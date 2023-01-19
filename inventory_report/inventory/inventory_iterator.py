from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, data):
        self.init = 0
        self.data = data

    def __next__(self):
        product = self.data[self.init]
        if product:
            self.init += 1
        else:
            raise StopIteration()
        return product
