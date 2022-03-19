# A function for dividing any 2 numbers and returning the result to 2 decimal places
name = "complete"
def rounded_division(a,b):
    
  if a == "" or b == "":
    result = "Empty value(s) entered, cannot divide."
    
  elif (type(a) == str and a.isalpha()) or (type(b) == str and b.isalpha()):
    result = "Non numeric value entered, cannot divide."
  
  elif (type(a) == str and a.isalnum() == False) or (type(b) == str and b.isalnum() == False):
    result = "Non numeric value entered, cannot divide."

  elif b == float(b) == 0.00:
    result = "Cannot divide by zero."
  
  else:
    result = round(float(a)/float(b), 2)

  return result

#print(rounded_division("?","7"))
