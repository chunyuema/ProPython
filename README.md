# ProPython

## What is the Python Interpreter

- Processor gets instruction (machine code) from memory and then exectute them
- Other languages go through: souce code - compiler -> machine code (C/C++/GO) -> executed by the processor
- Python goes through: source code - compiler part of the interpreter -> byte code -> executed by the PVM part of the interpreter

## Key Features of Python:

- interpreted language: no complilation before running
- strongly and dynamically typed:
- object oriented: function is the first-class objects
- quick writting but slower execution
- used a scripting / general purpose language

## Is Python a compiled language?

- source code is compiled into byte code
- byte code is then interpreted by the PVM to give the machine language
- generally considered as a interpreted language

## Interpreted Language:

- executed line by line, other languages such as JS, R, PHP, Ruby are the same

## Memory in Python:

- handled by python memory manager
- memory allocated by manager in form of a private heap space
- all objects are store on the heap and not accessible to the programmer

## **pycache**:

- compiled code is stored in this folder with .pyc

## CPython:

- CPython is the implementation of Python concept in C language
- Other implementations include PyPy, JPython

## namespace:

- namespace ensures object names are unique w/o conflicts
- namespaces are implemented as dictionaries
- local -> global -> built-in

## What are Python packages? Libraries?

- packages are namespaces containing multiple modules
- libraries are collection of Python packages (NumPy, Pandasm Matplotlib)

## Built-in types of Python:

- integer, floats, complex numbers, strings, booleans, built-in functions

## Efficiency of NumPy:

- better support vectorized operations
- more convienent as it comes with pre-defined operations

## Explain multithreading in Python:

- Python has a construct called the Global Interpreter Lock (GIL). The GIL makes sure that only one of your ‘threads’ can execute at any one time. A thread acquires the GIL, does a little work, then passes the GIL onto the next thread. This happens very quickly so to the human eye it may seem like your threads are executing in parallel, but they are really just taking turns using the same CPU core.
