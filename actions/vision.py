from pyscreeze import screenshot
import pyautogui

def capture_screen():
    screenshot = pyautogui.screenshot()
    path = screenshot.png
    screenshot.save(path)
    return path