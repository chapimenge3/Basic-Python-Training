## While Loop in Python

In the previous lesson, we learned about the `for loop`. In this lesson, we will learn about the `while loop`.

So let's say there is a problem that says 

> until the user enters a number greater than 100, keep asking the user to enter a number.

So, how are we going to solve this problem with a for loop?

It is kind of not the for loop's job to do this. Because for loop is used to iterate over a finite list of items. So we can't use a for loop to solve this problem.

To solve this problem, we will use a while loop.

While loop is a loop which execute a block of code until a condition is met.

So in this case we have a condition that says `until the user enters a number greater than 100`. So we will use a while loop to execute a block of code until the user enters a number greater than 100.

First let's see the syntax of a while loop.

```python
while condition:
    # block of code
```

- `while` is a keyword which tells the python interpreter that we are using a while loop.   
- `condition` is a condition which will be evaluated at the time of execution. If the condition is `True`, the block of code will be executed. If the condition is `False`, the block of code will not be executed.
- `:` is a keyword which tells the python interpreter that we are going to define a block of code.

With that in mind, let's solve the problem.

```python
number = int(input("Enter a number: "))
while number <= 100:
    number = int(input("Enter a number: "))
```

Let's break down a little bit what all is happening in the above code.

- input() function will ask the user to enter a number.
    - we can print something before asking the user to enter a number like `input("Enter a number: ")`
    - this function will return a string data type.

- int() function will convert the input string to an integer.
    - as the `input` function returns a string, we need to convert it to an integer to compare it with the number 100.

- `number = int(input("Enter a number: "))` will assign the value of the input to the variable `number`.

- `while number <= 100:` will check if the number is less than or equal to 100. If the number is less than or equal to 100, the block of code will be executed. If the number is greater than 100, the block of code will not be executed.
- `number = int(input("Enter a number: "))` will ask the user to enter a number again.

Now this might seems a little bit confusing, but honestly, it is not. Just follow the code and you will understand it.

Don't worry if you don't know the functions like `input` and `int` yet. We will learn about them in later lessons.

So now let's get back to out lesson while loop.

Keep in mind that while loop will execute a block of code until a condition is met. So if the condition is never met, the while loop will never end.

for example:

```python
while False:
    print("Hello World")
```

In the above code, the condition is `False`. So the block of code will never be executed.

Another example would be 

```python
while 1 < 0:
    print("Hello World")
```

In the above code, the condition is `1 < 0`. So the block of code will never be executed.

So, if you are using a while loop, make sure that the condition is met at some point. Otherwise, your program will never end.

Not exiting the program is called an infinite loop. So make sure that you don't create an infinite loop.

Let's see what infinite loop looks like.

```python
while True:
    print("Hello World")
```

If you run this and keep it your computer likely will crash. So don't do that.

That's it for this lesson.