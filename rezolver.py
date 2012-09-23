# -*- coding: utf-8 -*-

filename = "dict.csv"

lookup = {}

with open(filename,"r") as file:
    for line in file:
    	(key, value) = line.split(" ")[0:2]
    	lookup[key] = value

print(lookup)

pair = raw_input("Enter <address> <name> pair: ")

try:
    file = open(filename, "a")
    try:
    	file.write("\n")
    	file.write(pair)
    finally:
        file.close()
except IOError:
    print("Error occured "+IOError)