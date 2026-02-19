import InquirerPy
from InquirerPy import prompt

questions = [
    {"type": "input", "name": "title", "message": "Project Title:"},
    {"type": "input", "name": "description", "message": "Project Description:"},
    {"type": "input", "name": "instructions", "message": "Installation Instructions:"},
    {"type": "input", "name": "usage", "message": "Usage Information:"},
    {"type": "list", "name": "license", "message": "Please select an appropriate license for your project:",  "choices": ["Apache License 2,0", "MIT License", "GNU GPL v3", "GNU LGPL v3", "Mozilla Public License 2.0", "Creative Commons" , "Unlicense",], "default": None,},
    {"type": "input", "name": "author", "message": "Author:"},
    {"type": "input", "name": "contact", "message": "Contact Info:"},
]