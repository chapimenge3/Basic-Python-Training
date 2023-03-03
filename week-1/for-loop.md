## For loop in Python

Since now we have learned about Variables, Data type and if condition so let's use them in a program.

Let's say we want to print the numbers from 1 to 10. We can do it like this:

```python
print(1)
print(2)
print(3)
# ...
print(10)
```

This will definitely work correctly right ? Now let's say we want to print the numbers from 1 to 100. We can do it like this:

```python
print(1)
print(2)
print(3)
# ...
print(100)
```

Does this look good to you? I don't think so. It is not a good practice to write the same code over and over again. So what can we do? 

What if i am to tell you that we can do it in a better way? Let's see how.

```python
for i in range(1, 11):
    print(i)
```

Amazing right? What just happened? Let's break it down.

In the above code we used a concept called `Loop`. Loop is a programming concept which allows us to execute a block of code multiple times. 

So what is a block of code? A block of code is a piece of code which is surrounded by curly brackets `{}` in other programming language. In Python, we use indentation to define a block of code. So in the above code, the block of code is the `print(i)` statement.

So For loop is a loop which will execute a block of code multiple times. In the above code, we are executing the `print(i)` statement 10 times. where `i` is a variable which will take the value from 1 to 10.

In this way we can execute a block of code multiple times. 

So let's brake down the above code.

```python
for i in range(1, 11):
    print(i)
```

- `for` is a keyword which tells the python interpreter that we are using a for loop.
- `i` is a variable which will take the value from 1 to 10 at the time of execution.
- `in` is a keyword which tells the python interpreter that we are using some kind of list or bounded range.
- `range(1, 11)` is a function which will return a list of numbers from 1 to 10.
    - `range(1, 11)` will return `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`
    - So range can be used in 3 ways:
        - range(i) - will return a list of numbers from 0 to i-1.
            - `range(10)` will return `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]`
        - `range(i, j)` - will return a list of numbers from i to j-1.
            - `range(1, 11)` will return `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`
        - range(i, j, k) - will return a list of numbers from i to j-1 with a step of k.
            `range(1, 11, 2)` will return `[1, 3, 5, 7, 9]`
- `:` is a keyword which tells the python interpreter that we are going to define a block of code.

Amazing magic right? Now let's try to print the numbers from 1 to 100.

```python
for i in range(1, 101):
    print(i)
```

Now we let's use the range function in a different way.

print the numbers from 1 to 10 with a step of 2.

```python
for i in range(1, 11, 2):
    print(i)
```

print the numbers from 10 to 1 with a step of -1.

```python
for i in range(10, 0, -1):
    print(i)
```

Okay that is so crazy. Now we will use for loop, if condition and variables together.

The problem we are going to solve is:

Print the numbers from 1 to 100. But if the number is divisible by 3 then print `Fizz` instead of the number and if the number is divisible by 5 then print `Buzz` instead of the number and if the number is divisible by both 3 and 5 then print `FizzBuzz` instead of the number.

Is that hard ? hmm we have already solved a problem like that but let's break it down.

question asked 
    - looping from 1 to 100
        - if the number is divisible by 3 then print `Fizz` instead of the number
        - if the number is divisible by 5 then print `Buzz` instead of the number
        - if the number is divisible by both 3 and 5 then print `FizzBuzz` instead of the number.
        - else print the number

How about now ? Is it hard ? Let's solve it.

```python
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
```

Wow that was so easy really the key is to break the problem down into smaller problems and solve them one by one.

Let's try to solve another problem.

Print the sum of all even numbers from 1 to 100.

So as usual we will break the problem down into smaller problems.

- looping from 1 to 100
    - if the number is even then add it to the sum
    - else do nothing

We are going to use Variables and For loop in this problem.(indirectly also data type)

```python
total_sum = 0 # we are initializing the sum variable with 0 so that we can add the numbers to it.

for i in range(1, 101): # looping from 1 to 100
    if i % 2 == 0: # checking if the number is even a
        total_sum = total_sum + i # adding the number to the sum

print(total_sum) # printing the sum
```

What we just did is simply looping from 1 to 100 and adding the even numbers to the sum. 

So that was fun right? 

To save you from the boredom of writing the same code over and over again. Gonna give you a challenge.

Exercise 1:

Print the sum of all odd numbers from 1 to 100.

Exercise 2:

Print the sum of all numbers from 1 to 100 which are divisible by 3 or 5.

Exercise 3:

Have one variable called `number` and print if the number is prime or not.

Exercise 4:

Tell me what do you think will happen if we use `range(1, 0)` in a for loop.

That's it.