#! python3

import re, pyperclip

#Create a regex for phone numbers

phoneRegex = re.compile(r'''
(
((\d\d\d) | (\(\d\d\d\)))?				# area code optional
(\s|-)									# first separator
\d\d\d								# first three digits
-									# separator
\d\d\d\d								# last 4 digits
(((ext(\.)?\s) | x)						# extension word-part optional
(\d{2,5}))?
)							# extension number part optional between 2 to 5 digits
	''', re.VERBOSE)

#Create a regex for email addresses

emailRegex = re.compile(r'''
[a-zA-Z0-9_.+]+							# name part
@										# @symbol
[a-zA-Z0-9_.+]+							# domain name

	''',re.VERBOSE)

#get the text off the clipboard

text = pyperclip.paste()

#Extract the email/phone from the text

extractedphone = phoneRegex.findall(text)
extractedemail = emailRegex.findall(text)

allphonenumbers = []

for phonenumber in extractedphone:
	allphonenumbers.append(phonenumber[0])

results = '\n'.join(allphonenumbers) + '\n'.join(extractedemail)
pyperclip.copy(results)
