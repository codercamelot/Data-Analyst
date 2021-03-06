# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AUC2SoVZs06wwWjyQ6SI0QwZXdWsaN6H

Name: Shekhar Shrestha

Python for Data Analytics

What is Python and why is it useful?

Python is a high level programming language. It is useful for different purposes for web development , data science, machine learning etc.

# Create a variable that holds the string “hello there!”
"""

a = 'hello there!'
print(a)

"""Create a variable for first name, last name and an email extension.  
Concatenating all three together to form an email address.  For example: firstnamelastname@gmail.com
"""

first_name = 'coder'
last_name = 'camelot'
email_ext = '@gmail.com'
print(first_name + last_name + email_ext)

"""Store someone you know name in a variable called name.  Print their name in lower and uppercase using a method."""

name = 'coder2020camelot'
print(name.upper())
print(name.lower())

"""Using a variable, ask your friend if they want to hang out on the 15th of the month.  For example, “Do you want to hang out on the 15th of this month?”  You should have to convert the number to a string."""

hang_out = input("Do you want to hang out on the 15th of this month? (yes/no):")
print(hang_out)

"""UNIT 2

Create a list of 5 of your favorite tv shows.
"""

Tv_Shows = ['Friends','The office','Jack Ryan','limitless','The Silicon Valley']
# print(Tv_Shows)

"""Print the list in its original order."""

print(Tv_Shows)

"""Use the sorted() function to print the list in alphabetical order.  How is sorted() different from sort()?

sorted() method sorts the given sequence either in ascending order or in descending order and always return the a sorted list

Print out your original list.
"""

print(Tv_Shows)

"""Used sorted() to print your list in reverse alphabetical order."""

a = sorted(Tv_Shows, reverse = True)
print(a)

"""Create a message indicating how many favorite TV shows you have – use the len() function."""

message = "You have {message} favourite TV shows".format(message = len(Tv_Shows))
print(message)