import pyautogui
import time

# Sleep for 5 seconds to allow me to open book
time.sleep(5)

# Range can be changed depending on the number of pages
for i in range(10):

    # Turn Page
    pyautogui.keyDown('right')
    pyautogui.keyUp('right')

    # Take and save a screenshot
    pyautogui.screenshot('images/page_%d.pdf' % i)
    time.sleep(0.05)
