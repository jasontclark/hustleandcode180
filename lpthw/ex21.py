def add(a, b):
    print "ADDING %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "Multiplying %d * %d" % (a, b)
    return a * b

def divide(a,b):
    print "Dividing %d / %d" % (a, b)
    return a / b

print "Let's do some math with just functions!"

age    = add(30,5)
height = subtract(78,4)
weight = multiply(90,2)
iq     = divide(100,2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# A puzzle for extra credit, type it anyway.
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "This becomes: ", what, "Can you do it by hand?"

# The formula for 24 + 34 / 100
answer = subtract(divide(add(24,34), 100), 23)

print "The answer to the next one is ", answer,"."
