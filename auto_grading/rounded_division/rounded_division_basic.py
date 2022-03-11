# A function for dividing any 2 numbers and returning the result to 2 decimal places

def rounded_division(a,b):
  result = round(float(a)/float(b), 2)

  return result

print(rounded_division("20","3"))