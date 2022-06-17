---
marp: true
---

# Accessing files and other I/O
This document will teach you how to access files and write files.

---

## Motivating example: List all files with `CONFIDENTIAL`
You've just finished a bunch of documents to be released to a client. Just
before sending them you realise a crucial mistake, some of these documents
contain **confidential** information. But there are so many documents! How are
you going to know which files are confidential and which ones are good to send?

You would have to open each file, search the contents for the text
`CONFIDENTIAL` and create a list of bad files and files that okay to send.

---

## Reading a file
Luckily Python is here to rescue us! To open *ordinary text files*
```python
openedFile = open('document1.txt')
contentOfFile = openedFile.read()
print(contentOfFile)
```
`open()` produces a "file" object which we can manipulate like any other object in Python. We can `read` or `write` to this file object among other things.
`contentOfFile` is a variable containing the entire content of the `openedFile`. `contentOfFile` is a simple string like any other we've dealth with so far.

---

Now that `contentOfFile` is a string of the entire `document1.txt` searching for `"CONFIDENTIAL"` is a simpler exercise.

---

## An aside: opening more complex files.
Suppose you attempted this process with a `.docx` file. You'd likely find a bunch of binary garbage spewed out.
Largely this is because Word documents aren't just text, information on how this text should be formatted is stored additionally.

Take a look at the exercises for some possible solutions.

---

## Listing files
Well this only helps for a single file. Can we do better? Is there a way to load every file in the directory?

Yes! `os.listdir()` will let us do this.

```python
for filename in os.listdir():
    openedFile = open(filename)
    # ...
```

---

Congratulations, you've now identified the confidential documents.
The next step would be to replace `CONFIDENTIAL` with `<INFO ON REQUEST>`.

---

## Writing to a file
If you were following along with this example you may have noticed `write()` which is very similar to `read()` in its simplicity.

Attempting to use `write()` on any of the existing file objects you've been creating won't work however.

```
io.UnsupportedOperation: not writable
```

---

For a variety of reasons involving your operating system, you have to let Python know what you intend to do with the file prior to opening it.

Do you intend to write to this file? Read from this file? or both?

In order to communicate this you add a secondary value

```python
f = open('document4.txt', 'r') # r for reading
f = open('document4.txt', 'w') # w for writing
f = open('document4.txt', 'a') # for appending (read on for more info)
f = open('document4.txt', 'rw') # self-explanatory
```

---

### Difference between `a`ppend and `w`rite
These two words may seem to overlap in this scenario but they are important distinctions.
`write` overwrites what was in the file previously *entirely*.
`append` will merely add your text to the end of the file.

---

## Some notes on best practice
In most (all?) modern operating systems, there is a limit to the number of files a program can have open. If you attempt to open a file once this limit is exceeded you'll get an error from `open()`.
Thus when any program `open`s a file it's recommended to close the file object after you are done using it.
```python
openedFile.close()
```

---

A slightly nicer way to achieve the whole `open` and `close`
```python
with open('document2.txt') as openedFile:
    print(openedFile.read())
```

Once the code leaves the `with ... as` block the file will automatically be closed. This helps the coder know exactly when the file is no longer present.