# Exception handling
This document will teach the idea of exception handling as a necessary step
towards I/O (Input/Output).

---

## Case study: A new calculator!
It's been a long day in the office at Calc inc. for everyone. The final commits
have been pushed for the day and everyone is clocking out. You decide to stay
behind to run a few tests on our new product.

---

Here's the code:
```python
import math
while (True):
    operation = input("Please specify the operation\n> ")
    x = float(input("Please specify the first number\n> "))
    y = float(input("Please specify the second number\n> "))
    if "x" in operation or "*" in operation:
        print("Multiplication not completed yet :P")
    elif "+" in operation:
        # Dave: could you double check this code not really sure...
        print(x + y)
    elif "/" in operation:
        print(x / y)
    elif "^" in operation:
        print(math.pow(x,y))
    else:
        # Linda: So... what happens if the user inputs a bad operation?
    None
```

---

As your getting to leave the office you try one last test of the code.
```
Please specify the operation
> /
Please specify the first number
> 1
Please specify the second number
> 0
Traceback (most recent call last):
  File "calc.py", line 10, in <module>
    print(x / y)
ZeroDivisionError: float division by zero
```
Damn! It's far too late to be fixing something like this. You write a quick ticket and then clock out with your colleagues.

---

## How would you fix it?
Given what you've learnt so far how would you handle this? Take your time, try figuring it out yourself.

---

```python
...
elif "/" in operation:
    if y != 0:
        print(x / y)
    else:
        print("Can't perform a division by zero")
...
```

Jobs done! You might think to yourself. But just before you commit this amazing patch another ticket pops up on your desktop.

---

## Another bug
The following input has also been causing issues.
```
Please specify the operation
> ^
Please specify the first number
> -1
Please specify the second number
> 0.5
Traceback (most recent call last):
  File "calc.py", line 14, in <module>
    print(math.pow(x,y))
ValueError: math domain error
```

Well I guess we could add another `if` statement...

---

## What even are these error messages?
Let's take another look at the errors messages we've gotten:
`ValueError: ...` and `ZeroDivisionError: ...`. What do these mean?

These are known as exceptions or errors. These mechanisms allow us to get more *information* and *control* over errors in our program.

Because we aren't **handling** these errors they will default to stopping our program and printing themselves out on the screen.

---

## A better solution
Instead of letting the errors stop our program we could use a try-except block.
```python
try:
    lotsOfCode()
except ValueError:
    print("A value error has occurred")
except ZeroDivisionError as err:
    print(str(err))
```

In other languages it's called a try-catch block with `except` being replaced
with the word `catch`. Think of this as preventing the exception from *leaping* onto the screen and catching it here before it does so.

If we successfully catch an exception we can then move on with our code.

---

## The new fix

```python
import math
while (True):
    operation = input("Please specify the operation\n> ")
    x = float(input("Please specify the first number\n> "))
    y = float(input("Please specify the second number\n> "))
    try:
        if "x" in operation or "*" in operation:
            print("Multiplication not completed yet :P")
        elif "+" in operation:
            # Dave: could you double check this code not really sure...
            print(x + y)
        elif "/" in operation:
            print(x / y)
        elif "^" in operation:
            print(math.pow(x,y))
        else:
            # Linda: So... what happens if the user inputs a bad operation?
        None
    except Exception as e:
        print(str(e))
```

---

## So what is try-except even doing?
You may have noticed that we used `except Exception as e` instead of the errors
we've seen so far, `ZeroDivisionError` and `ValueError`. Why is that and why is
this code even working?

Currently we don't have concepts like inheritance to understand this so instead
consider that the `except` part is looking for an error to match with.

Suppose there was a `dogException` if we have a `except mammalException` then
this block would catch the dog exception. In the previous case `Exception` is
the most general type of... well exception!