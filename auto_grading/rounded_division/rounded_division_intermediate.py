# A function for dividing any 2 numbers and returning the result to 2 decimal places
import email


name = "joan"
email_address = "joan@email.com"

def rounded_division(a,b):
  
  if a == "" or b == "":
    result = "Empty value(s) entered, cannot divide"
  
  else:
    result = round(float(a)/float(b), 2)

  return result
