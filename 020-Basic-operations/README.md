---
marp: true
---

# Basic operations

---

## Python as a calculator
For this short section we're going to ignore the work we had done to
Visual Studio Code and instead focus on the Python *interpreter*.

Open a terminal or command prompt and type,
```
python
```

---

## The interpreter
At this point your terminal should have changed a little.
You might be seeing something like this,
```
Python 3.8.1 (default, Jan 22 2020, 06:38:00) 
[GCC 9.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

This is the Python interpreter prompt.
Try typing in some basic maths, `2+2`, `3-5*2` etc.

Each time you do this Python parses the line of input and evaluates it.
This is in stark contrast to other languages which aren't *interpreted* but are
*compiled*.
In compiled languages the whole program and flow must be written out
first before the computer *compiles* it to machine code (very low level stuff)
which becomes a binary or executable file.

---

## A calculator
Let's see if we can do some more stuff, multiplication? Can we use brackets?
How about the something like 5^2?

---

## Highly advanced calculator
Ok let's try some more stuff with our calculator. In mathematics we have the
concept of unknowns like when we're asked to solve for x. Let's try something,
```
x = 2*(5-2)/3
```
When we run this command in our prompt we get... nothing? Well don't worry, in
programming it's common that if there's nothing said then there's nothing wrong!

To get our answer we have to write `x` without an equal sign (more on this later).

Note how I said *without and equal sign*. That means we can also do `x + 4` and
it does exactly what we suspect.

---

# More than a calculator
Now you might be thinking that we've been following the usual mathematic rules
which might make you assume `x = 2.0` and nothing will change it. Just like the
speed of light or the acceleration of gravity right?

Luckily for us programming does not follow that mathematical rule. Try the
following,
```
x = 3.0
x
x = 5.0
x
```

This is the first important distiction. Don't think of `x` as a number or an
unknown number you have to solve. Instead think of it like a box or container.

---

## A container?
Take a look at what we've done with `x` in the past few sides. We first put
`2*(5-2)/3`
