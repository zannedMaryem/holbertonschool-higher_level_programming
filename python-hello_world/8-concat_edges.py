#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
 language that combines remarkable power with very clear syntax"
str = str[:6] + str[38:66] + str[-23:-17]
str = str[7:] + str[:6]
print(str)
