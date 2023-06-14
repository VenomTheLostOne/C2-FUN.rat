def vol_cc():
    from ctypes import cast, POINTER
    from comtypes import CLSCTX_ALL
    from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
    
    # Get the default audio device
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    
    # Create an instance of the audio endpoint volume interface
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    
    # Get the current volume range
    volume_range = volume.GetVolumeRange()
    min_volume = volume_range[0]
    max_volume = volume_range[1]
    
    # Set the volume level (between 0.0 and 1.0)
    new_volume = 0.01 # Example: set the volume to 50%
    volume.SetMasterVolumeLevelScalar(new_volume, None)
    