## Break, Continue, Pass in Python

In previous lessons, we have leaned about if statements, for loops, and while loops. In this lesson, we will learn about the break, continue, and pass statements.

### Break Statement

The break statement is used to exit a loop. For example, if we have a while loop that runs forever, we can use the break statement to exit the loop when some condition is met.

```python
i = 1
while True:
    print(i)
    i += 1
    if i == 5:
        break
```

What the above code will do is 

    - assign 1 to i
    - print i which is 1
    - increment i by 1
    - check if i is equal to 5
        - if it is, break the loop

So in this case the loop continues until i is equal to 5. Then the loop will break. 

Pretty simple right? Let's see another example.

```python
for i in range(1, 10):
    if i == 5:
        break
    print(i)
```

In this case, the loop will break when i is equal to 5. So the loop will print 1, 2, 3, and 4. Then it will break.

### Continue Statement

The continue statement is used to skip the current iteration of a loop. For example, if we have a for loop that iterates over a list of numbers, we can use the continue statement to skip the current iteration if the number is even.

```python
for i in range(1, 10):
    if i % 2 == 0:
        continue
    print(i)
```

In the above code if the number is even, the loop will skip the current iteration and continue with the next iteration. So the loop will print 1, 3, 5, 7, and 9. and it will never print 2, 4, 6, 8.

That is all it does. Let's see another example.

```python
i = 1
while True:
    if i % 2 == 0:
        continue

    if i == 10:
        break
    
    print(i)
    i += 1
    
```

In the above code, the loop will continue until i is equal to 10. If i is even, the loop will skip the current iteration and continue with the next iteration. So the loop will print 1, 3, 5, 7, and 9. and it will never print 2, 4, 6, 8.

### Pass Statement

The pass statement is a null statement. The difference between a comment and a pass statement in Python is that while the interpreter ignores a comment entirely, pass is not ignored.

However, nothing happens when the pass is executed. It results in no operation (NOP).

```python
while True:
    pass
```

The above programs is valid and it will run forever. But it does nothing. It is just a null statement.

Pass is mostly used as a placeholder for future code. For example, if we have a function that is not implemented yet, we can use the pass statement to implement it in the future.

```python
def function(args):
    pass
```

Don't worry if you don't understand what the above code does. We will learn about functions in the next lesson.

### Summary

- The break statement is used to exit a loop.
- The continue statement is used to skip the current iteration of a loop.
- The pass statement is a null statement.

That's it