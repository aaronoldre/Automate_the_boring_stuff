import re

namesRegex = re.compile(r'Agent \w+')
mo = namesRegex.findall('Agent Alice gave the secret documents to Agent Bob.')
print(mo)

# find and replace agent names with REDACTED
mo = namesRegex.sub('REDACTED', 'Agent Alice gave the secret documents to Agent Bob.')
print(mo)

# find and replace with code names
# finds first letter of name
namesRegex = re.compile(r'Agent (\w)\w*')
mo = namesRegex.findall('Agent Alice gave the secret documents to Agent Bob.')
print(mo)

# Agent Alice becomes Agent A*****
mo = namesRegex.sub(r'Agent \1*****', 'Agent Alice gave the secret documents to Agent Bob.')
print(mo)

re.compile(r'''
(\d\d\d-)|   # area code (without parens, with dash)
(\(\d\d\d\) ) # -or- area code with parens and no dash

\d\d\d   # first 3 digits
-        # second dash
\d\d\d\d # last 4 digits
\sx\d{2,4}  # extension, like x1234''', re.IGNORECASE | re.DOTALL| re.VERBOSE) # pipe allows for multiple of the re options as second argument