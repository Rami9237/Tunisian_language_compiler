class Number():
    def __init__(self, value):
        self.value = value

    def eval(self):
        return int(self.value)


class BinaryOp():
    def __init__(self, left, right):
        self.left = left
        self.right = right


class Sum(BinaryOp):
    def eval(self):
        return self.left.value + self.right.value


class Sub(BinaryOp):
    def eval(self):
        return int(self.left.value) - int(self.right.value)
    
class Divide(BinaryOp):
    def eval(self):
        return int(self.left.value) / self.right.value

class Print():
    def __init__(self, value):
        self.value = value

    def eval(self):
        print("FDSQDS")
        if (not(hasattr(self.value,'left'))):
            print(self.value[0].value[1:-1])
        else:
            print(self.value.eval())