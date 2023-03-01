## Data Type in Python

Python has the following data types built-in by default, in these categories:

1. String - `str`
2. Integer - `int`
3. Float - `float`
4. Boolean - `bool`
5. List - `list`
6. Tuple - `tuple`
7. Dictionary - `dict`
8. Set - `set`

Did you feel overwhelmed by the list above? Don't worry, we will cover each of them in detail in the following sections.

1. String - `str`

A string is a sequence of characters. In Python, strings are surrounded by either single quotation marks, or double quotation marks.

```python
x = "Hello World"
name = 'Chapi Menge'
```

In other programming language you might see character data type, but in Python, a character is simply a string with a length of 1. Square brackets can be used to access elements of the string.

```python
first_vowel = 'a'
second_vowel = 'e'
```

2. Integer - `int`

Integers are whole numbers, positive or negative, without decimals, of unlimited length.

```python
x = 1
y = -2
z = 0
```

As you have seen in the example above, we can assign a value to a variable using the assignment operator `=`.

So bear in mind that `=` is not the same as `==`. `=` is used to assign a value to a variable, while `==` is used to compare two values. More on this later.

3. Float - `float`

Float, or "floating point number" is a number, positive or negative, containing one or more decimals. 

```python
x = 1.10
y = 1.0
z = -35.59
```

Did you notice the `int` and `float` data types are very similar? The only difference is that `int` is a whole number, while `float` is a number with a decimal point. 

We can apply any operation on `int` and `float` data types, and the result will be a `float` data type.

```python
x = 1 + 2.8
print(x) # output will be 3.8
```

What if i want to divide two integers and get an integer as a result? Let's see what happens when we divide 5 by 2.

```python
x = 5 / 2
print(x) # output will be 2.5
```

We got a `float` as a result, but if we wanted an `int`. How can we do that? We can use the `int()` function to convert a `float` to an `int`.

```python
x = 5 / 2
y = int(x)
print(y) # output will be 2
```

But there is a better way to do this. We can use the `//` operator to get the integer part of a division.

```python
x = 5 // 2
print(x) # output will be 2
```

So just remember that `//` is used to get the integer part of a division, while `/` is used to get the float part of a division.

4. Boolean - `bool`

Boolean represents one of two values: `True` or `False`. That's it.

```python
x = True
y = False
```

Boolean might be the most easiest data type to understand. It can only have two values, `True` or `False`. This is useful when we want to check if a condition is `True` or `False`.

There are different operation that results in a boolean value. For example, the `==` operator returns `True` if two values are equal, otherwise it returns `False`.

```python
x = 5 == 5
print(x) # output will be True
```

There is also !=, <, >, <=, >= operators that returns a boolean value.

```python
x = 5 != 5
print(x) # output will be False

y = 5 > 3
print(y) # output will be True

z = 5 < 3
print(z) # output will be False

a = 5 >= 5 # this operator is greater than or equal to
print(a) # output will be True

b = 5 <= 2 # this operator is less than or equal to
print(b) # output will be False
```

5. List - `list`

A list is a collection which is ordered and changeable. You can store multiple data types in a list.

```python
x = ["apple", "banana", "cherry"]
y = [1, 5, 7, 9, 3]
z = [True, False, False]
a = [True, 2, "apple"] # this is a list with multiple data types
```

Lists are created using square brackets. We can access items in a list by referring to the index number.

```python
x = ["apple", "banana", "cherry"]
print(x[1]) # output will be banana
```

We can also change the value of a specific item by referring to the index number.

```python
x = ["apple", "banana", "cherry"]
x[1] = "blackcurrant"
print(x) # output will be ['apple', 'blackcurrant', 'cherry']
```

Did you notice when we change index 1 it changed the value of the second item in the list? That's because Python is a zero-indexed language. This means that the first item has index 0. 

So the index number are as follows:

```python
x = ["apple", "banana", "cherry"]
x[0] # first item
x[1] # second item
x[2] # third item
```

6. Tuple - `tuple`

A tuple is a collection which is ordered and unchangeable. You can store multiple data types in a tuple.

```python
x = ("apple", "banana", "cherry")
y = (1, 5, 7, 9, 3)
z = (True, False, False)
a = (True, 2, "apple") # this is a tuple with multiple data types
```

So what is the difference between a list and a tuple? The main difference is that a tuple is unchangeable, while a list is changeable. We can access items in a tuple by referring to the index number.

```python
x = ("apple", "banana", "cherry")
print(x[1]) # output will be banana
```

But if we try to change the value of a specific item by referring to the index number, we will get an error.

```python
x = ("apple", "banana", "cherry")
x[1] = "blackcurrant" # this will raise an error
```

7. Dictionary - `dict`

A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.

```python
x = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}
```

We can access the items of a dictionary by referring to its key name.

```python
x = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}
print(x["age"]) # output will be 36
```

So what is the difference between a list and a dictionary? The main difference is that a dictionary is unordered, while a list is ordered. We can access items in a dictionary by referring to the key name. so that we can have any key name we want.

You might ask why is this useful? Well, let's say we want to store a person's name, age and country. We can store this in a list like this:

```python
person = ["John", 36, "Norway"]

print(person[0]) # output will be John
print(person[1]) # output will be 36
print(person[2]) # output will be Norway
```

But do you think the above code is easy to understand? What if there is a better way to store this data? We can use a dictionary to store this data like this:

```python
person = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}
print(person["name"]) # output will be John
print(person["age"]) # output will be 36
print(person["country"]) # output will be Norway
```

As you can see, the above code is much easier to understand. We can access the items of a dictionary by referring to its key name. So we can have any key name we want.

8. Set - `set`

A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets. It only contains unique values.

```python
x = {"apple", "banana", "cherry"}
```

Hmmm something seems familiar. We have seen this before. Yes, you are right. This is similar to a dictionary. But the main difference is that a set is unordered and unindexed, while a dictionary is ordered and indexed. We can access items in a set by referring to the index number.

```python
fruits = {"apple", "banana", "cherry"}
person = {
    "name": "John",
    "age": 36,
    "country": "Norway"
}
```

What do you think fruits data type? also person data type? If you say fruits is a set and person is a dictionary, you are right.

Because Dictionary have a key and separated with its value by a colon(':'), while Set have a value and separated with its value by a comma(',').

So it's  enough to know the data types. Now let's move on to the next topic. 

Please read and practice to understand the data types because we are going to use them more in the next topics.