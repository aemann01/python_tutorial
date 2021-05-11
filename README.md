## Beginner Python Programming for Biology

(Updated 6.4.18)

### What is Python?
Python is a flexible, easy to read programming language often used in the biological sciences. It was developed in the lat 1980s by Guido van Rossum (a.k.a, Python's official Benevolent Dictator for Life) and named after British skit group, Monty Python. Unlike other common programming languages (e.g., Perl), Python relies heavily on whitespace to structure its code. In this tutorial you'll learn the basic syntax of Python as well as how to write simple functions and loops. In addition, we introduce two helpful Python libraries -- pandas and BioPython -- and the interactive IPython environment for data analysis.

### Installing Python
* [Windows instructions](https://www.python.org/downloads/windows)
* If you have Mac OS or Linux, Python should already be installed on your computer. Type the following into the command line to see which version is installed.
```bash
python --version
```
* If you receive an error message or no version name is displayed you may need to install the [latest version of python](https://www.python.org/downloads/mac-osx)

**NOTE** This tutorial is written to run Python version 3 or above. If you have Python 2.7 or lower there will be some syntax errors

### Install the [pandas](https://pandas.pydata.org/) Python library
* On Linux
```bash
sudo apt-get install python-pip && pip install numpy && pip install pandas
```
* [MacOS](https://pandas.pydata.org/pandas-docs/stable/install.html)
* [Windows](https://pandas.pydata.org/pandas-docs/stable/install.html)

### Install BioPython
* [Instructions](http://biopython.org/DIST/docs/install/Installation.html#htoc3)

### Install IPython
* [Instructions](https://ipython.org/install.html)

### More Python resources
* [Learn Python the Hard Way](https://learnpythonthehardway.org/)
* [BioPython Tutorial and Cookbook](http://biopython.org/DIST/docs/tutorial/Tutorial.html)
* [Code Academy](https://www.codecademy.com/learn/learn-python)

### Python Syntax Basics
Python programs are written as text documents that end with the .py extension. Typically, Python scripts begin with ```text #!/usr/bin/python``` (#! is called a shebang), which indicates the location of your python install and makes the script executable (though this isn't strictly necessary). Unlike other programming languages (e.g., Perl or R), blocks of code are not specificed by brackets or bracers. Instead, blocks of code in Python are indicated by indentation and colons. For example:

```python
if (x > y):
  print("x is greater than y")
else:
  print("x is less than or equal to y")
```

In this example script, a print statement is called depending on which criteria is met in the if/else statements. It's good practice to include comments in your code with further information on what a particular block of code or statement is doing (or is intended to do). Comments in Python are indicated by a hash symbol (#). So let's add some comments to our previous script.

```python
if (x > y):
  print("x is greater than y")
else:
  print("x is less than or equal to y") # if x is not greater than y this statement will be run
```

Anything beyond the # symbol on the same line will be ignored by your Python interpretor.

### Data Types in Python
Variables or objects that you define or import into the Python environment have different data types. Data types are not implicitly declared by the user (as is the case with many lower-level languages like C). Instead, they are inferred from the assigned statement. It's important to note that because of this sometimes Python will infer the **WRONG** data type. Be sure to check that your objects are assigned to the proper type to avoid problems down the road.

The most common data types in Python include:
* Boolean --> true or false
* Integer --> any full number (e.g., 5, 10, 10000)
* Float --> a number with a fractional value (e.g., 1.5, 3.0, 5.467)
* String --> any character, sentence, word etc.

### Statements and Expressions
Variables or objects are assigned to some value with the = sign. In this example, I'm assiging the string "Hello World" to an object named myString:

```python
myString = "Hello World"
```

This line of code stores my string in the object but does nothing else with it. If I wanted to then print my string to the screen after its assignemnt I would need to call it with the print statement.

```python
print(myString)
```
### Math and Other Operator Examples
* Addition --> +
* Subtraction --> -
* Multiplication --> *
* Division --> /
* Exponentation --> **
* Modulus --> %
* Equal to --> ==
* Not equal to --> !=
* More or less than --> > <

### Important Python Data Structure Types
* List --> a mutable (i.e., changeable) ordered sequences of objects delineated by square brackets []
* Dictionary --> an object type that consists of unique keys that are associated with values. Think of a word in a dictionary as a key and the words definition as the associated value. Defined by curly brackets {key:value}
* Tuple --> similar to a list but an immutable (i.e., unchangeable) sequence of ojects, delineated by parentheses ()
