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
# Title: {data["title"]}

## Description: 

{data["description"]}
"""

content = generate_readme(answers)
print(content)

with open("readme.md", "w") as file:
    file.write(content)