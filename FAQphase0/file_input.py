#i deepak chander sharma, 000890413 certify that this is my own work and i havent allowed anybody to cpy my content
"""
first i will run this  this input file from where faqbot would be able to read the data from the text files

by clicking run and then click on run  this run this script.

Deepak chander sharma , 000890413
"""
def file_input(filename):
    """Loads each line of the file into a list and returns it."""
    lines = []
    with open(filename) as file: # opens the file and assigns it to a variable
        for line in file:
            lines.append(line) # the strip method removes extra whitespace
    return lines

print(file_input("questions.txt"))