# A function for dividing any 2 numbers and returning the result to 2 decimal places

def rounded_division(a,b):

  if (type(a) != float or int or str) or (type(b) != float or int or str):
    result = "Incorrect data type Entered. Please use str, int or float"

  elif a == "" or b == "":
    result = "Empty value(s) entered, cannot divide"
    
  elif (type(a) == str and a.isalpha()) or (type(b) == str and b.isalpha()):
    result = "Non numeric value entered, cannot divide."
  
  else:
    result = round(float(a)/float(b), 2)

  return result

print(rounded_division([4],5))
