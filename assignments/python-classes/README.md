# 📘 Assignment: Python Classes

**Difficulty:** Beginner  
**Estimated time:** 45–60 minutes

## 🎯 Objective

Learn how to define and use classes in Python to model real-world objects and behaviors. This assignment walks you through creating a simple class, adding attributes and methods, and interacting with class instances.

## 📂 Files
- `starter-code.py` — starter code with a class skeleton and minimal examples
- `solution.py` — (optional) reference implementation

## 🔧 Prerequisites
- Python 3.x
- Basic familiarity with functions and data types in Python

## 📝 Tasks

### 🛠️ Define a Simple Class

#### Description
Create a class named `Car` that represents a car with attributes for make, model, and year. Add a method to display information about the car.

#### Requirements
Completed program should:

- Define a class `Car` with `make`, `model`, and `year` attributes
- Include a method `display_info()` that prints the car's details
- Create an instance of `Car` and call `display_info()`


### 🛠️ Add Methods and Interactions

#### Description
Expand the `Car` class to include a `mileage` attribute, a method to update the mileage, and a method to display the current mileage.

#### Requirements
Completed program should:

- Add a `mileage` attribute to the `Car` class (default 0)
- Add a method `update_mileage(new_mileage)` to update the mileage (should not decrease mileage)
- Add a method `display_mileage()` to print the current mileage
- Demonstrate updating and displaying mileage for a `Car` instance

## 💡 Hints
- Use `self` to access instance attributes inside methods.
- Optionally validate `new_mileage` in `update_mileage()` so it cannot be lower than the current mileage.

## ✅ How to run
From the repository root, run:

```bash
python3 assignments/python-classes/starter-code.py
```

## 📤 Submission
- Save your completed solution as `solution.py` and submit via a pull request or ZIP upload.
