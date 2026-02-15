import InquirerPy
from InquirerPy import prompt
import os
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
print(answers)
    
data = questions, answers

def generate_readme(data):
    
    return f"""
# Project Title: {data["title"]}

## Description: {data["description"]}
"""

content = generate_readme
# documents_path = os.path.expanduser("./challenge-6-bc26")

# for filename in os.listdir(documents_path):
#     if os.path.isfile(os.path.join(documents_path, filename)):
#         with open(os.path.join(filename, "readme1.md"), "w") as file:
#             file.write(f"{content}\n")
#             print(filename)



documents_path = os.path.expanduser("./")

for filename in os.listdir(documents_path):
    if os.path.isfile(os.path.join(documents_path, filename)):
        with open(os.path.join(documents_path, "readme.md"), "w") as file:
            file.write(f"{content}\n")

        
        