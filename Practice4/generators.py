#iterator
class Counter:
    def __init__(self, max_value):
        self.max = max_value
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.max:
            self.current += 1
            return self.current
        else:
            raise StopIteration
for num in Counter (3):
    print(num)

#generator
def my_generator():
    yield 1
    yield 2
    yield 3
for num2 in my_generator:
    print(num2)