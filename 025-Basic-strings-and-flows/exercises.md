# Basic operations exercises
## Teleprompter
You are working on an intelligent teleprompter. The teleprompter will adjust
the speech in accordance to what the audience is thinking.
```python
from random import random # ignore this line

audienceHappiness = random() - 0.5
print("Audience happiness at:", audienceHappiness)
#! happy: "So happy to be here!"
#! angry: "It's an honor to be here."

audienceHappiness = random() - 0.5
print("Audience happiness at:", audienceHappiness)
#! happy: "I see all the smiling faces in the crowd"
#! angry: "I hope my speech will provide some comfort to those in the audience"

audienceHappiness = random() - 0.5
print("Audience happiness at:", audienceHappiness)
#! happy: "For a prosperous tomorrow!"
#! angry: "For a better tomorrow!"
```
When `audienceHappiness` is greater than or equal to 0 then the audience is
happy otherwise the audience is angry.

We need you to implement the speech such that it handles when the audience is
happy and when they are not.
Replace the comments of the form `#!` with the correct implementation.

## Teleprompter \*cough\*
The teleprompter also needs to ensure the audience does not become too unruly.
A polite \*cough\* should help with that.

The audience is considered unruly when `audienceHappiness` is above `0.25` or
below `-0.25`. Before you print the line of the speech please print a `*cough*`.

# Solutions
## Teleprompter
```python
from random import random # ignore this line

audienceHappiness = random() - 0.5
print("Audience happiness at:", audienceHappiness)
if audienceHappiness >= 0:
  print("So happy to be here!")
else:
  print("It's an honor to be here.")

audienceHappiness = random() - 0.5
print("Audience happiness at:", audienceHappiness)
if audienceHappiness >= 0:
  print("I see all the smiling faces in the crowd")
else:
  print("I hope my speech will provide some comfort to those in the audience")

audienceHappiness = random() - 0.5
print("Audience happiness at:", audienceHappiness)
if audienceHappiness >= 0:
  print("For a prosperous tomorrow!")
else:
  print("For a better tomorrow!")
```

## Teleprompter \*cough\*
```python
from random import random # ignore this line

audienceHappiness = random() - 0.5
print("Audience happiness at:", audienceHappiness)
if audienceHappiness > 0.5 or audienceHappiness < 0.5:
  print("*cough*")
if audienceHappiness >= 0:
  print("So happy to be here!")
else:
  print("It's an honor to be here.")

audienceHappiness = random() - 0.5
print("Audience happiness at:", audienceHappiness)
if audienceHappiness > 0.5 or audienceHappiness < 0.5:
  print("*cough*")
if audienceHappiness >= 0:
  print("I see all the smiling faces in the crowd")
else:
  print("I hope my speech will provide some comfort to those in the audience")

audienceHappiness = random() - 0.5
print("Audience happiness at:", audienceHappiness)
if audienceHappiness > 0.5 or audienceHappiness < 0.5:
  print("*cough*")
if audienceHappiness >= 0:
  print("For a prosperous tomorrow!")
else:
  print("For a better tomorrow!")
```
