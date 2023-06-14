def duck():
    import winsound
    import time
    
    def play_sound(frequency, duration):
        winsound.Beep(frequency, duration)
        time.sleep(0.1)
    
    # Funny sound effects
    def funny_sounds():
        play_sound(523, 250)  # C5 note
        play_sound(659, 500)  # E5 note
        play_sound(587, 250)  # D5 note
        play_sound(523, 500)  # C5 note
        play_sound(349, 500)  # F4 note
        play_sound(392, 500)  # G4 note
        play_sound(523, 1000)  # C5 note (longer duration)
    
    # Call the funny_sounds function
    funny_sounds()
    def play_hacking_sound():
        frequency = 1000  # Frequency of the sound (in Hz)
        duration = 200  # Duration of each sound (in milliseconds)
    
        for _ in range(5):
            winsound.Beep(frequency, duration)
            time.sleep(0.1)
    
            frequency += 200  # Increase frequency for each iteration
    
            # Pause between each set of sounds
            time.sleep(0.2)
    
    # Call the play_hacking_sound function
    play_hacking_sound()
    
    def play_rick_roll():
        # Frequencies for the melody (notes)
        frequencies = [440, 493, 523, 440, 392, 523, 659, 587, 523]
    
        # Durations for each note
        durations = [400, 200, 200, 400, 400, 400, 800, 400, 800]
    
        for frequency, duration in zip(frequencies, durations):
            winsound.Beep(int(frequency), int(duration))
            time.sleep(0.1)
    
    # Call the play_rick_roll function
    play_rick_roll()