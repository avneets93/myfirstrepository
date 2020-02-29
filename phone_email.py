#! python3

import re, pyperclip

#Create a regex for phone number
phoneRegex = re.compile('''
# 415-444-0000, 555-8889, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345
(
((\d\d\d)|(\(\d\d\d))?   #area code(optional)
(\s|-)    #first separator
\d\d\d  #first three digits
-      #separator
\d\d\d\d    #last 4 digits
(((ext(\.)?\s)?|x)(\d{1,5}))?	 #extension(optional)
)
''',re.VERBOSE)

#Create a regex for email address
emailRegex = re.compile('''
[a-zA-Z0-9.+]+   #name part
@  #@ symbol
[a-zA-Z0-9.+]+   #domain part
''',re.VERBOSE)

#Get the text off the clipboard
text = pyperclip.paste()

#Extract the email/phone from this text 
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
	allPhoneNumbers.append(phoneNumber[0])

#print(allPhoneNumbers)
#print(extractedEmail)
#Copy the extracted email/phone to the clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)

