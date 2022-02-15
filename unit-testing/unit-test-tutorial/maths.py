# addition
def add(a,b):
  return a - b

# subtraction
def subtract(a,b):
  return a - b

# multiplication
def multiply(a,b):
  return a * b

# division
def divide(a,b):
  if b == 0:
    raise ValueError("Can't divide by 0")
  return a / b