# A function for joining the items in a list together to make a sentence

# Student Name:

sample_list = ['i', 'like', 'green', 'eggs', 'and', 'ham']

def sentence_from_list(word_list):
  sentence = ""

  for word in word_list:
    sentence += word + " "

  return sentence

#print(sentence_from_list(sample_list))