import rounded_division_basic as basic
import rounded_division_intermediate as intermediate
import rounded_division_advanced as advanced
import rounded_division_complete as complete
import os

input_files = [basic, intermediate, advanced, complete]
input_filenames = [file.name for file in input_files]
print(input_filenames)

def autograde_rounded_division(input_file):
  correction_comments = []
  marks = 0

  # Basic functionality - no data validation
  a = 20
  b = 3
  output = input_file.rounded_division(a,b)

  if output == 6.67:
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

   # Data validation - incorrect data type
  a = "20"
  b = "3"
  try:
    output = input_file.rounded_division(a,b)
  except TypeError as e:
    result = '''Data Validation (Data Type) Failed:
    String data not accounted for
    Inputs: "20", "3"
    You should ensure that only int or float data is used in the calculation
    Use float(a) and float(b) to convert the values to floats
    Error Outputted: {e}'''
  else:
    marks += 20
    result = f'''Data Validation (Data Type) Passed:
    String data accounted for
    Inputs: {a}, {b}
    Expected Output: 6.67
    Actual Output: {output}
    Marks Awarded: 20'''

  correction_comments.append(result)

  # Data validation - empty values
  a = ""
  b = ""
  try:
    output = input_file.rounded_division(a,b)
  except TypeError as e:
    result = '''Data Validation (Empty Values) Failed:
    Empty values not accounted for
    Inputs: Empty values for both a and b
    Expected Output: Message accounting for empty values
    Error Outputted: {e}
    Use
      if a == "" or b == "":
    to test for empty values, and print a message if either is true'''
  else:
    marks += 20
    result = f'''Data Validation (Empty Values) Passed:
    Empty values(s) accounted for
    Inputs: {a}, {b}
    Expected Output: Message accounting for empty values
    Actual Output: {output}
    Marks awarded: 20'''

  correction_comments.append(result)

  # Data Validation - Divide by 0
  a = 20
  b = 0
  try:
    output = input_file.rounded_division(a,b)
  except ZeroDivisionError as e:
    result = f'''Data Validation (Divide by 0) Failed:
    Divide by 0 not accounted for
    Inputs: {a}, {b}
    Expected Output: Message accounting for 0 entered for variable b
    Actual Output: {e}
    Use if float(b) == 0.00 to test'''
  
  else:
    marks += 20
    result = f'''Data Validation (Divide by 0) Passed:
    Variable b entered as 0 accounted for
    Inputs: {a}, {b}
    Expected Output: Message accounting for 0 entered as variable b
    Actual Output: {output}
    Marks awarded: 20'''
  
  correction_comments.append(result)

  correction_comments.append(f"Total marks: {marks}")

  return correction_comments

count = 1

for i in range(len(input_files)):
  
  comment_list = autograde_rounded_division(input_files[i])

  print(comment_list)

  file = open(f"auto_grading/feedback_outputs/grading_results_{input_filenames[i]}.txt", "w")

  for comment in comment_list:
    file.write(comment + '\n\n')

  file.close()
  count += 1

