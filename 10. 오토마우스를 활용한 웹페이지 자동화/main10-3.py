import pyautogui
import pyperclip
import time

pyautogui.moveTo(1315, 234, 0.2)
pyautogui.click()
time.sleep(0.1)

pyperclip.copy("금광2동 날씨")
pyautogui.hotkey("ctrl", "v")
time.sleep(0.3)

pyautogui.write(["enter"])
time.sleep(0.5)

startX = 997
startY = 253
endX = 1655
endY = 657

pyautogui.screenshot(r'금광2동 날씨.png', region=(startX, startY, endX - startX, endY - startY))
