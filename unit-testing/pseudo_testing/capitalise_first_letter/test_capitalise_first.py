import capitalise_first_basic as basic
import capitalise_first_indermediate as intermediate

filenames = ['basic', 'intermediate']

def correct_capitalise_first(basic):
  correction_comments = []
  marks = 0

  test_word = "horse"
  output = basic.capitalise_first(test_word)

  # Basic functionality - no data validation
  if output == "Horse":
    marks += 40
    result = f'''Basic functionality Passed:
    Input: {test_word}
    Expected Output: Horse
    Actual Output: {output}
    Marks awarded: 40'''
  else:
    result = f'''Basic Funcionality Failed:
    Input: {test_word}
    Expected Output: Horse
    Actual Output: {output}'''
  
  correction_comments.append(result)

  # Data validation - empty string
  test_word = ""
  try:
    output = basic.capitalise_first(test_word)
  except IndexError:
    result = '''Data Validation (Empty String) Failed:
    Empty string not accounted for. A message should be returned to account for this.'''
  else:
    marks += 20
    result = f'''Data Validation (Empty String) Passed:
    Empty string accounted for
    Input: {test_word}
    Expected Output: Message accounting for empty string
    Actual Output: {output}
    Marks awarded: 20'''

    correction_comments.append(result)
  
  # Data validation - incorrect data type
  test_word = 100
  try:
    output = basic.capitalise_first(test_word)
  except TypeError:
    result = '''Data Validation (Data Type) Failed:
    Non-string data not accounted for.
    You should ensure that only a string variable is entered.'''
  else:
    marks += 20
    result = f'''Data Validation (Data Type) Passed:
    Non-string data accounted for
    Input: {test_word}
    Expected Output: Message accounting for non-string
    Actual Output: {output}
    Marks Awarded: 20'''

  correction_comments.append(result)

  test_word = "1horse"
  output = basic.capitalise_first(test_word)
  if output == test_word:
    result = f'''Data Validation (Non-alphabet 1st character) Failed:
    Non-alphabet first character not accounted for
    Input: {test_word}
    Expected Output: Message accounting for non-alphabet first character
    Actual Output: {output}'''
  
  else:
    marks += 20
    result = f'''Data Validation (Non-alphabet first character) Passed:
    Non-alphabet first character accounted for
    Input: {test_word}
    Expected Output: Message accounting for non-aplpha first character
    Actual Output: {output}
    Marks awarded: 20'''
  
  correction_comments.append(result)

  correction_comments.append(f"Total marks: {marks}")

  return correction_comments

comment_list = correct_capitalise_first(basic)

print(comment_list)

file = open(f"correction_results_basic.txt", "w")

for comment in comment_list:
  file.write(comment + '\n\n')

file.close()