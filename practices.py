
# x = 1d

import requests
import re


class Scrapper:
    
    def __init__(self, name= "site:", url = "https://www.wikipedia.com"):

        # self.url = url
        # self.name = name
        # r = requests.get(url)
        # # print("Data:", r.content)
        # self.content = str(r.content)
        # urls = re.findall(r'https?://\w+\.\w+', self.content)
        # print("hi bro urls are:",urls ," Ends Here")
        # urls = re.findall(r'https?://[^\s"\'<>]+', self.content)
        # #updates
        # print("hi bro urls are:",urls ," Ends Here")
        

        self.url = url
        self.name = name
        r = requests.get(url)

        # IMPROVEMENT 1: Use r.text instead of str(r.content)
        self.content = r.text 

        # IMPROVEMENT 2: Use a better regex pattern
        # [^\s"\'<>]+ means: "Match everything EXCEPT spaces, quotes, and angle brackets"
        urls = re.findall(r'https?://[^\s"\'<>]+', self.content)

        # IMPROVEMENT 3: Remove duplicates using set()
        unique_urls = list(set(urls))

        # Print cleanly
        print(f"Found {len(unique_urls)} unique URLs for {self.name}:")
        for u in unique_urls:
            print(f" - {u}")

    def html(self):
        #self = self.content
        print("Html counts:", self.content.count("<html"))

    def head(self):
        # input("press enter to start: ")
        print("Head counts:", self.content.count("<head"))

    def title(self):
        print("Title counts:", self.content.count("<title"))

    def body(self):
        print("Body counts:", self.content.count("<body"))

    def h1(self):
        print("h1 counts:", self.content.count("<h1"))

    def a(self):

        print("<a> counts:", self.content.count("<a"))

    def p(self):

        print("<p counts:", self.content.count("<p"))

    def i(self):

        print("<i counts:", self.content.count("<i"))

    def to_string(self):
        self.html()
        self.head()
        self.title()
        self.body()
        self.h1()
        self.a()
        self.p()


    def tree(self):
        print()


# s1 = Scrapper()
s2 = Scrapper("JSON placeholder", "https://jsonplaceholder.typicode.com/")
# s3 = Scrapper("Chuck norris api", "https://api.chucknorris.io/")

# defaults

#x = s1.url
#y s1.name
# print(y, x)
# print(f"2: {s2.name}, {s2.url} ")
# print(f"3: (s3.name}, {s3.url}")

# s1.html()
# s1.head()
# s1.title()
# s1.body()
# s1.h1()
# s2.a()
# s1.p()
#s1.i()

#s3.to_string()
#r = requests.get('https://jsonplaceholder.typicode.com/')
#print(r.content)

# s2.tree()

