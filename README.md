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

### Importing Libraries
Many libraries or functions in Python are not included by default and instead must be loaded into the Python environment by the user. For example, say you would like to use the BioPython library in your script. You can do so by adding the following line to the beginning of your code:

```python
import Bio
```

Where ```python import``` is the library importation command and ```python Bio``` is the name of the BioPython library. NOTE: it is important that your import function calls are at the beginning of your script. More typically, however, you'll want to import specific functions or suites of tools from the larger library instead of importing the full library itself. For example, if I was only interested in BioPython's SeqIO, a function that can be used to import a bunch of different sequence format file types, I could run the following command:

```python
from Bio import SeqIO
```

It's usually a good idea to import specific functions from your library instead of the full library whenever possible to cut down on memory useage. Additionally, you may need to install the library before it is available to use. [Installation instructions for BioPython](http://biopython.org/DIST/docs/install/Installation.html)

### Writing a Function
When the function that you want to run does not already exist, you can write your own! Try setting these up as small modules that you can link together to create larger programs to limit debugging time. The basic structure of a Python function is:

```python
def myFunction(optional input parameters):
  some set of conditions to run
```

After writing your function you need to call it in your script somewhere after it is defined

```python 
myFunction(input)
```

### Example: My First Python Program
Open the file called helloWorld.py for viewing

```python
#!/usr/bin/python3
import sys # import statements
```Useage: python helloWorld.py <your name> # doc string that describes how to use the function
def main():
  if len(sys.argv) >= 2:
    name = sys.argv[1]
  else:
    print("Please enter your name:")
    name = input()
  print("Hello", name)
if __name__ == '__main__': # standard way of calling the main function within a script
  main()
```

### Python Interactive Shell (IPython)
One of the nicest things about Python is its interactive shell environment IPython. You will need to install this separately but it provides an easy way to debug or test out your scripts. It also has the extra benefit of tab completion and you can use most Unix commands within the shell. [Instructions for downloading and installing IPython](http://ipython.org/install.html)

### Example: Parsing a Genbank File in IPython
So let's test this out by writing a short script that converts a genbank formatted file to fasta. First open up a terminal and run IPython:

```bash
ipython
```

First we'll need to import the SeqIO module from BioPython

```python
from Bio import SeqIO
```

Now in a single statement we can read in our genbank file and parse through it line by line to extract information from it in a loop

```python
for seqRecord in SeqIO.parse("my_file.gb", "genbank"):
  print(seqRecord)
```

The results of this command shows you all of the information in your genbank file for each sequence record object. Note -- you can call this variable (seqRecord) anything you want -- think of the for statement as saying **for each element in my file: do this**. There are a total of six individual genbank records in this file, each of them have different features and annotations associated with them. Let's look at some of the most common features that you'll find in this file type: the sequence **ID** (a.k.a. the NCBI accession and version number), the sequence **Name** (NCBI accession), the **Sequence** itself, and the sequence **Description** (usually the organism, locus, and other important information about the sequence). 

Try rerunning the above command but instead of seqRecord in the print statment, change the command to one of the features below

```python
seqRecord.id
seqRecord.name
seqRecord.description
seqRecord.seq
```

The above features are required fields for genbank files but often there is other information that we can pull that might be interesting. For example, what if we wanted to only list the organism from which each of our genbank records is derived from? This information is a subset of the annotations field in genbank files -- you can see this when you run:

```python
for seqRecord in SeqIO.parse("my_file.gb", "genbank"):
  print(seqRecord)
  
# E.g., this is part of the output of the above command
/organism=Brassica napus
/taxonomy=['Eukaryota', 'Viridiplantae', 'Embryophyta', 'Tracheophyta', 'Spermatophyta', 'Magnoliphyta', 'eudicotyledons', 'core eudicots', 'Rosidae', 'eurosids II', Brassicales', 'Brassicaceae', 'Brassica']
```

These are annotations within the sequence record, to pull these we need to indicate that the annotation is an aspect of our sequence record with the . operator as well as select those annotations named "organism" within square brackets.

```python
for seqRecord in SeqIO.parse("my_file.gb", "genbank"):
  print(seqRecord.annotations["organism"])
```

Now that we've taken a look at our genbank file, let's convert the sequence data in this file to a workable fasta file format. We can also do this with BioPython!

First you need to define an output handle (think of this as a temporary place holder for your eventual output file)

```python
output_handle = open("my_file.fa", "w")
```

Now we can loop through each record in our genbank file and write the sequence feature of each in fasta format 

```python
for seqRecord in SeqIO.parse("my_file.gb", "genbank"):
  output_handle.write(">%s %s\n%s\n" % (seqRecord.id, seqRecord.description, seqRecord.seq))
```

### Example: Calculating the Percent Identity of Two Fasta Sequences
Open the file percent_identity.py for viewing

```python
import sys # library that allows you to communicate via command linefrom Bio import AlignIO #load AlignIO (input/output) class from BioPython library
"""Problem: You have an alignment file of two 16S rRNA genes (fasta format) and want to calculate the percent identity between them"""
# add fancy colors to the output of your screen (in this case green when the script is complete)
class colors:
  COMPLETE = '\033[92m'
# initialize our data/variables
align = AlignIO.read(sys.argv[1], "fasta")
first_seq = list(align[0])
next_seq = list(align[1])
def pid():
  matches = 0 #initialize values for loop 
  for nucleotide in range(0, len(first_seq)):
    if first_seq[nucleotide] == next_seq[nucleotide]:
      matches += 1
    perc_id = (matches*100)/float((len(first_seq)))
    print(colors.COMPLETE + ("Percent identity: %.2f" % perc_id))
pid()
```

### Example: Data Munging
Open the file otu_table_fix.py for viewing

```python
import sys # library that allows you to communicate via command line
import pandas as pd # load and set up alias for pandas library
"""PROBLEM: you have a tab delimited OTU table called filtered_otu_table_L6.txt with redundanttaxa strings that need to be collapsed"""
data = pd.read_csv(sys.argv[1], sep="\t", skiprows=1)
def fixOTU():
  fixed_data = data.groupby("#OTU ID").sum() 
  # how many duplicate records were in the file?
  duplicates = data.shape[0] ­ fixed_data.shape[0]print("Number of duplicate rows to be collapsed: %i" %duplicates)
  # now write your fixed OTU table to file
  with open("collapsed_otu_table.txt", "w") as outfile:
    fixed_data.to_csv(outfile, sep="\t")
  outfile.close() # you're done writing to file, close it (not necessary but good practice)
  print("Complete, collapsed OTU table written to: collapsed_otu_table.txt") # tell the userthat it's done!
fixOTU()
