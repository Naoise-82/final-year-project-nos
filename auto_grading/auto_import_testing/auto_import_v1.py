from os import listdir
filenames = [f[:-3] for f in listdir("auto_grading/capitalise_first_letter")]
print(filenames)