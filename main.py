#Write a program to count the occurrences of a specific character in a string.
string_data=input("Enter a string: ")
#using count() method
for ch in string_data:
    print( ch,"occured", string_data.count(ch), "times")
