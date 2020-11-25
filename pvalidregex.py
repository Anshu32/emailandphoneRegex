#! python3

import re

passRegex = re.compile(r'''
	^(?=.*[a-z])                #    ==>
	(?=.*\d)                    #    ==>
	(?=.*[A-Z])                 #    ==>
	(?=.*[@!#$%^&*?])           # positive lookaheads
	[A-Za-z\d@!#$%^&*?]         # conditions for lower case upper case one number and special character
	{8,15}$                     # length of the password
	''',re.VERBOSE)

text = input()

mo = passRegex.search(text)

if mo:
	print("Valid password")
else:
	print("Not a valid password")
