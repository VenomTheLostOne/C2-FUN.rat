def blackwall():
    import requests
    import ctypes
    from PIL import Image
    from io import BytesIO
    
    def set_wallpaper_from_url(image_url):
        response = requests.get(image_url)
        image = Image.open(BytesIO(response.content))
    
        # Convert the image to BMP format in memory
        image_path = 'wallpaper.bmp'
        image.save(image_path, 'BMP')
    
        # Set the wallpaper
        ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)
    
    # Specify the URL of the image you want to set as the wallpaper
    image_url = "https://i.ibb.co/xsnRczw/images.jpg"
    
    # Call the set_wallpaper_from_url function with the image URL
    set_wallpaper_from_url(image_url)
    