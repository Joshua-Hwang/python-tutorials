---
marp: true
---

# Basic operations
This section intends to teach variables, numbers and assignments.

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
How about the something like 5^3?
```
5^3
6
5^2
7
```
Uhhh... Well that's unexpected. (You don't need to know what any of this means
so don't worry). In many languages including Python the `^`
operator does not raise powers. Instead it takes the XOR function of the bits
that make up the number.
```
5 = 101
3 = 011
-------
6 = 110
```

To get powers we need to use `5**3`.

---

## What they didn't teach you in maths
There is one operator that wasn't taught in school that is actually very
important. This is the **modulo** operator, `4 % 3`. This operation gives
the remainder of a division.

In the example `4 % 3` we have a remainder 1. The operation is very important
when you're checking if a number is divisible by another. If a number if
divisible then there won't be any remainder, `562 % 2 = 0`.

---

## Highly advanced calculator
Ok let's try some more stuff with our calculator. In mathematics we have the
concept of unknowns like when we're asked to solve for x. Let's try something,
```
x = 2*(5-2)/3
```
When we run this command in our prompt we get... nothing? Well don't worry, in
programming it's common that if there's nothing said then there's nothing wrong!

To get our answer we have to write `x` without being on the left of
an equal sign, i.e. `x =` (more on this later).

Note how I said *without an equal sign*. That means we can also do `x + 4` and,
as long as it isn't `x + 4 =`, it does exactly what we suspect.

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
Take a look at what we've done with `x` in the past few sides. `x=2*(5-2)/3`
means we first put `2*(5-2)/3` *into* `x`. But the computer is lazy so instead
will first evaluate `2*(5-2)/3` to `2.0` and then places that value into `x`.

When we run something like `x+2`, since there's no equals sign thus we peek
inside our `x` variable and replace `x+2` with `2.0+2` which evaluates to `4.0`.

This is a very difficult topic to wrap your head around the first time since it
goes against what you've probably been taught at school. Take some time to
practice and digest this.

---

## Reflect
Now let's put proper names to what we've learnt.

When we type `1` or `0.32` or 'False` we call these *literals*.

This `x` that we've been using is known as a *variable*.
This is because the value can vary.

When we put a value into a variable like `x=3` we call this an *assignment*.
This is because we're assigning a literal to a variable.
