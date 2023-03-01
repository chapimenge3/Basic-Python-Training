## If Else condition in Python

What is an if condition?

An if statement is used to check if a condition is true or false. If the condition is true, the code inside the if statement will be executed. If the condition is false, the code inside the if statement will be skipped.

```python
if 5 > 2:
    print("Five is greater than two!")
```

You see in the above code, we are checking if 5 is greater than 2. If the condition is true, we print a message. Now what do you think will happen to the above code. Will it print the message or not? Let's run the code and see what happens.

The next thing we need to learn is the else statement. The else statement is used to execute a block of code when the condition is false.

```python
if 5 < 2:
    print("Five is greater than two!")
else:
    print("Five is not greater than two!")
```

Now we have an if statement and an else statement. The if statement will check if 5 is greater than 2. If the condition is true, it will print "Five is greater than two!". If the condition is false, it will skip the if statement and execute the code inside the else statement.

That is easy right? But let's ask ourselves a question. What if we want to check for more than two conditions? For example, we want to check if a number is greater than 5, less than 5, or equal to 5. How can we do that?

Shall we do first if else condition?

```python
x = 5
if x >= 5:
    if x == 5:
        print("x is equal to 5")
    else:
        print("x is greater than 5")
else:
    print("x is less than 5")
```

That is correct right? YES it will work but there is more to it. We can do the above code in a better way. Let's see how.

```python
x = 5
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")
```

Now there is a new keyword right? which is elif. The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition".

So in the above code, we are checking if x is greater than 5. If it is, we print "x is greater than 5". If it is not, we check if x is equal to 5. If it is, we print "x is equal to 5". If it is not, we print "x is less than 5".

We can have as many elif statements as we want. But we can have only one else statement. The else statement is used to catch anything which isn't caught by the preceding conditions.

But the else statement must be at the end. If you put the else statement before the elif statements, you will get an error.

Now let's see more example.


1. Check if a number is positive or negative

```python
x = -5
if x > 0:
    print("x is positive")
else:
    print("x is negative")
```

2. Check if a number is odd or even?

To solve this problem, we can use the modulo operator. The modulo operator returns the division remainder. The syntax is:

```python
number % 2
```
In more practical terms, let's see the below example.

what is 5 divide by 2 ?

Answer: 2.5 right but we are not interested in the decimal part. We are interested in the remainder. So the remainder is 1. 

Another answer will be 5 divide by 2 is 2 with remainder 1.

Now in python we can use the modulo operator to get the remainder. Let's see how.

```python
x = 5
y = x % 2
print(y) # output will be 1
```

Just remember not to use the modulo operator zero. It will give you an error.

Back to the problem. We can use the modulo operator to check if a number is odd or even. Let's see how.

If Even number is divided by 2, the remainder will be 0. If Odd number is divided by 2, the remainder will be 1.

```python
x = 5
if x % 2 == 0:
    print("x is even")
else:
    print("x is odd")
```

3. Check if the person is eligible to vote or not? Eligibility criteria is 18 years old.

```python
person = {
    'name': 'John',
    'age': 18,
    'country': 'Ethiopia'
}

if person['age'] >= 18:
    print(person['name'] + " is eligible to vote")
else:
    print(person['name'] + " is not eligible to vote")
```

did you see we used `+` operator to concatenate the string and the variable. Let's see how it works.

In Python if we want to join two strings we can use the `+` operator. Let's see how it works.

```python
x = "Hello"
y = "World"
z = x + y
print(z) # output will be HelloWorld
```

So basically we will learn more concepts in this kind of ways. So it is important to understand the basics.

Conclusion on if else condition

- If statement is used to check if a condition is true or false. If the condition is true, the code inside the if statement will be executed. If the condition is false, the code inside the if statement will be skipped.
- The else statement is used to execute a block of code when the condition is false.
- The elif keyword is pythons way of saying "if the previous conditions were not true, then try this condition".
- We can have as many elif statements as we want. But we can have only one else statement. The else statement is used to catch anything which isn't caught by the preceding conditions.
- The else statement must be at the end. If you put the else statement before the elif statements, you will get an error.

## Exercise

1. Write a program to check if a list is empty or not.
2. Write a program to check if the list element number is odd or even.

Hint:
- use `len(list)` to get the length of the list

```python
x = [1, 2, 3, 4, 5]
print(len(x)) # output will be 5 number of elements in the list
```

Enjoy coding and have fun.