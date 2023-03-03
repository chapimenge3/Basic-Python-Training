## Functions in Python

We have talked about a block of code when we are talking about `while`, `if` and `for` loops. So what will happen if we have the same block codes in different places?

We will have to copy and paste the same code in different places. That is not a good practice.

So what we can do is we can create a function and call that function in different places.

What is Functions ?

Functions are a block of code which can be executed multiple times. They can be used to perform a specific task.

Function will take some argument that you can use in your block of code and can be changed dynamically.

functions cal also return a value. This means that you can use the value returned by the function in your code.

Let's see how we can create a function.

```python
def function_name(argument1, argument2):
    # block of code
    return value
```

In the above syntax, we have defined a function named `function_name`, which can be used later to call the function.

The function will take two arguments `argument1` and `argument2`. You can use these arguments in your block of code.

The function will return a value which can be used in your code.

Let's see how we can use this function.

```python
def add(a, b):
    return a + b

sum = add(1, 2)
print(sum)
```

In this example

    - we have created a function named `add` which will take two arguments `a` and `b`.
    - The function will return the sum of `a` and `b`.
    - We have called the function `add` with the arguments `1` and `2`.
    - The function will return the value `3`.
    - We have stored the value returned by the function in a variable named `sum`.
    - We have printed the value of `sum`.

So in this way we can create a function and use it in our code.

Let's see another example.

```python
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

print(is_even(2))
print(is_even(3))
print(is_even(4))
```

In this example

    - we have created a function named `is_even` which will take one argument `number`.
    - The function will check if the number is even or not.
    - If the number is even, the function will return `True`.
    - If the number is odd, the function will return `False`.
    - We have called the function `is_even` with the arguments `2`, `3`, and `4`.
    - The function will return the value `True`, `False`, and `True`.
    - We have printed the value returned by the function.

But can we use this function in a loop?

Yes, we can use this function in a loop.

```python
for i in range(1, 10):
    if is_even(i):
        print(i)
```

You see the function returns a boolean value. So we can use it in a loop to check if the number is even or not.

### Default Arguments

We can also use default arguments in our function. This means that if we don't pass any argument to the function, it will use the default value.


```python
def add(a, b=2):
    return a + b

print(add(1))
print(add(1, 3))
```

See in the above example, we have created a function named `add` which will take two arguments `a` and `b`.

We have set the default value of `b` to `2`. So if we don't pass any value to `b`, it will use the default value.

One thing to note about default arguments is that the default arguments should be at the end of the arguments.

```python
def add(a=2, b):
    return a + b
```

This will give an error because the default argument `a` is not at the end.

### Keyword Arguments

We can also use keyword arguments in our function. This means that we can pass the arguments in any order.

This means if we are passing values to out function we can use the name in the argument to pass the value.

```python
def add(a, b):
    return a + b

print(add(a=1, b=2))
print(add(b=2, a=1))
```

In the above example we have created a function named `add` which will take two arguments `a` and `b`.

We have called the function with the keyword arguments `a` and `b`.

But as you can see we have passed the values in different order. But the function will still work.

### ADVANCED TOPIC

The rest is not required for the course but if you want to learn more about functions you can read the following.

### Variable Length Arguments

We can also use variable length arguments in our function. This means that we can pass any number of arguments to the function.

```python
def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(add(1, 2, 3, 4, 5))
print(add(1, 2, 3))
```

In the above example we have created a function named `add` which will take any number of arguments.

We have used a for loop to iterate over the arguments and add them.

We have called the function with two different arguments.

### Variable Length Keyword Arguments

We can also use variable length keyword arguments in our function. This means that we can pass any number of keyword arguments to the function.

```python
def add(**kwargs):
    sum = 0
    for i in kwargs:
        sum += kwargs[i]
    return sum

print(add(a=1, b=2, c=3, d=4, e=5))
print(add(a=1, b=2, c=3))
```

This way the variable we passed in our function will be a dictionary. So we can access the values using the keys like we did in the previous example.

That's all for this week. In the next week we will learn about `Classes` in Python.

Exercise

1. Create a function named `is_prime` which will take one argument `number`. The function will check if the number is prime or not. If the number is prime, the function will return `True`. If the number is not prime, the function will return `False`.

2. Create a function named `multiply` which will take two arguments `a` and `b`. The function will return the product of `a` and `b`.

3. Create a function named `multiply_all` which will take any number of arguments. The function will return the product of all the arguments.

4. Create a function named `add` which will take any number of keyword arguments. The function will return the sum of all the arguments.

Let me know if you have any questions or suggestions.