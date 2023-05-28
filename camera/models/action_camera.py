"""
Action Camera

This class represents an action camera.It inherits from the Camera class.
"""

from models.camera import Camera

class ActionCamera(Camera):
    """
    Class representing an action camera.
    """

    # pylint: disable=too-many-arguments
    def __init__(self, brand, model, lens, resolution, zoom, water_resistant):
        super().__init__(brand, model, lens)
        self.resolution = resolution
        self.zoom = zoom
        self.water_resistant = water_resistant

    def change_settings(self, resolution, zoom):
        """
        Change the settings of the action camera.
        """
        self.resolution = resolution
        self.zoom = zoom

    def take_photo(self):
        """
        Take a photo using the action camera.

        Returns:
        str: A string representing the details of the taken photo.
        """
        return f"Action Camera: {self.brand} {self.model}, Lens: {self.lens}, " \
               f"Resolution: {self.resolution}, Zoom: {self.zoom}, " \
               f"Water Resistant: {self.water_resistant}"

