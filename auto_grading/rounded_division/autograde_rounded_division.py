import rounded_division_basic as basic
import rounded_division_intermediate as intermediate
import rounded_division_advanced as advanced
import rounded_division_complete as complete

def autograde_rounded_division(basic):
  correction_comments = []
  marks = 0

  a = "20"
  b = "3"
  output = basic.rounded_division(a,b)

  # Basic functionality - no data validation
  if output == 2.00:
    marks += 40
    result = f'''Basic functionality Passed:
    Inputs: {a}, {b}
    Expected Output: 6.67
    Actual Output: {output}
    Marks awarded: 40'''
  else:
    result = f'''Basic Funcionality Failed:
    Inputs: {a}, {b}
    Expected Output: 6.67
    Actual Output: {output}
    Please ensure that you are dividing {a}/{b}, not {b}/{a} in your function
    Use round(float(a)/float(b), 2) to get the answer to 2 decimal places'''
  
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

file = open(f"grading_results_basic.txt", "w")

for comment in comment_list:
  file.write(comment + '\n\n')

file.close()