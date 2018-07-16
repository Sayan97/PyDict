# -*- coding: utf-8 -*-
"""
Created on Sat Sep 30 17:25:40 2017

@author: Sayan
This is a program to find the definition of words as a dictionary
"""

#Importing  the libraries for use
import json
from difflib import get_close_matches

#Get the data file for the dictionary
data = json.load(open("data.json"))

#Function for searching in the data file
def look(a):
    a = a.lower()
    if a in data:
        return data[a]
    elif len(get_close_matches(a, data.keys(), cutoff=0.8)) > 0:
        if get_close_matches(a,data.keys(),cutoff=0.8)[0] == a.title():
            return data[a.title()]
            exit()
        check = input("Did you mean %s instead? [y/n]" % get_close_matches(a,data.keys(),cutoff=0.8)[0])
        if check.lower() == 'y':
            return data[get_close_matches(a,data.keys(),cutoff=0.8)[0]]
        elif check.lower() == 'n':
            return "Please enter the value again"
            exit()
        else:
            return "This entry is not valid, please try again."
            exit()
    else:
        return "The word you entered could not be found"

#Taking input from user
word = input("Enter the word: ")
check1 = look(word)

#Checking for the type of output generated
if type(check1) == list:
    for i in check1:
        print(i)
else:
    print(check1)
