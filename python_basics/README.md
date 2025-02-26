# Python Scripts Overview

This repository contains three Python scripts that demonstrate modular functions, data types, and control structures. Below is a detailed explanation of each script and how to run them.

## 1. `modular_functions.py`
This script defines a function to calculate the area of different shapes (circle, rectangle, triangle) and tests the function by printing the calculated areas.

### Key Points:
- **Function: `calculate_area()`**
  - Takes three parameters: 
    - `shape`: The type of shape ("circle", "rectangle", or "triangle").
    - `dimension1`: The first dimension (e.g., radius for circle, length for rectangle/triangle).
    - `dimension2`: The second dimension (optional, e.g., width for rectangle/height for triangle).
  - Calculates the area based on the shape and dimensions provided.
  - If an invalid shape is provided, it returns an "Invalid shape" message.

### Example Output:
```bash
Circle area (radius 5): 78.54
Rectangle area (5x10): Invalid shape  # Typo in the shape name 'rectangle'
Triangle area (base 6, height 8): 24.0

datatypes.py
This script demonstrates how to define and check various Python data types and perform type conversions.

Code Overview
Creates variables of different types:
Integer (int_var)
Float (float_var)
Complex (complex_var)
List (list_var)
Dictionary (dict_var) [Note: Incorrect syntax used for dictionary creation]
Boolean (bool_var)
Uses the type() function to print the type of each variable.
Demonstrates type conversion by converting an integer to a float.
Bug in the code: The dictionary is incorrectly defined as a list.
Example Output
Type of int_var: <class 'int'>
Type of float_var: <class 'float'>
Type of complex_var: <class 'float'>  # Typo in the type check (should be complex)
Type of list_var: <class 'list'>
Type of bool_var: <class 'bool'>

control_structures.py
This script contains control structures such as conditional statements, list comprehensions, and loops.

Code Overview
classify_number(n) Function:
Checks if a number is even or odd using the modulo (%) operator.
List Comprehension:
Generates a list of even numbers between 1 and 50.
While Loop:
Prints numbers counting down from 10 to 1.
Example Output

Enter an integer: 45
The number 45 is odd.
Even numbers from 1 to 50: [2, 4, 6, ..., 50]
Counting down from 10 to 1:
10 9 8 7 6 5 4 3 2 1

