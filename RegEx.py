import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
321-555-4421
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

text01 = '''123456789abce&&myemail@mail.com'''

emails = '''
bala@gmail.com
bala.rmur@gmail.edu
bala-123@my-wrok.net
'''


urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''
#pattern = re.compile(r'[$a-z]')
pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z-]+\.(com|edu|net)')
links = re.compile(r'(http[s])*://(www\.)?([a-zA-z]+)(\.[a-zA-z]+)')




matches = links.finditer(urls)

for match in matches:
	a= match.group(3)+match.group(4)
	print (a)