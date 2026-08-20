# In this file, we will learn about the famous library: re (Regular Expressions)

"""
Your learning path: 
Day 1 → [] . \d \w \s
       ↓
Day 2 → * + ? {n,m}
       ↓
Day 3 → ^ $ \b | ()
       ↓
Day 4 → findall search match sub split
       ↓
Day 5 → Email Phone URL Date
       ↓
Day 6 → 20 practice problems
       ↓
Day 7 → Build your own Text Extractor
"""

# "re" stands for Regular Expressions
import re  # Built-in library for finding patterns in text

#........................................................................................... 
# Level 1: Character Basics

text = "cat cot cut got get git gat"
print(re.findall(r'c[uo]t', text))                             #1.| [] → choice                        
print(re.findall(r'g.t', text))                                #2.| "." → any character 
print(re.findall(r'[aeiou]', text))                            #3.| [aeiou] = Match ONE character that is a, e, i, o, or u.

text = "My numbers are 123 and 456"
print(re.findall(r'\d', text))                                 #1.|  \d = single digits
print(re.findall(r'\d+', text))                                #2.|  \d+ means one or more digits.
print(re.findall(r'\s', text))                                 #3.|  \s = whitespace


text = "Hello_@123!" #, @, ! > no use here
print(re.findall(r'\w', text))                                 #1.|  \w = word character
print(re.findall(r'\w+', text))                                #2.|  \w+      one or more word characters

#........................................................................................... 
# Level 2: Quantifiers

text = "ct cat caat caaat color colour colouur"
print(re.findall(r'ca*t', text))                               #1.|  ca*t, here, a can appear 0 or more times
print(re.findall(r'ca+t', text))                               #2.|  ca+t, here, requires at least ONE a
print(re.findall(r'colou?r', text))                            #3.|  colou?r, here, u is optional (0,1 only)

text = "a aa aaa aaaa aaaaa 1 12 123 1234 12345"
print(re.findall(r'a{2,4}', text))                             #1.|  a{2,4}, here, minimum 2 and maximum 4
print(re.findall(r'\b\d{2,4}\b', text))                        #2.|  \d{2,4}, Between 2 and 4 digits | \b = word boundary
print(re.findall(r'a{3}', text))                               #3.|  r'a{3}', here, {n} = Exactly this many.     || This becomes extremely useful for dates -> r'\d{4}-\d{2}-\d{2}' = 2026-08-19
print(re.findall(r'a{2,}', text))                              #4.|  r'a{2,}', here, {n,} = n or More

text = "I am running and jumping today"
print(re.findall(r'\b\w+ing\b', text))                         #1.|  \b = word boundary | \w+ = one or more word characters | ing = literal "ing" | \b = word boundary

#........................................................................................... 
# Level 3: Position & Groups

text = "Python is easy. I love python"
print(re.findall(r'^Python', text))                            #1.| (^) = Start of the string.
print(re.findall(r'python$', text))                            #2.| ($) = end of the string.

text = "cat caterpillar scatter cat, I have a cat and a dog"
print(re.findall(r'cat', text))                                #1.| r'cat' = Without boundaries | r'\bcat\b' = not to find inside words: caterpillar
print(re.findall(r'\b(cat|dog)\b', text))                      #2.| "|" = OR, 

text = "Azeem: 26, John: 30, Jane: 25, Bob: 40"
print(re.findall(r'(\w+): (\d+)', text))                       #1.| here, () create groups | (\w+) → name | : → literal : | space → literal space | (\d+) → age

#........................................................................................... 
# Level 4: Python re Functions

text = "I have 10 apples and 20 oranges"
print(re.findall(r'\d+', text))                                #1.| findall() = FIND ALL

result = re.search(r'\d+', text)                               #2.| search() = find the first match
print(result.group())                                             # .group() = a method which Match extraction

text = "Python is powerful"
result = re.match(r'Python', text)                             #3.| match() = checks from the beginning.
print(result.group())

text = "My numbers are 123 and 456"
print(re.sub(r'\d+', '***', text))                             #4.| sub = substitute / replace

text = "hello   world    python"
print(re.split(r'\s+', text))                                  #5.| split() = Split using regex | \s+ handles all spaces.

#........................................................................................... 
# Level 5: Real-World Regex

