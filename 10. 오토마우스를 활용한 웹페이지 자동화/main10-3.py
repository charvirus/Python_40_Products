import pyautogui
import pyperclip
import time

name = "금광2동 날씨"

pyautogui.moveTo(1315, 234, 0.2)
pyautogui.click()
time.sleep(0.1)

pyautogui.write("a")
pyautogui.hotkey("ctrl","a")
pyperclip.copy(name)
pyautogui.hotkey("ctrl", "v")
time.sleep(0.3)

pyautogui.write(["enter"])
time.sleep(1)

startX = 997
startY = 253
endX = 1655
endY = 657

pyautogui.screenshot(name+'.png', region=(startX, startY, endX - startX, endY - startY))
