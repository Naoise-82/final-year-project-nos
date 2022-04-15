from pandas import *
import os
from tkinter import Tk, filedialog
from importlib.machinery import SourceFileLoader

root = Tk()
root.withdraw()

root.attributes('-topmost', True)

# open the path to the assignment folder and assign to a string
assignment_folder_path = ''
initial_directory = "C:\\Users\\Naoise\\OneDrive - Cork Education and Training Board\\02 - Subjects\\Computer Science\\CS_Test_Autograding"

while assignment_folder_path == '':
  assignment_folder_path = filedialog.askdirectory(title="Select The Assignment Folder", initialdir=initial_directory) +"/"

print(assignment_folder_path)

# access the feedback_data CSV file and add the filenames ot a list
feedback_data = read_csv(assignment_folder_path + "feedback_data.csv")
student_files = feedback_data['filename'].tolist()

# import all of the students' files as modules
modules = []

for file in student_files:
  try:
    file = SourceFileLoader(file, assignment_folder_path + file + ".py").load_module()
    modules.append(file)
    print("Successfully imported", file)
  except ImportError as e:
    print("Error importing", file)
    print(e)

# function for running the autograding
def run_autograde(input_file):
  correction_comments = []
  marks = 0

  # Basic functionality - no data validation
  word_list = ['i', 'like', 'green', 'eggs', 'and', 'ham']
  
  output = input_file.sentence_from_list(word_list)

  if output == "i like green eggs and ham " or "i like green eggs and ham" or "i like green eggs and ham." "I like green eggs and ham" or "I like green eggs and ham.":
    marks += 40
    result = f'''<pre><b>Basic functionality Passed:</b>
    <b>Input:</b> {word_list}
    <b>Expected Output:</b> "i like green eggs and ham " or more complete answer.
    <b>Actual Output:</b> "{output}"
    <b>Marks awarded:</b> 40
    '''
  else:
    result = f'''<pre><b>Basic Functionality Failed:</b>
    <b>Input:</b> {word_list}
    <b>Expected Output:</b> i like green eggs and ham 
    <b>Actual Output:</b> "{output}"
    
    Use a for loop to add each item in the list to a new string:
    sentence = ""
    for word in word_list:
      sentence += word + " "
      '''
  
  correction_comments.append(result)

  # Intermediate - Empty List validation
  word_list = []

  output = input_file.sentence_from_list(word_list)
  if len(output) == 0:
    result = '''<b>Data Validation (Empty List) Failed:<br>
    Empty list not accounted for
    <b>Input:</b> []
    <b>Expected Output:</b> Message accounting for empty list
    <b>Actual Output:</b> {output}
    
    Use an if statement to check for an empty list, for example:
    if len(word_list) == 0:
      sentence = "Empty list entered, cannot create sentence"
      '''
  
  else:
    if len(output) > 0:
      marks += 20
      result = f'''<b>Data Validation (Empty List) Passed:</b>
      Empty list accounted for
      <b>Input:</b> []
      <b>Expected Output:</b> print() statement accounting for empty list
      <b>Actual Output:</b> {output}
      <b>Marks Awarded:</b> 20
      '''

  correction_comments.append(result)

  # Advanced Output - Last space removed and full-stop added
  word_list = ['i', 'like', 'green', 'eggs', 'and', 'ham']

  output = input_file.sentence_from_list(word_list)

  if output[-2:] != "m.":
    result = f'''<b>Advanced Output (Remove last space and add full-stop) Failed:</b>
    <b>Input:</b> {word_list}
    <b>Expected Output:</b> Last 2 characters of output to be "m."
    <b>Actual Output:</b> {output[-2:]}
    
    Modify the end of the string after concatenating the list together, for example:
    sentence = sentence[:-1] + "."
    '''
  
  else:
    marks += 20
    result = f'''<b>Advanced Output (Remove last space and add full-stop) Passed:</b>
    <b>Input:</b> {word_list}
    <b>Expected Output:</b> Last 2 characters of output to be "m."
    <b>Actual Output:</b> Last 2 characters are "{output[-2:]}"
    <b>Marks awarded:</b> 20
    '''

  correction_comments.append(result)

  # Complete Output - First letter of first word capitalised, non-string data type validation
  word_list = ['We', 'like', 'green', 'eggs', 'and', 'ham', 2]

  try:
    output = input_file.sentence_from_list(word_list)

  except TypeError as e:
    result = f'''<b>Complete Output (First letter capitalised and non-string data validated) Failed:</b>
    Divide by 0 not accounted for
    <b>Input:</b> {word_list}
    <b>Expected Output:</b> We like green eggs and ham 2.
    <b>Actual Output:</b> {e}

    Use the code you wrote in the Capitalise First Letter assignment to modify the
    completed sentence string at the end of your code:
    first_letter = sentence[0].upper()
    finished sentence = first_letter + sentence[1:]

    Check for non-string items in the list and convert them to strings
     str_word_list = []
    for word in word_list:
      word = str(word)
      str_word_list.append(word)
    </pre>'''
  
  else:
    marks += 20
    result = f'''<b>Complete Output (First letter of first word capitalised) Passed:</b>
    <b>Input:</b> {word_list}
    <b>Expected Output:</b> We like green eggs and ham 2.
    <b>Actual Output:</b> {output}
    Marks awarded: 20
    </pre>'''
  
  correction_comments.append(result)

  correction_comments.append(f"<pre><b>Total marks:</b> {marks}</pre>")

  return correction_comments

feedback_files = []

# autograde all scripts, write the results to a text file, append text file path to feeback_data.csv
count = 1
for i in range(len(student_files)):
  
  try:
    comment_list = run_autograde(modules[i])

  except AttributeError or ValueError as e:
    comment_list = ["Your file didn't run correctly, check for syntax errors and try again."]
  
  else:
    feedback_file = f"{assignment_folder_path}\\{student_files[i]}_feedback.txt"

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
feedback_data.to_csv(assignment_folder_path + 'feedback_data.csv', index=False)
