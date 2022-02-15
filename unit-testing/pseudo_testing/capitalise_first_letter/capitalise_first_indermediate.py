# A function for capitalising the first letter of a string
# Intermediate version - Empty String Validation 

def capitalise_first(input_string):
  #answer = ""
  if input_string == "":
    answer = "Empty string entered"
  else:
    first_character = input_string[0].upper()
    answer = first_character + input_string[1:]
  
  return answer