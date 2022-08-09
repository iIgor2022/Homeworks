nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]


class FlatIterator:
    def __init__(self, it_list):
        self.nested_list = it_list
        self.index = -1
        self.sublist = iter([])

    def __iter__(self):
        return self

    def __next__(self):
        try:
            result = next(self.sublist)
        except StopIteration:
            self.index += 1
            try:
                self.sublist = iter(self.nested_list[self.index])
            except IndexError:
                raise StopIteration
            result = next(self.sublist)
        return result


for item in FlatIterator(nested_list):
    print(item)

flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)



nested_list_gen = [
    ['a', [1, 2, 3], 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None],
]


def flat_generator(nested_list):
    index = 0
    while True:
        try:
            result = nested_list[index]
        except IndexError:
            break
        for element in result:
            yield element
        index += 1


for item in flat_generator(nested_list_gen):
    print(item)