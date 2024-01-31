import asyncio
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import telegram

driver = webdriver.Chrome()

URL = "https://www.ppomppu.co.kr/zboard/zboard.php?id=ppomppu"

driver.get(url=URL)
driver.implicitly_wait(time_to_wait=10)

titles = driver.find_elements(By.XPATH,"""//*[@id="revolution_main_table"]/tbody/tr/td[3]/table/tbody/tr/td[2]/div/a/font""")
urls = driver.find_elements(By.XPATH,"""//*[@id="revolution_main_table"]/tbody/tr/td[3]/table/tbody/tr/td[2]/div/a""")

for i in range(len(titles)):
    print(titles[i].text)
    print(urls[i].get_attribute('href'))

message = ""

token = "6554981239:AAEbHU0Oj2HhPYqgfixmkC-mQ6opaKrwo3k"
chat_id = "6885683105"


async def main():
    bot = telegram.Bot(token)
    for i in range(len(titles)):
        message = titles[i].text + "\n" + urls[i].get_attribute('href')
        print(message)
        async with bot:
            await bot.send_message(text=message, chat_id=chat_id)


if __name__ == '__main__':
    asyncio.run(main())