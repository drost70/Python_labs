class Camera:
    def __init__(self, model, resolution, zoom, memoryCardType, photosCount):
        """
            Parameters:
            model (str): The name of the camera model.
            resolution (str): The maximum resolution of the camera.
            zoom (int): The current optical zoom of the camera.
            memoryCardType (str): The type of memory card used by the camera.
            photosCount (int): The number of photos stored in the camera memory.
        """
        self.model = model
        self.resolution = resolution
        self.zoom = zoom
        self.memoryCardType = memoryCardType
        self.photosCount = photosCount

    def reset_zoom(self):
        self.zoom = 1
        if self.zoom == 1:
            print("Zoom level has been reset to 1.")
        else:
            print("Failed to reset zoom level.")

    def save_photo(self, value):
        self.photos_count += value

    def erase_memory(self, memory_cleared):
        if memory_cleared:
            print("All photos have been erased from memory.")
        else:
            print("Failed to erase photos from memory.")

    def change_settings(self, resolution, zoom):
        if resolution and resolution.strip():
            print(f"Resolution successfully changed to {resolution}")
            self.resolution = resolution
        else:
            print("Failed to change resolution!")
        if 1 <= zoom <= 5:
            self.zoom = zoom
            print(f"Optical zoom successfully changed to {zoom}")
        else:
            print("Failed to change optical zoom!")

    def __str__(self):
        return f'Model: {self.model}, Resolution: {self.resolution}, Zoom: {self.zoom}, ' \
               f'Memory Card Type: {self.memoryCardType}, Photos Count: {self.photosCount}'

