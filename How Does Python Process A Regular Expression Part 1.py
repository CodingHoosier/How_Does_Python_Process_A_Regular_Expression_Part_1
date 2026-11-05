# https://www.youtube.com/watch?v=kWLfB8lrT4A
# How Does Python Process A Regular Expression? Part 1
# Bring in the library
#  that we need. 
import re
# Create a RegEx object
#  we can use later.
# Our pattern is any
#  combination of 
#  lower case letters
#  anywhere in the string.
regEx = "[a-z]"
p = re.compile(regEx)
my_str = "xyz"
# Check against our string.
# We matched the x in the
#  first position.
result = p.search(my_str)
print(f"result is of type {result}")
print(f"group(): {result.group()}")
print(f"start(): {result.start()}")
print(f"end(): {result.end()}")
# Now let's try it with a
#  sting that won't match.
# The result wuill be None.
my_str = "123"
result = p.search(my_str)
print(f"result is of type {result}")
# So, the easy way to check 
#  for a pattern match is 
#  to check for None.
result = p.search("12h45") 
if result is not None:
    print("Pattern found")
    print(f"Starting at index {result.start()}")
else:
    print("Pattern NOT found")
print("----------------")
# Search for 3 lower case
#  characters in a row...
regEx = "[a-z]{3}"
p = re.compile(regEx)
# This will match our RegEx:
my_str = "1234ppp999"
print(f"{p.search(my_str)}")
