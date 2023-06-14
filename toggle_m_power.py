def toggle_m():
    import ctypes
    import time
    HWND_BROADCAST = 0xFFFF
    WM_SYSCOMMAND = 0x0112
    SC_MONITORPOWER = 0xF170
    MONITOR_OFF = 2
    MONITOR_ON = -1
    def set_monitor_power(on):
        hwnd = ctypes.windll.user32.GetForegroundWindow()
        ctypes.windll.user32.PostMessageW(hwnd, WM_SYSCOMMAND, SC_MONITORPOWER, MONITOR_ON if on else MONITOR_OFF)
    def block_input_events(block):
        user32 = ctypes.windll.user32
        user32.BlockInput(block)
    set_monitor_power(False)
    block_input_events(True)
    time.sleep(10)
    block_input_events(False)
    set_monitor_power(True)

