def exp_sh():
    import subprocess
    import time
    # Terminate the File Explorer process
    subprocess.call(["taskkill", "/f", "/im", "explorer.exe"])
    
    # Wait for a few seconds
    time.sleep(5)
    
    # Run the File Explorer again
    subprocess.Popen("explorer.exe")
