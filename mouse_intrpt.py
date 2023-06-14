def interupt():
    import pyautogui
    import time
    # Disable fail-safe feature
    pyautogui.FAILSAFE = False
    
    # Call the pyautogui function to move the mouse cursor to a corner of the screen
    def hide_mouse_cursor():
        width, height = pyautogui.size()
        pyautogui.moveTo(width, height, duration=0)
    
    # Hide the mouse cursor
    hide_mouse_cursor()
    
    # Wait for a few seconds
    time.sleep(5)
    
    # Move the mouse cursor back to the center of the screen to show it
    pyautogui.moveTo(pyautogui.size().width / 2, pyautogui.size().height / 2, duration=0)
