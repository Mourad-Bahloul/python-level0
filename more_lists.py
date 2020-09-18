import statistics
from random import shuffle

notes = [3, 4, 6, 8, 5, 4, 9]
print(notes)
shuffle(notes)  # reorganise the content
print(notes)
shuffle(notes)  # reorganise the content
print(notes)

# use of statistics module
average_note = statistics.mean(notes)
print("mean note is {}".format(average_note))

# split a string into a list
txt = "hello, my name is Peter, I am 26 years old"

x = txt.split(", ")

print(x)
