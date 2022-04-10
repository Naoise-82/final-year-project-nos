from pandas import *
import os
import pathlib

#change the current working directory to the current path
current_path = pathlib.Path(__file__).parent
# print(current_path)
os.chdir(current_path)

# access the feedback_data CSV file and add the filenames ot a list
feedback_data = read_csv("feedback_data.csv")
feedback_data.head()
student_files = feedback_data['filename'].tolist()

# import all of the students' files as modules
modules = []

for file in student_files:
  try:
    modules.append(__import__(file))
    print("Successfully imported", file)
  except ImportError:
    print("Error importing", file)

# function for running the actual autograding
def run_autograde(input_file):
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

feedback_files = []

# autograde all scripts, write the results to a text file, append text file path to feeback_data.csv
count = 1
for i in range(len(student_files)):
  
  comment_list = run_autograde(modules[i])

  feedback_file = f"{current_path}\\{student_files[i]}_feedback.txt"

  feedback_files.append(feedback_file)

  file = open(feedback_file, "w")

  for comment in comment_list:
    file.write(comment + '\n\n')

  file.close()
  count += 1

# add the feedback_filepath column to the csv data
feedback_data["feedback_filepath"] = feedback_files
print(feedback_data.head())

# write the data back to the csv file
feedback_data.to_csv('feedback_data.csv', index=False)
