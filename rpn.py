#!/usr/bin/env python3

import operator
#import matplotlib
#matplotlib.use('Agg')
#import matplotlib.pyplot as plt

operators = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '^': operator.pow,
}

def calculate(myarg, y):
    stack = list()
    for token in myarg.split():
        try:
            token = int(token)
            stack.append(token)
        except ValueError:
            function = operators[token]
            arg2 = stack.pop()
            arg1 = stack.pop()
            result = function(arg1, arg2)
            stack.append(result)
            y.append(result)
        #print(stack)
    if len(stack) != 1:
        raise TypeError("Too many parameters")
    return stack.pop()

def main():
    y = []

    result = calculate(input("rpn calc> "),y)
    print("Result: ", result)
    print(y)
 #   plt.plot(y)
  #  plt.savefig('graph.png')
if __name__ == '__main__':
    main()
