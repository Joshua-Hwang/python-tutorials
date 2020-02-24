---
marp: true
---

# Basic strings, functions and control flows
This section intends to teach how programming languages handle words and about
control flows.

---

## We have numbers, now what
So we can use numbers great. But afterwards you start wanting something more,
something that can really *speak* to you. Well now we can with **strings**!
```python
abc = "Hello, World!"
abc
```

---

## Strings
Strings (like `"Hello, World!"`) are literals just like the numbers we saw
earlier. Just like the number literals the **string literals** can be assigned
to a variable.

>Strings are called "strings" because they are made up of a sequence,
>or string, of characters.

---

## Functions
So we can now write messages. But they still have those annoying single-quotes
surrounding them. To output or  **print** a message correctly we have to use
a **function**. These are special operations that go beyond the basic
addition and multiplication that we've been using.

In this case we'll be using the `print()` function.
```python
print("Hello")
print(abc)
print(abc, "Goodbye")
```

You will notice when I referred to the function I had `()`. This is because a
function might require additional information. These additional pieces of
information are sometimes called **arguments** or **parameters**.
When you call `print` the program needs to know *what* do you want to print.

---

## Ifs and elses
Now let's say we're working on a project, the boss needs to know if we're going
overbudget this month. The boss doesn't *do* numbers, we'll have to communicate it
in a way that is easy to understand.

We'll write this in VSCode and run our program from there.
```python
# This is a comment. The program ignores this line. It's useful for communication
budget = 100 # this is our monthly budget in $1,000s
costs = 25.1*4 # we have weekly costs of $2,5100
netTotal = budget - costs # this is the net total income
if netTotal > 0:
  print("We're fine")
else:
  print("We're overbudget")
```

---

## Dissecting the if else block
Let's take a look at what we've done. It reads very much like a natural sentence.
>If thing is true do something, else do something else
```python
if thing:
  something()
else:
  somethingElse()
print("If statement done")
```

The `else` block is optional and can be skipped.

---

## Indents
You'll notice there's an indent at `something()` and `somethingElse()`.
Why is this? Consider the following,
```python
if thing:
something()
print("thing is true")
print("If statement done")
```

---

Does it mean?
```python
if thing:
    something()
    print("thing is true")
    print("If statement done")
```

or
```python
if thing:
    something()
    print("thing is true")

print("If statement done")
```

This is why the indents exist.

---

## More control flow
Let's say we want to make another check if we just meet our budget.
We could do the following,
```python
if netTotal > 0:
  print("We're fine")
else:
  if netTotal == 0:
    print("We're just on budget")
  else:
    print("We're overbudget")
```

---

But we can use a much more **elegant** solution.
Edit your previous program with the following.
```python
if netTotal > 0:
  print("We're fine")
elif netTotal == 0:
  print("We're just on budget")
else:
  print("We're overbudget")
```

---

## Deeper dive into functions
You've been exposed to `print()` but as you might've guessed there are more
functions than just that. Here are a few of the most common.
* `len()` measures the length of the parameter
* `int()` convert the parameter to an integer
* `str()` convert the parameter to a string
* `float()` convert the parameter to a float

More can be found at: https://docs.python.org/3/library/functions.html
