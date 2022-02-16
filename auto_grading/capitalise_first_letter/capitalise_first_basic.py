

# A function for capitalising the first letter of a string
def capitalise_first(input_string):
  
  first_character = input_string[0].upper()
  answer = first_character + input_string[1:]
  
  return answer