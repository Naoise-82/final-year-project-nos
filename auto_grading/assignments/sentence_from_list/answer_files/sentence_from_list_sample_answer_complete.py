# A function for joining the items in a list together to make a sentence

# Student Name:

sample_list = ['i', 'like', 'green', 'eggs', 'and', 'ham']
sample_list_02 = ['we', 'like', 'green', 'eggs', 'and', 'ham', 2]

def capitalise_first(input_string):
  
  # check for empty string
  if input_string == "":
    answer = "No word entered"

  # ensure the input is a string
  elif type(input_string) != str:
    answer = "Input variable is not a string"
  
  # if all validation passes, capitalise the first letter
  else:
    first_character = input_string[0].upper()
    answer = first_character + input_string[1:]
  
  return answer

def sentence_from_list(word_list):
  sentence = ""

  # check for empty list
  if len(word_list) == 0:
    sentence = "List is empty."
  
  # ensure that each item in the list is a string variable
  str_word_list = []
  for word in word_list:
    word = str(word)
    str_word_list.append(word)
  
  # add each word in the list to the sentence string with a space
  for word in str_word_list:
    sentence += word + " "
  
  capitalised_sentence = capitalise_first(sentence)
  
  # remove the last space and add a full stop
  final_sentence = capitalised_sentence[:-1] + "."

  return final_sentence

#print(sentence_from_list(sample_list))
#print(sentence_from_list(sample_list_02))