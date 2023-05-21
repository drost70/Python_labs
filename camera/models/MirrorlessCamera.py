from models.Camera import Camera


class MirrorlessCamera(Camera):
    """
    Class representing a mirrorless camera.
    """

    # pylint: disable=too-many-arguments
    def __init__(self, brand, model, lens, resolution, zoom, memory_card_type):
        super().__init__(brand, model, lens)
        self.resolution = resolution
        self.zoom = zoom
        self.memory_card_type = memory_card_type
        self.photos_count = 0

    def save_photo(self):
        """
        Save a photo taken with the mirrorless camera.
        """
        self.photos_count += 1

    def erase_memory(self):
        """
        Erase the memory of the mirrorless camera.
        """
        self.photos_count = 0

    def change_settings(self, resolution, zoom):
        """
        Change the settings of the mirrorless camera.
        """
        self.resolution = resolution
        self.zoom = zoom

    def take_photo(self):
        return f"Mirrorless Camera: {self.brand} {self.model}, Lens: {self.lens}," \
               f" Resolution: {self.resolution}, Zoom: {self.zoom}," \
               f" Memory Card Type: {self.memory_card_type}, Photos Count: {self.photos_count}"
