class Camera:
    __instance = None

    def __init__(self, model=None, resolution=None, zoom=0, memory_card_type=None, photos_count=0):
        """
        Parameters:
        - model (str): The name of the camera model.
        - resolution (str): The maximum resolution of the camera.
        - zoom (int): The current optical zoom of the camera.
        - memory_card_type (str): The type of memory card used by the camera.
        - photos_count (int): The number of photos stored in the camera memory.
        """
        self.model = model
        self.resolution = resolution
        self.zoom = zoom
        self.memory_card_type = memory_card_type
        self.photos_count = photos_count

    def __str__(self):
        return f'Model: {self.model}, Resolution: {self.resolution}, Zoom: {self.zoom}, ' \
               f'Memory Card Type: {self.memory_card_type}, Photos Count: {self.photos_count}'

    @staticmethod
    def getinstance(model, resolution, zoom, memory_card_type, photos_count):
        """
        Get a singleton instance of the Camera class.
        If an instance does not exist, create a new instance with the provided arguments.

        Returns:
        - instance: The Camera instance.
        """
        if not Camera.__instance:
            Camera.__instance = Camera(model, resolution, zoom, memory_card_type, photos_count)
        return Camera.__instance

    def reset_zoom(self):
        """
        Reset the zoom level of the camera to 1.
        """
        self.zoom = 1
        if self.zoom == 1:
            print("Zoom level has been reset to 1.")
        else:
            print("Failed to reset zoom level.")

    def save_photo(self, value):
        """
        Save a photo to the camera's memory.
        """
        self.photos_count += value

    def erase_memory(self, memory_cleared):
        """
        Erase the photos from the camera's memory.
        """
        if memory_cleared:
            print("All photos have been erased from memory.")
        else:
            print("Failed to erase photos from memory.")

    def change_settings(self, resolution, zoom):
        """
        Change the camera's settings.
        """
        if resolution and resolution.strip():
            print(f"Resolution successfully changed to {resolution}")
            self.resolution = resolution
        else:
            print("Failed to change resolution!")
        if 1 > zoom or zoom > 5:
            print("Failed to change optical zoom!")
        else:
            self.zoom = zoom
            print(f"Optical zoom successfully changed to {zoom}")

