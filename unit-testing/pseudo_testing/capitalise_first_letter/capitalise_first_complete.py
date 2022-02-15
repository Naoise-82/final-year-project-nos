# A function for capitalising the first letter of a string
  
def capitalise_first(input_string):

  # check for empty string
  if input_string == "":
    answer = "No word entered"

  # ensure the input is a string
  elif type(input_string) != str:
    answer = "input variable is not a string"

  # check that the fisrt character is a letter
  elif input_string[0].isalpha() == False:
    answer = "First character is not a letter"
  
  # if all validation passes, capitalise the first letter
  else:
    first_character = input_string[0].upper()
    answer = first_character + input_string[1:]
  
  return answer