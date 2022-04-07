# A function for joining the items in a list together to make a sentence

# Student Name:

sample_list = ['i', 'like', 'green', 'eggs', 'and', 'ham']
sample_list_02 = ['we', 'like', 'green', 'eggs', 2]

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
  
  # add each word in the list to the string with a space
  for word in str_word_list:
    sentence += word + " "
  
  # remove the last space and add a full stop
  sentence = sentence[:-1] + "."

  return sentence

print(sentence_from_list(sample_list))
print(sentence_from_list(sample_list_02))