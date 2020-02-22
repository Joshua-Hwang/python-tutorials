---
marp: true
---

# Basic containers
This document will teach ideas like loops and containers such as
lists, dictionaries and sets.

---

## Loops
So we've seen `if-else` statements now we will show you the other tools of
control flow. Looping will allow you to repeat pieces of code multiple times.

---

## FizzBuzz
You're in an interview. It's going really well!
They seem to really like what you've talking about, you've got this in the bag.
But before you can get too comfortable,
the most difficult part of any software developer
interview is about to take place... FizzBuzz.

> Replace any number divisible by three with the word "fizz",
> and any number divisible by five with the word "buzz".
> If a number if both then print "fizzbuzz". If none of these just print the
> number.
> Do this for 0 to 200.

Can you master this final challenge and nail the interview?

---

## How can we do this?
Well we have our trusty `if` statements now. But if we try to use just this,
we'll realise that we have to copy and paste for *every* number. There's no way
the interviewers are going to be happy with that.
```Python
number = 2
if number % 3 == number % 5 == 0:
  print("fizzbuzz")
elif number % 3 == 0:
  print("fizz")
elif number % 5 == 0:
  print("buzz")
else:
  print(number)
```

---

## Enter loops
Do not worry, we'll use Python `for` loops!
```Python
for number in range(10):
  print("the current number is", number)
```

Hopefully the `for` loop pattern makes sense; for each `number` in the `range`
of numbers up to 10, `print()` a sentence involving the `number`.
If you tried this piece of code you'll find that the print happens 10 times and
prints a different number of repetition. We call this **iteration** across
`range(10)`. `range(10)` is the set of integers from 0 to 9.

Now we can replace the print statement with our previous code.

---
```Python
for number in range(200):
  if number % 3 == number % 5 == 0:
    print("fizzbuzz")
  elif number % 3 == 0:
    print("fizz")
  elif number % 5 == 0:
    print("buzz")
  else:
    print(number)
```

---

## Motivating example
Congrats! After your *impressive* solution to the fizzbuzz problem you have
volunteered to be the host for a company event tonight.
The event tonight has some *very* important guests coming. It's vital
that they get invited on stage in the right order.

Here's the **list**,
```Python
names = ["Jason", "Brenda", "Sam", "Cohen", "Ashley"]
```

The names are in the correct hierarchy from left to right.

---

## What do we do with that?
We *could* grab the names and print them each. But what will happen if more
people are added last minute? What if Sam gets a surprise promotion tonight and
you call the names in the wrong order. Embarrassing!

---

## For loop to the rescue
```Python
names = ["Jason", "Brenda", "Sam", "Cohen", "Ashley"]
for name in names:
  print("Please welcome,", name)
```

Not only can `for` loop **iterate** across a `range` of numbers.
We can also use a `for` loop to **iterate** across a list of names.

---

## More lists
The event went smoothly the entire night. As the night rolls to a close the
woman from table 11 is beginning to approach you.
Unfortunately you can't remember her name for the life of you!

All you have is this list of assigned tables containing all the employees
in order of their table number.
```Python
employees = ["James", "Mary", "John", "Patricia", "Robert", "Jennifer",
"Michael", "Linda", "William", "Elizabeth", "David", "Barbara", "Richard",
"Susan", "Joseph", "Jessica", "Thomas", "Sarah", "Charles", "Karen",
"Christopher", "Nancy", "Daniel", "Margaret", "Matthew", "Lisa", "Anthony",
"Betty", "Donald", "Dorothy", "Mark", "Sandra", "Paul", "Ashley", "Steven", 
"Kimberly", "Andrew", "Donna", "Kenneth", "Emily", "Joshua", "Michelle",
"George", "Carol", "Kevin", "Amanda", "Brian", "Melissa", "Edward", "Deborah",
"Ronald", "Stephanie"]
```

You certainly can't iterate over the list and try the names of every employee! What do you do.

---

## Indexing
Luckily lists have an additional feature.
```Python
print("Hi", employees[11])
```

TODO: make some note about it's 0-based index

