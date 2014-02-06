# No setup
import arithmetic

i = 0
while i < 3:
    input = raw_input("Type in your question.")
    token = input.split(" ")
    if token[0] == 'q':
        i = 3
    elif token[0] == "+":
        arithmetic.add(token[1], token[2])
    elif token[0] == "-":
        arithmetic.subtract(token[1], token[2])
    elif token[0] == "*":
        arithmetic.multiply(token[1], token[2])
    elif token[0] == "/":
        arithmetic.divide(token[1], token[2])
    elif token[0] == "square":
        arithmetic.square(token[1])
    elif token[0] == "cube":
        arithmetic.cube(token[1])
    elif token[0] == "pow":
        arithmetic.power(token[1], token[2])
    elif token[0] == "mod":
        arithmetic.mod(token[1], token[2])