import re

batRegex = re.compile(r'Bat(wo)?man')
mo = batRegex.search("The Adventures of Batman")
print(mo.group()) # returns 'Batman'

mo = batRegex.search('The Adventures of Batwoman')
print(mo.group()) # returns 'Batwoman'

mo = batRegex.search('The Adventures of Batwowowoman')
# print(mo.group()) # returns None

phoneRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneRegex.search('My phone number is 415-555-4242. Call me tomorrow.')
print(mo.group())# returns '415-555-4242'

mo = phoneRegex.search('My phone number is 555-4242. Call me tomorrow.')
# mo.group() # returns None

# using '?'
phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo = phoneRegex.search('My phone number is 555-4242. Call me tomorrow.')
print(mo.group())
mo = phoneRegex.search('My phone number is 415-555-4242. Call me tomorrow.')
print(mo.group())


# using '*''
batRegex = re.compile(r'Bat(wo)*man')
mo = batRegex.search("The Adventures of Batman")
print(mo.group()) # returns 'Batman'

mo = batRegex.search('The Adventures of Batwoman')
print(mo.group()) # returns 'Batwoman'

mo = batRegex.search('The Adventures of Batwowowoman')
print(mo.group()) # returns 'Batwowowoman'

# using '+'
batRegex = re.compile(r'Bat(wo)+man')
mo = batRegex.search("The Adventures of Batman")
# print(mo.group()) # returns None

mo = batRegex.search('The Adventures of Batwoman')
print(mo.group()) # returns 'Batwoman'

mo = batRegex.search('The Adventures of Batwowowoman')
print(mo.group()) # returns 'Batwowowoman'

regex = re.compile(r'\*\(\?\+')
mo = regex.search('I learned about +, *, and ?s in school today')
# print(mo.group()) # returns None because looking for specific pattern

haRegex = re.compile(r'(Ha){3}')
mo = haRegex.search('He said "HaHaHa"')
print(mo.group()) # Returns 'HaHaHa'

phoneRegex = re.compile(r'((\d\d\d-)?\d\d\d-\d\d\d\d(,)?){3}')
mo = phoneRegex.search('My numbers are 415-555-1234,415-555-4242,222-555-0000')
print(mo.group()) # Returns '415-555-1234,415-555-4242,222-555-0000'

haRegex = re.compile(r'(Ha){3,5}')
mo = haRegex.search('He said "HaHaHa"')
print(mo.group()) # Returns 'HaHaHa'

mo = haRegex.search('He said "HaHaHaHaHaHa"')
print(mo.group()) # Returns 'HaHaHaHaHa'

haRegex = re.compile(r'(Ha){3,}')
mo = haRegex.search('He said "HaHa"')
# print(mo.group()) # Returns None

# greedy version
digitRegex = re.compile(r'(\d){3,5}')
mo = digitRegex.search('1234567890')
print(mo.group()) # Returns '12345'

# non-greedy version
digitRegex = re.compile(r'(\d){3,5}?')
mo = digitRegex.search('1234567890')
print(mo.group()) # Returns '123'
