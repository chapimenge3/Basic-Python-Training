## Python Variables

What is a variable?

A variable is a container for a value, which can be of various types. In Python, variables are created when you assign a value to it:

```python
x = 5
y = "Hello, World!"
```

So variable is responsible for storing data that we can use later in our program.

```python
x = 5
y = 10
z = x + y # here we used variable x and y to store data and then we used them to perform addition operation
print(z) # output will be 15
```

## Variable Names

There are rules and conventions for naming variables in Python. Below are the rules:

1. Variable names cannot start with a number.
2. Variable names cannot contain spaces.
3. Variable names cannot contain special characters like !, @, #, $, %, etc. except for the underscore character (_).
4. Variable names are case-sensitive (name, Name and NAME are three different variables).

Some important conventions for naming variables in Python are:

1. Variable names should be short and descriptive.
2. Variable names should be in lowercase unless we are using constants.
3. Avoid using ambiguous names like `l` (lowercase letter el), `O` (uppercase letter oh), and `I` (uppercase letter eye) as variable names.

## Assign Value to Multiple Variables

In python we can assign a single value to multiple variables in one line.

```python
x = y = z = "Orange"
```

We can also assign multiple values to multiple variables in one line.

```python
x, y, z = "Orange", "Banana", "Cherry"
```

But when assigning multiple values to multiple variables, the number of variables must match the number of values, otherwise you will get an error.

```python
x, y, z = "Orange", "Banana" # this will raise an error because left side has 3 variables and right side has 2 values
```

When we assign to multiple variables, the value is assign to each variable from left to right.
