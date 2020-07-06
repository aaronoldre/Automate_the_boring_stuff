import re

beginsWithHelloRegex = re.compile(r'^Hello')
mo = beginsWithHelloRegex.search('Hello there')
# returns 'Hello'

beginsWithHelloRegex.search('He said Hello') == None
# hello is at the end 

endsWithWorldRegex = re.compile(r'world!$')
endsWithWorldRegex.search('Hello world!')
# returns 'world!'

allDigistRegex = re.compile(r'^\d+$')
allDigistRegex.search('2344566784466')
# all digits
allDigistRegex.search('2344x566784466') == None # because x in middle

atRegex = re.compile(r'.at') # anything followed by 'at'
mo = atRegex.findall('The cat in the hat sat on the flat mat.')
print(mo)

atRegex = re.compile(r'.{1,2}at') # anything followed by 'at'
mo = atRegex.findall('The cat in the hat sat on the flat mat.')
print(mo) # looks for letter or space before the 'at'

nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
# .* uses greedy mood
mo = nameRegex.findall('First Name: Al Last Name: Sweigart')
print(mo)

serve = '<To serve humans> for dinner.>'

nongreedy = re.compile(r'<(.*?)>')
mo = nongreedy.findall(serve)
print(mo)

greedy = re.compile(r'<(.*)>')
mo = greedy.findall(serve)
print(mo)


prime = 'Serve the public trust.\nProtect the innocent.\nUpload the law.'
print(prime)
dotStar = re.compile(r'.*')
mo = dotStar.findall(prime)
print(mo) # stops after first line

dotStar = re.compile(r'.*', re.DOTALL)
mo = dotStar.findall(prime)
print(mo) # prints all

# case insensative
vowelRegex = re.compile(r'[aeiou]')
mo = vowelRegex.findall('Al, why does your python book talk about Robocop so much?')
print(mo) # prints list of all lowercase vowels

vowelRegex = re.compile(r'[aeiou]', re.I)
mo = vowelRegex.findall('Al, why does your python book talk about Robocop so much?')
print(mo) # prints list of all vowels


