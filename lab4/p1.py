class Stack(object):
    def __init__(self):
        self.storage = []

    def push (self, newValue):
        self.storage.append( newValue )

    def top(self ):
        return self.storage[len(self.storage) - 1]

    def pop(self ):
        result = self.top()
        self.storage.pop()
        return result

    def isEmpty(self ):
        return len(self.storage) == 0

class CalculatorEngine(object):
    def __init__(self ):
        self.dataStack = Stack ()

    def pushOperand(self , value ):
        self.dataStack.push(value)

    def currentOperand(self ):
        return self.dataStack.top()

    def performBinary(self , fun):
        right = self.dataStack.pop()
        left = self.dataStack.top()
        self.dataStack.push( fun(left , right ))

    def doAddition(self ):
        self.performBinary (lambda x, y: x + y)

    def doSubtraction(self ):
        self.performBinary (lambda x, y: x - y)

    def doMultiplication(self ):
        self.performBinary (lambda x, y: x * y)

    def doDivision(self ):
        try:
            self.performBinary (lambda x, y: x / y)
        except ZeroDivisionError :
            print("divide by 0!" )
            exit (1)

    def doTextOp(self , op):
        if (op == '+'): self.doAddition ()
        elif (op == '-'): self.doSubtraction ()
        elif (op == '*'): self.doMultiplication ()
        elif (op == '/'): self.doDivision ()


class RPNCalculator(CalculatorEngine):
    def __init__(self):
        # your code here
        super().__init__()

    def doModulo(self):
        try:
            self.performBinary(lambda x, y: x % y)
        except ZeroDivisionError:
            print("divide by 0!")
            exit(1)
    
    def doTextOp(self, op):
        if (op == '%'): self.doModulo()
        return super().doTextOp(op)

    def eval(self, line):
        # your code here
        line = line.split(' ')
        for word in line:
            if word != '+' and word != '-' and word != '*' and word != '/' and word != '%':
                self.pushOperand(int(word))
            else:
                self.doTextOp(word)
        return self.currentOperand()
                