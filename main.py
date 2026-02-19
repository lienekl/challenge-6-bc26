import InquirerPy
from InquirerPy import prompt
import os
from InquirerPy.base.control import Choice
from InquirerPy.separator import Separator
from questions import questions


answers = prompt(questions)

    
def generate_readme(answers):
    
    return f"""
# {answers["title"]}

## Description

{answers["description"]}

## Installation Instructions

{answers["instructions"]}

## Usage Information

{answers["usage"]}

## License

Please select an appropriate license for your project:

{answers["license"]}

## Author

{answers["author"]}

## Contact Information

For questions or feedback, please contact:

*{answers["contact"]}*

"""

content = generate_readme(answers)


with open("readme.md", "w") as file:
    file.write(content)