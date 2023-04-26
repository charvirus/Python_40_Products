import pyautogui
import time
import pyperclip

날씨 = ["서울 날씨", "시흥 날씨", "청주 날씨", "부산 날씨", "강원도 날씨", "성남 날씨", "금광2동 날씨"]

addr_x = 1431
addr_y = 64
startX = 997
startY = 253
endX = 1655
endY = 657

for 지역날씨 in 날씨:
    pyautogui.moveTo(addr_x,addr_y)
    time.sleep(0.2)
    pyautogui.click()
    time.sleep(0.9)
    pyautogui.typewrite("www.naver.com",interval=0.1)
    pyautogui.write(["enter"])
    time.sleep(1)

    pyperclip.copy(지역날씨)
    pyautogui.hotkey("ctrl","v")
    time.sleep(0.5)
    pyautogui.write(["enter"])
    time.sleep(1)
    저장경로 = 지역날씨+'.png'
    pyautogui.screenshot(저장경로,region=(startX,startY,endX-startX,endY-startY))