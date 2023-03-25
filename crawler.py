from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

new_links = set()
all_links = set()
visited = []
answer = []

initial = "https://cm2023.obss.io/2165506a-18f1-4322-a260-bd8b6dc2240e?lang=EN"

def getThem(url):
    global visited, answer
    new_links
    
    driver.get(url)
    lnks = driver.find_elements(By.TAG_NAME, "a")  # find all links
    for link in lnks:
        href = link.get_attribute("href")
        all_links.add(href)
        if href is not None and len(href) > 20 and "https://cm2023.obss.io" == href[:22]:
            if href not in visited:
                new_links.add(href)
                index = link.get_attribute("x-data-index")
                value = link.get_attribute("x-data-value")
                arr = (index, value)
                if index != None and value != None and arr not in answer:
                    answer.append(arr)
                    print(arr)

# getThem(initial)
a = ['https://cm2023.obss.io/2165506a-18f1-4322-a260-bd8b6dc2240e/blog?lang=EN', 'https://twitter.com/keepmeintouchio', 'mailto:kisiselveri@obss.com.tr', 'https://www.linkedin.com/company/keepmeintouch', 'https://cm2023.obss.io/2165506a-18f1-4322-a260-bd8b6dc2240e/privacy?lang=EN', 'https://obss.com.tr/', None, 'https://cm2023.obss.io/2165506a-18f1-4322-a260-bd8b6dc2240e?lang=EN#', 'https://cm2023.obss.io/2165506a-18f1-4322-a260-bd8b6dc2240e?lang=EN', 'https://www.facebook.com/keepmeintouchio/', 'https://cm2023.obss.io/2165506a-18f1-4322-a260-bd8b6dc2240e/aboutus?lang=EN', 'https://cm2023.obss.io/2165506a-18f1-4322-a260-bd8b6dc2240e/features?lang=EN', 'https://cm2023.obss.io/2165506a-18f1-4322-a260-bd8b6dc2240e?lang=EN#trailer', 'https://cm2023.obss.io/2165506a-18f1-4322-a260-bd8b6dc2240e?lang=EN#explore', 'https://cm2023.obss.io/2165506a-18f1-4322-a260-bd8b6dc2240e/faq?lang=EN', 'https://www.instagram.com/keepmeintouchio/', 'https://www.resmigazete.gov.tr/eskiler/2018/03/20180310-6.htm', 'https://cm2023.obss.io/2165506a-18f1-4322-a260-bd8b6dc2240e/eula?lang=EN', 'mailto:contact@keepmeintouch.io']

for i in a:
    getThem(i)
print(all_links)
# for i in range(10):
#     url = new_links.pop()
#     if url not in visited:
#         visited.append(url)
#         getThem(url)
#     all_links.append(url)
        
print(answer)
print(new_links)

# print(new_links)
answer.sort(key=lambda x: x[0])
str = ""
for i in answer:
    str += i[1]
print(str)
driver.close()