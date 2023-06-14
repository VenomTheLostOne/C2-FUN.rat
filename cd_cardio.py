def cd_open_close():
    import ctypes
    import time
    # Call the Windows API function to open or close the CD tray
    def toggle_cd_tray(open):
        ctypes.windll.winmm.mciSendStringW(f"set cdaudio door {'open' if open else 'closed'}", None, 0, None)
    
    # Open the CD tray
    toggle_cd_tray(True)
    
    # Wait for a few seconds
    time.sleep(5)
    
    # Close the CD tray
    toggle_cd_tray(False)
