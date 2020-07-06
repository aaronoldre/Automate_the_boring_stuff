import re

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# phoneRegex.findall() # finds all the phone numbers in our search
# returns list of strings and not match object if no groups are given

phoneRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
# returns tuple with area code and local number
phoneRegex = re.compile(r'((\d\d\d)-(\d\d\d-\d\d\d\d))')
# returns tuple with full number, area code, and local number
mo = phoneRegex.findall('home 415-555-4242 cell 412-555-5555')
print(mo) # returns list of tuples of strings

# character classes
digitRegex = re.compile(r'0|1|2|3|4|5|6|7|8|9')
# \d for 0 to 9
# \D for everything not 0 to 9
# \w any letter, digit, underscore
# \W evertyhing not a letter, digit, or underscore
# \s space, tab, new lines
# \S everything not a space, tab or new line

lyrics = """
On the twelfth day of Christmas
My true love gave to me
12 drummers drumming
11 pipers piping
10 lords a leaping
9 ladies dancing
8 maids a milking
7 swans a swimming
6 geese a laying
5 gold rings, badam-pam-pam
4 calling birds
3 French hens
2 turtle doves
And 1 partridge in a pear tree"""

xmasRegex = re.compile(r'\d+\s\w+')
mo = xmasRegex.findall(lyrics)
print(mo)

# make your own class
vowelRegex = re.compile(r'[aeiouAEIOU]')  # r'(a|e|i|o|u)'
mo = vowelRegex.findall('Robocop easts baby food.')
print(mo)

doublevowelRegex = re.compile(r'[aeiouAEIOU]{2}')  # finds double vowels
mo = doublevowelRegex.findall('Robocop easts baby food.')
print(mo)

consonantsRegex = re.compile(r'[^aeiouAEIOU]')  # r'(a|e|i|o|u)'
mo = consonantsRegex.findall('Robocop easts baby food.')
print(mo)