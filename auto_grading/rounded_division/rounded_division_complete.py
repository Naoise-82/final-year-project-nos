# A function for dividing any 2 numbers and returning the result to 2 decimal places

def rounded_division(a,b):
    
  if a == "" or b == "":
    result = "Empty value(s) entered, cannot divide."
    
  elif a.isalpha() or b.isalpha():
    result = "Non numeric value entered, cannot divide."
  
  elif a.isalnum() == False or b.isalnum() == False:
    result = "Non numeric value entered, cannot divide."

  elif b == "0":
    result = "Cannot divide by zero."
  
  else:
    result = round(float(a)/float(b), 2)

  return result

print(rounded_division("?","7"))
