"""
Mirrorless Camera Module

This module defines the MirrorlessCamera class, which represents a mirrorless camera.
"""

# pylint: disable=too-many-arguments
from models.camera import Camera
from decorators.decorators import logged

class MirrorlessCamera(Camera):
    """
    Class representing a mirrorless camera.
    """
    def __init__(self, brand, model, lens, resolution, zoom, memory_card_type):
        super().__init__(brand, model, lens)
        self.resolution = int(resolution)
        self.zoom = int(zoom)
        self.memory_card_type = memory_card_type
        self.photos_count = 0
        self.data_set = {"RAW", "JPEG"}

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

    @logged("file")
    def take_photo(self):
        photo_details = (
            f"Digital Camera: {self.brand} {self.model}, Lens: {self.lens}, "
            f"Resolution: {self.resolution}, Zoom: {self.zoom}"
        )
        if self.resolution < 0 or self.zoom < 0:
            raise ValueError
        return photo_details
    

    def __str__(self):
        return (
            f"Digital Camera: {self.brand} {self.model}, Lens: {self.lens},"
            f" Resolution: {self.resolution}, Zoom: {self.zoom},"
            f" Memory Card Type: {self.memory_card_type}, Photos Count: {self.photos_count}"
        )
