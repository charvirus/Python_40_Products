#!/usr/bin/env python
# coding: utf-8

# In[25]:


from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

URL='https://www.google.co.kr/imghp'
driver.get(url=URL)

driver.implicitly_wait(time_to_wait=10)


# In[33]:


from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

elem = driver.find_element(By.XPATH,"""//*[@id="APjFqb"]""")
elem.send_keys("바다")
elem.send_keys(Keys.RETURN)


# In[38]:


import time
elem = driver.find_element(By.TAG_NAME,"body")
for i in range(60):
    elem.send_keys(Keys.PAGE_DOWN)
    time.sleep(0.1)
    
try:
    driver.find_element(By.XPATH,"""//*[@id="islmp"]/div/div/div/div/div[1]/div[2]/div[2]/input""").click()

    for i in range(60):
        elem.send_keys(Keys.PAGE_DOWN)
        time.sleep(0.1)
except:
    pass


# In[58]:


links =[]
images = driver.find_elements(By.CSS_SELECTOR,"#islrg > div.islrc > div > a.FRuiCf.islib.nfEiy > div.fR600b.islir > img")

imagess = driver.find_elements(By.CSS_SELECTOR,"#islrg > div.islrc > div > div > a.FRuiCf.islib.nfEiy > div.fR600b.islir > img")


for image in images:
    if image.get_attribute('src') is not None:
        links.append(image.get_attribute('src'))

for image in imagess:
    if image.get_attribute('src') is not None:
        links.append(image.get_attribute('src'))

print('찾은 이미지 개수 : ',len(links))


# In[51]:


import urllib.request

for k,i in enumerate(links):
    url = i
    urllib.request.urlretrieve(url,"C:\\Users\\jbran\\PycharmProjects\\Python_40_Products\\19. 구글 이미지 크롤링\\images download\\"+str(k)+".jpg")

print("다운로드 완료")

