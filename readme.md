# Manatee Python
## A Leaving Cert Computer Science Python Script Autograding Workflow

### Overview
The goal of this project is to design a workflow that automatically collects, organises, grades and sends feedback on Python programming assignments as part of the Leaving Certificate Computer Science coursework. It is achieved through the use of *Teams, OneDrive, Power Automate (Cloud Version), Power Automate for Desktop* and *Outlook* from the *Microsoft 365 Suite*, coupled with the Python scripts included in this repository, which are modelled on Unit testing concepts.

The conetnts of this repository are only part of the entire worklow, the *Teams* and *Power Automate* elements functions within their enviroments online and on the desktop, but their underlying code and JSON data, as well as flowcharts of their function are included here for archiving purposes.

### Repository Contents
- **auto_grading**
  - **assignments**: These are the sample answers and the autograding scripts based on the asignments in the Final Report
  - **auto_import_trial:** This folder wa used to test an improved algorithm for importing mulitple files into a running script, later incorporated into the autograding scripts them selves.
  - **example_feedback_outputs:** These are early output text files from autograding, aminly used as a trial for folder redirection and assessing the visual format of the output
- **power_automate_cloud:** This folder contains flowchart images and JSON exports from the 3 version of the file collection flows created throughout the course of the project.
- **power_automate_desktop:** This folder contains the code for the desktop flow that sends the feedback to students, exported directly from the app itself into a text file. It is a proprietry language unique to the app; this text can be copied and pasted into *Power Automate for Desktop* to be used by anyone else.
- **power_automate_feedback_testing:** This folder was the first trial of *Power Automate for Desktop* to see if the contects of a text file and a CSV could be used to send an email of feedback to a student.
- **unit_test_trial:** This folder conatins the early experimenting I did with Unit Tests and exprting their results. I abandoned this method early on in the prject. This si kept as a record.