text = "Contact me at john@example.com"                        #1.| Email Syntax:  username → john | @ → @ | domain → example.com
print(re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', text))

text = "Call me at 555-123-4567"             
print(re.findall(r'\d{3}-\d{3}-\d{4}', text))                  #2.| Phone number: \d{3} → 555 | - → - | \d{3} → 123 | - → - | \d{4} → 4567  

text = "Today is 2026-08-20 and tomorrow is 2026-08-21"
print(re.findall(r'\d{4}-\d{2}-\d{2}', text))                  #3.| Date: YYYY-MM-DD => \d{4}-\d{2}-\d{2}

text = "Visit https://google.com for more information"
print(re.findall(r'https?://\w+\.\w+', text))                  #4.| https? → http or https:// → literal | \w+ → domain | \. → literal dot | \w+ → extension

text = "I love #python and #programming"
print(re.findall(r'#\w+', text))                               #5.| #keywords: # → literal # | \w+ → one or more word characters

#........................................................................................... 
# Level 6: Build Regex From Structure

text = "Items cost $9.99, $4.50 and $100"
print(re.findall(r'\$\d+(?:\.\d{2})?', text))                  #1.| here, (?:...) means a non-capturing group | Price: $ → digits → optional decimal-(2)

text = "Meeting at 10:30am and another at 08:45pm"
print(re.findall(r'\d{2}:\d{2}.m?', text))                     #2.| \d{2}= 2digits | : = :| \d{2} = 2digits |.m = am/pm

text = "Users: john123, user_99, python_dev"
print(re.findall(r'\b\w+\b', text))                            #3.| \w+ = it represent letters, numbers, and _

#........................................................................................... 
# Final Project

import re
import json 

text = """
Contact john@example.com, admin@web.dev,
or jane123@gmail.com.

Call 555-123-4567 or international line +1-800-555-0199.

Visit https://google.com, http://domain.org, or ://test.com.

Price: $19.99, clearance item for $4.50, and wholesale at $1,250.00.

Date: 2026-08-20, secondary milestone on 2027-11-05.

Tags: #python #regex #coding #developer_life #ai2026
"""
# Result Pattern: Emails | Phones | URLs | Prices | Dates | Hashtags

# Email pattern matching standard email addresses
email_pattern = (
    r'[a-zA-Z0-9._%+-]+'  # Matches the username portion (letters, digits, and valid special characters)
    r'@'                  # Matches the literal '@' separator
    r'[a-zA-Z0-9.-]+'     # Matches the domain name portion (letters, digits, hyphens, and dots)
    r'\.[a-zA-Z]{2,}'     # Matches the literal dot followed by a top-level domain of 2 or more letters
)

# Phone pattern matching local, formatted, and international phone numbers
phone_pattern = (
    r'(?:\+?\d{1,3}[-.\s]?)?'  # Optional non-capturing group: country code (+1, +44) and optional separator
    r'\(?\d{3}\)?'             # Matches a 3-digit area code, optionally wrapped in parentheses: (123) or 123
    r'[-.\s]?'                 # Matches an optional separator: a dash, dot, or space
    r'\d{3}'                   # Matches the next 3 digits of the phone number
    r'[-.\s]?'                 # Matches another optional separator: a dash, dot, or space
    r'\d{4}'                   # Matches the final 4 digits of the phone number
)

# URL pattern matching web addresses with deep paths and query variables
url_pattern = (
    r'https?://'                     # Matches 'http://' or 'https://' protocol prefixes
    r'(?:www\.)?'                    # Optional non-capturing group: matches 'www.' if present
    r'[-a-zA-Z0-9@:%._+~#=]{1,256}'  # Matches the core domain string up to 256 valid URL characters long
    r'\.[a-zA-Z0-9()]{2,6}\b'        # Matches domain extension (like .com or .tech) and enforces a word boundary
    r'[-a-zA-Z0-9()@:%_+.~#?&/=]*'   # Captures remaining paths, trailing slashes, tracking IDs, or query strings
)

# Price pattern using an OR (|) operator to capture numbers with or without commas
price_pattern = (
    r'\$\d{1,3}(?:,\d{3})*(?:\.\d{2})?'  # Matches comma-separated prices: $1,000, $1,250.50, $40,000,000
    r'|'                                 # Alternation operator: functions as a logical OR fallback
    r'\$\d+(?:\.\d{2})?'                 # Matches flat numbers without comma formatting: $100, $9.99, $1250
)

# Date pattern strictly validating YYYY-MM-DD structures
date_pattern = (
    r'\b'                       # Enforces a word boundary to prevent partial matches inside longer number blocks
    r'\d{4}-'                   # Matches a strict 4-digit year format followed by a literal hyphen
    r'(?:0[1-9]|1[0-2])-'       # Validates months: restricts options exclusively to 01-09 or 10-12 plus a hyphen
    r'(?:0[1-9]|[12]\d|3[01])'  # Validates days: restricts options exclusively to 01-09, 10-29, or 30-31
    r'\b'                       # Enforces a trailing word boundary to isolate the date string safely
)

# Hashtag pattern extracting isolated social media tags
hashtag_pattern = (
    r'\B'   # Non-word boundary: ensures the '#' is not immediately preceded by alphanumeric characters
    r'#'    # Matches the literal '#' symbol
    r'\w+'  # Matches one or more alphanumeric characters or underscores following the symbol
)

result = {
    "emails": re.findall(email_pattern, text),
    "phones": re.findall(phone_pattern, text),
    "urls": re.findall(url_pattern, text),
    "prices": re.findall(price_pattern, text),
    "dates": re.findall(date_pattern, text),
    "hashtags": re.findall(hashtag_pattern, text)
}
# print(result)

#........................................................................................... 
# TERMINAL JSON PRINTER

# json.dumps() converts the dict to a string. 
# indent=4 formats it with clean spacing line-by-line.
print(json.dumps(result, indent=4))
