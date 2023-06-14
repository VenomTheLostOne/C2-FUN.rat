def taskmaneger_sh():
    import subprocess
    import time
    # Open Task Manager
    subprocess.Popen('taskmgr.exe')
    
    # Wait for a few seconds
    time.sleep(5)
    
    # Close Task Manager
    subprocess.call('taskkill /IM taskmgr.exe /F')
