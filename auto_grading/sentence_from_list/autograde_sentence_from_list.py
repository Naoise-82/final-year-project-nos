from pandas import *
import os
import pathlib
from tkinter import Tk, filedialog

root = Tk() # pointing root to Tk() to use it as Tk() in program.
root.withdraw() # Hides small tkinter window.

root.attributes('-topmost', True) # Opened windows will be active. above all windows despite of selection.

folder_path = filedialog.askdirectory() # Returns opened path as str
print(folder_path) 

#change the current working directory to the current path
# current_path = pathlib.Path(__file__).parent
# print(current_path)
os.chdir(folder_path)

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

# function for running the autograding
def run_autograde(input_file):
  correction_comments = []
  marks = 0

  # Basic functionality - no data validation
  word_list = ['i', 'like', 'green', 'eggs', 'and', 'ham']
  
  output = input_file.sentence_from_list(word_list)

  if output == "i like green eggs and ham ":
    marks += 40
    result = f'''Basic functionality Passed:
    Input: {word_list}
    Expected Output: i like green eggs and ham 
    Actual Output: {output}
    Marks awarded: 40'''
  else:
    result = f'''Basic Funcionality Failed:
    Input: {word_list}
    Expected Output: i like green eggs and ham 
    Actual Output: {output}
    Use a for loop to add each item in the list to a new string:
    sentence = ""
    for word in word_list:
      sentence += word + " "
    '''
  
  correction_comments.append(result)

  # Intermediate - Empty List validation
  word_list = []
  try:
    output = input_file.sentence_from_list(word_list)
  except TypeError as e:
    result = '''Data Validation (Empty List) Failed:
    Empty list not accounted for
    Inputs: []
    Use an if statement to check for an empty list, for example:

    if len(word_list) == 0:
      sentence = "Empty list entered, cannot create sentence
    
    Error Outputted: {e}'''
  else:
    marks += 20
    result = f'''Data Validation (Data Type) Passed:
    Empty list accounted for
    Input: []
    Expected Output: print() statement accounting for empty list
    Actual Output: {output}
    Marks Awarded: 20'''

  correction_comments.append(result)

  # Advanced Output - Last space removed and full-stop added
  word_list = ['i', 'like', 'green', 'eggs', 'and', 'ham']

  if output == "i like green eggs and ham.":
    result = '''Advanced Output (Remove last space and add full-stop) Failed:
    Input: {word_list}
    Expected Output: i like green eggs and ham.
    Modify the end of the string after concatenating the list together, for example:
    sentence = sentence[:-1] + "."
    '''
  else:
    marks += 20
    result = f'''Advanced Output (Remove last space and add full-stop) Passed:
    Input: {word_list}
    Expected Output: i like green eggs and ham
    Actual Output: {output}
    Marks awarded: 20'''

  correction_comments.append(result)

  # Complete Output - First letter of first word capitalised
  word_list = ['i', 'like', 'green', 'eggs', 'and', 'ham']
  
  if output == "I like green eggs and ham.":
    result = f'''Complete Output (First letter of first word capitalised) Failed:
    Divide by 0 not accounted for
    Input: {word_list}
    Expected Output: I like green eggs and ham.
    Actual Output: {output}

    Process the first word in the list before adding the words together to form the sentence, for example:
    first_word = str_word_list[0]
    if len(first_word) >= 1:
      first_letter = first_word[0].upper()
      first_word = first_letter + first_word[1:]

    capitalised_list = [first_word]
    capitalised_list.extend(str_word_list[1:])'''
  
  else:
    marks += 20
    result = f'''Complete Output (First letter of first word capitalised) Passed:
    Input: {word_list}
    Expected Output: I like green eggs and ham.
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

  feedback_file = f"{folder_path}\\{student_files[i]}_feedback.txt"

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
