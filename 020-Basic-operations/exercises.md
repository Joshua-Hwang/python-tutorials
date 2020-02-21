# Basic operations exercises
## Using variables
Convert the following into Python,
`y = 3 + i + x`
`i = 3/4`
`x = 3(4+5)`

## The division question
Consider `4/2` and `4-2` are the results the same?
How about `4.0-2` and `4-2.0`?
Why is this?

## The floating point question
Now let's take a look at this,
```
1/5 + 1/5 + 1/5 + 1/5 + 1/5
1/6 + 1/6 + 1/6 + 1/6 + 1/6 + 1/6
```
How strange...

Could you come up with an explanation for why this happens.

## Repeat these problems using VSCode

# Solutions
## Using variables
Should be pretty simple trial and error. You will probably hit a few walls,
remember to read the error messages and
think about why what you intend doesn't work out in Python.

## The division question
The answer has a few parts. Firstly, many languages prefer to separate decimal
numbers (also known as **floating points**) and integers.

Floating points are called such because the decimal point 'floats' around,
`1234.5`, `12.345` etc.

When we explicitly write `4.0` then the interpreter *knows* we want a floating
point number and it will store it as such. Even though `4.0` *can* be converted
to `4` very easily.

When we apply operations like addition and subtraction to integers
then we'll always get another integer out, `1+2=3`, `45-234=-189`.

When we apply these same operations but for floating point numbers it's only
natural to evaluate to another floating point.

When dealing with integer division we have no guarantee that another integer
will pop out. `4/2` might produce an integer sure but `4/3` won't. It's easier
for everyone to keep things consistent, thus all divisions are evaluated as
floating points.

Note: This was not always the case. In many other languages,
like C and even Python 2 (the old version of Python)
the division of two integers leads to an integer output.
If you still want that functionality you can use `4//3` (a double division sign).

The way integer division is defined is that it just erases all digits after the
decimal point. Thus `5//2 = 2` and `-5//2 = -2`.

## The floating point question
This is the reason why we separate integers from floating points.

A computer does not have infinite memory thus it can only store a finite number
decimal places.

Consider a computer than can only store 5 decimal places. In this computer a
computation like, `1/3 = 0.33333` might occur. But that isn't true,
we know the real answer is `1/3 = 0.333333333...` all to infinity, a computer
cannot hold such information in a floating point number.

The computer will attempt to resolve such *floating point precision errors*
in a variety of ways this is why the 1/5 will work but 1/6 won't;
even 1/8 works!


