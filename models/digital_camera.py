"""
Digital Camera Module

This module defines the DigitalCamera class, which represents a digital camera.
"""

from models.camera import Camera

# pylint: disable=line-too-long
# pylint: disable=too-many-arguments
class DigitalCamera(Camera):
    """
    Class representing a digital camera.
    """

    def __init__(self, brand, model, lens, resolution, zoom, memory_card_type):
        super().__init__(brand, model, lens)
        self.resolution = resolution
        self.zoom = zoom
        self.memory_card_type = memory_card_type
        self.photos_count = 0
        self.data_set = {"CCD", "CMOS", "BSI"}

    def save_photo(self):
        """
        Save a photo taken with the digital camera.
        """
        self.photos_count += 1

    def erase_memory(self):
        """
        Erase the memory of the digital camera.
        """
        self.photos_count = 0

    def change_settings(self, resolution, zoom):
        """
        Change the settings of the digital camera.
        """
        self.resolution = resolution
        self.zoom = zoom

    def take_photo(self):
        """
        Take a photo using the digital camera.

        Returns:
            str: A string representing the details of the taken photo.
        """
        return (
            f"Digital Camera: {self.brand} {self.model}, Lens: {self.lens}, "
            f"Resolution: {self.resolution}, Zoom: {self.zoom}, "
            f"Memory Card Type: {self.memory_card_type}, Photos Count: {self.photos_count}"
        )

    def __str__(self):
        return f"Digital Camera: {self.brand} {self.model}, Lens: {self.lens}, Resolution: {self.resolution}, Zoom: {self.zoom}, Memory Card Type: {self.memory_card_type}, Photos Count: {self.photos_count}"
