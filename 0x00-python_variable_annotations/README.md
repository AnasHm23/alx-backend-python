# 0x00. Python - Variable Annotations

## Learning Objectives

By the end of this project, you will gain knowledge and skills in the following areas:

- Type annotations in Python 3
- How you can use type annotations to specify function signatures and variable types
- Duck typing
- How to validate your code with mypy

## Requirements

### General

- **Editors**: You are allowed to use vi, vim, or emacs for coding.
- **Python Version**: All code will be interpreted/compiled using Python 3 (version 3.7).
- **File Endings**: Ensure that all your files end with a newline character.
- **Shebang Line**: The first line of all your Python files should be exactly `#!/usr/bin/env python3`.
- **README.md**: A mandatory README.md file must be present at the root of your project folder.
- **Code Style**: Your code should adhere to the pycodestyle style (version 2.5).
- **Executable Files**: All your Python files must be executable.
- **File Length**: The length of your files will be tested using `wc`.
- **Documentation**: 
  - All your modules should have documentation. You can check this using `python3 -c 'print(__import__("my_module").__doc__)'`.
  - All your classes should have documentation. You can check this using `python3 -c 'print(__import__("my_module").MyClass.__doc__)'`.
  - All your functions, both inside and outside a class, should have documentation. You can check this using `python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`.

### Collaborators

- ANAS HOUMAID

### Documentation Guidelines

- A documentation is not just a single word; it should be a complete sentence that explains the purpose of the module, class, or method. The length of your documentation will be verified.

## Project Overview

- Variable annotations in Python allow you to provide additional information about the types of variables (including class variables and instance variables). Here’s what you need to know:

### Background:
- Variable annotations were introduced in Python 3.6 as part of PEP 526.
- They build upon the concept of type hints, which were introduced in Python 3.5 (as described in PEP 484).