import pyautogui
import time
import pyperclip

pyautogui.moveTo(1241,256,0.2)
pyautogui.click()
time.sleep(0.5)

pyautogui.write("a")
pyautogui.hotkey("ctrl","a")
pyperclip.copy("서울 날씨")
pyautogui.hotkey("ctrl","v")
time.sleep(0.5)

pyautogui.write(["enter"])
time.sleep(1)