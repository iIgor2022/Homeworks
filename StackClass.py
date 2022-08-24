class Stack:
    def __init__(self):
        self.stack_list = []

    def isEmpty(self):
        if len(self.stack_list) > 0:
            return False
        else:
            return True

    def push(self, item):
        self.stack_list.append(item)

    def pop(self):
        try:
            result = self.stack_list.pop()
        except IndexError:
            result = None
        return result

    def peek(self):
        try:
            result = self.stack_list[-1]
        except IndexError:
            result = None
        return result

    def size(self):
        return len(self.stack_list)


def is_balanced_string(string):
    stack = Stack()
    for symbol in string:
        if symbol in ['(', '{', '[']:
            stack.push(symbol)
        elif symbol in [')', ']', '}']:
            if stack.isEmpty():
                return "Несбалансированно"
            symbol_from_stack = stack.pop()

            if not ((symbol_from_stack == '(' and symbol == ')')
                or (symbol_from_stack == '[' and symbol == ']')
                or (symbol_from_stack == '{' and symbol == '}')):
                return "Несбалансированно"
    if stack.isEmpty():
        return "Сбалансированно"
    else:
        return "Несбалансированно"