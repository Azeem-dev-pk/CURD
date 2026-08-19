# in this file, we will learn about most famous library: Response

# import response
# import requests

import re

text = "cat cot cut got get"
print(re.findall(r'c[uo]t', text))                           
print(re.findall(r'c.t', text))

text = "My numbers are 123 and 456"
print(re.findall(r'\d', text))
print(re.findall(r'\d+', text))             #. |        \w → word, \d → digit, \s → space, [] → choice, "." → any character

text = "Hello_@123!" #, @, ! ❌
print(re.findall(r'\w', text))

text = "ct cat caat caaat color colour colouur"
print(re.findall(r'ca*t', text))            #1. |  ca*t, here, a can appear 0 or more times
print(re.findall(r'ca+t', text))            #2. |  ca+t, here, requires at least ONE a
print(re.findall(r'colou?r', text))         #3. |  colou?r, here, u is optional (0,1 only)

text = "a aa aaa aaaa aaaaa"
print(re.findall(r'a{2,4}', text))          #1. |  a{2,4}, here, minimum 2 and maximum 4
print(re.findall(r'a{3}', text))            #2. |  r'a{3}', here, {n} = Exactly this many.     || This becomes extremely useful for dates -> r'\d{4}-\d{2}-\d{2}' = 2026-08-19
print(re.findall(r'a{2,}', text))           #3. |  r'a{2,}', here, {n,} = n or More



