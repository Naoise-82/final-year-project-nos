# A function for joining the items in a list together to make a sentence

# Student Name:

sample_list = ['i', 'like', 'green', 'eggs', 'and', 'ham']

def sentence_from_list(word_list):
  sentence = ""

  if len(word_list) == 0:
    sentence = "List is empty."

  for word in word_list:
    sentence += word + " "
  
  sentence = sentence[:-1] + "."

  return sentence

#print(sentence_from_list(sample_list))