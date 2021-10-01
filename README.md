# Dynamo Charlotte

Copyright (C) 2020-2021
Sonata Infinity Technologies.
Author: Juan Carlos Juárez.
Licensed under MPL 2.0.
All rights reserved.

Dynamo Charlotte is a Python-based Interpreter that runs on Python Lex-Yacc Parser. It is a beginner friendly language with a syntax similar to Visual Basic and Python, allowing to create anything from numbers to multi-dimensional arrays. The goal of Dynamo Charlotte is to keep a simple coding syntax while still referring to fundamental aspects of programming such as Non-Dynammic Memory, Explicit Data Types and much more. An ideal First-Time Language for teaching kids and programming beginners who are interested in coding, allowing them to learn and dive into the amazing world of Software Engineering. 👩‍💻👨‍💻 

How to Use Dynamo Charlotte
==========

*Requirements: Python 3.6+ installed.

Download the 'dynamocharlotte' folder and add it inside the directory where you will be working on. Now create a Python File and import Dynamo Charlotte as follows:

```python
import dynamocharlotte as dc
```

Now call the 'run' function on 'dc' in order to execute Dynamo Charlotte. To do this simply pass the code as a parameter using Python Multi-line String Triple Quotes. All Dynamo Charlotte Programs include a 'main' and 'end' keyword, where 'main' defines the start of the Main program and 'end' the end of the Program. The base template looks as follows:

```python
dc.run('''

main

end

''')
```

Now you are ready to go. Here's a 'Hello World!' Program Example. Just run it in your favorite IDE:

```python
import dynamocharlotte as dc

dc.run('''

main

print("Hello World!")

end

''')
```

For more Example Programs please check https://github.com/JC-Juarez/dynamocharlotte/tree/main/Code%20Examples

Dynamo Charlotte Documentation - Syntax, Grammar and Considerations
==========

Things to consider:

* While no Indentation is required for Dynamo Charlotte, it is strongly recommended for a better visualization.
* Operators priority is the same as in most Traditional Programming Languages (Visual Basic, C++, Python, Java, etc.)
* There are two types of Variables: Traditional (Number and String) and Object (Vector, Matrix and Cube).
* Object Variables are heterogeneous.
* Variables cannot start with numbers and cannot be the same as reserved tokens.
* The 'camelCase' variable declaration model is the official model for Dynamo Charlotte.

## Main Section

The Main section of the code starts with the word **'main'** and ends with the word **'end'**:

```python
import dynamocharlotte as dc

dc.run('''

main

...

end

''')
```

## Comments

Comments can be added by writing **//** followed the comment content. The can be placed at any part of the program:

```python
import dynamocharlotte as dc

dc.run('''

// This is a comment

main

// Another comment

...

// One more comment

end

// The last comment

''')
```

## Traditional Variables Declaration

There are two types of Traditional Variables: **'number'** and **'string'**. The type **'number'** can only hold numerical values such as:

```
3
3.2
0.15
99
```

The type **'string'** holds text values, cannot operate with arithmetical operators, and is declared and expressed by using double quotes in order to tell it apart from the type **'number'**:

```
"Hello World!"
"Red Car"
"3"
"The square root of 8 is 2.82..."
```

It is important to know that all variables must be declared at the top beginning of the program, before anything else (excluding comments, which can be at any part of the code). They are declared by using the word **'var'** followed by the name we want the variable to have, and then we use the word **'as'** followed by the Variable type, which can be either a **'number'** or **'string'**:

```python
import dynamocharlotte as dc

dc.run('''

var myNumber as number

var myString as string

main

...

end

''')
```








