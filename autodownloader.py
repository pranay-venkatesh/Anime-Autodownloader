# gogoanime anime downloader for a full season
import pyautogui
import time



def download():
    time.sleep(5)
    pyautogui.moveTo(238, 711)
    pyautogui.click()
    time.sleep(5)
    pyautogui.moveTo(516, 475)
    pyautogui.click()
    time.sleep(5)
    pyautogui.hotkey('ctrl', 'w')
    time.sleep(5)
    pyautogui.moveTo(516, 475)
    pyautogui.click()
    time.sleep(25)
    pyautogui.hotkey('ctrl', 'w')
    time.sleep(5)
    pyautogui.press('pagedown')
    pyautogui.moveTo(800,635)
    pyautogui.click()
    
for i in range (25):  # 25 episodes is the length of an average anime season
    download()
