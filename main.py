import InquirerPy
from InquirerPy import prompt
import os
from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator


questions = [
    {"type": "input", "name": "title", "message": "Project Title:"},
    {"type": "input", "name": "description", "message": "Project Description:"},
    {"type": "input", "name": "instructions", "message": "Installation Instructions:"},
    {"type": "input", "name": "usage", "message": "Usage Information:"},
    {"type": "list", "name": "license", "message": "Select a License:",  "choices": ["Apache License 2,0", "MIT License", "GNU GPL v3", "GNU LGPL v3", "Mozilla Public License 2.0", "Creative Commons" , "Unlicense",], "default": None,},
    {"type": "input", "name": "author", "message": "Author:"},
    {"type": "input", "name": "contact", "message": "Contact Info:"},
]
answers = prompt(questions)

def main():
    answers = inquirer.prompt(questions)
    print(answers)
    
if __name__ == "__main__":
    main()

data = answers
def generate_readme(questions, answers):
    
    return f """
# Project Title: {data["title"]}

## Description
{data["description"]}
"""

report = generate_readme("Title", "description")
print(report)

# documents_path = os.path.expanduser("./Documents")

# for filename in os.listdir(documents_path):
#     if os.path.isfile(os.path.join(documents_path, filename)):
#         with open(os.path.join(documents_path, "readme.md"), "a") as file:
#             file.write(f"{filename}\n")

#         print(filename)
        