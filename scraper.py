# from bs4 import BeautifulSoup
# import requests
# # >> https://pk.linkedin.com/jobs/search?keywords=Front-End%20Development&location=Lahore&geoId=104112529&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0
# html_text = requests.get('https://pk.linkedin.com/').text
# # print(html_text)
# soup = BeautifulSoup(html_text)
# soup.text
# j = soup.find('body').text.replace(' ','')
# print(url)


# import requests
# from bs4 import BeautifulSoup

url = "https://pk.linkedin.com/jobs/business-development-jobs-lahore?trk=homepage-basic_suggested-search&position=1&pageNum=0"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
# }
# response = requests.get(url, headers=headers)

# # Check if successful
# if response.status_code == 200:
#     print("Page fetched!")
#     html = response.headers     
#     # print(html)
# else:
#     print(f"Failed: {response.status_code}")

# soup = BeautifulSoup(response.text, "html.parser")
# # print(soup.prettify())

# bucket = soup.find_all('h3')
# # for one_toy in bucket:   # Now 'one_toy' is a single Tag!
# #     print(one_toy.text)  # Now you can look at the toy's text!




# step_1_basics.py
# RUN THIS FIRST. No internet required.

print("--- STEP 1: Python Basics ---")

# 1. String & Variable
# url = "https://example.com"
print(f"1. URL stored: {url}")

# 2. List (like a bucket)
links = ["/job1", "/job2", "/job3"]
print(f"2. List of links: {links}")

# 3. Dictionary (Key-Value pairs)
job = {"title": "Engineer", "salary": 80000}
print(f"3. Single Job Dict: {job}")

# 4. For Loop (going through the bucket)
print("4. Looping through the list:")
for link in links:
    print(f"   - Now processing: {link}")

# 5. Function (reusable block)
def greet(name):
    return f"Hello, {name}"

print(f"5. Function output: {greet('Student')}")

# 6. Try/Except (Error handling)
try:
    result = 10 / 0  # This will fail
except ZeroDivisionError:
    print("6. Error handled gracefully! (Didn't crash)")

print("\n✅ STEP 1 PASSED. If you see this, your Python is ready.")