# Exception handling exercises
## Index error
Your company has a number of records for few of it's loyal customers.
Each membership number is associated with an index in the following list.
```python
members = {"Alex", "Bertha", "Cooper", "Diana", "Elvis", "Francine"}
memberNumber = int(input("Please input the members number to get the name\n> "))
print(members[memberNumber])
```

Unfortunately our frontline guys keep mistyping and sending the whole server
into shutdown!

How could we use try-except blocks to handle the errors?

## Another error
Well that has certainly stopped some of the crashes. But now we're discovering
that some of the employees accidentally mistype and might add a character by
mistake causing a `ValueError` to occur.

The team is considering getting keyboards with numpads to prevent the errors
from occurring. But they need to know how many of such errors are actually
occurring.

Following from the previous exercise, could you also add a second except block
that catches and records the number of `ValueError`s but **not** `IndexError`s.

## A new system
The backend team has finally decided to establish a more realistic database
solution. They have chosen to go with a single file on the company laptop! Now
we need to open that file from our computer.

The following code has been provided. You do not need to worry about how to
access files.
```python
import os
filename = input("Please input the database to load\n> ")
data = open(os.path.join(os.path.dirname(__file__), filename))
```

Unfortunately we still need to make sure our employees don't type the wrong
filename. 