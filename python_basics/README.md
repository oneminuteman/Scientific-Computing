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

