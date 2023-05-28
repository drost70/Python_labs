"""
Action Camera

This class represents an action camera.It inherits from the Camera class.
"""


from models.camera import Camera

# pylint: disable=too-many-arguments
class ActionCamera(Camera):
    """
    Class representing an action camera.
    """

    def __init__(self, brand, model, lens, resolution, zoom, waterproof):
        super().__init__(brand, model, lens)
        self.resolution = resolution
        self.zoom = zoom
        self.waterproof = waterproof
        self.data_set = {"4K", "1080p", "720p"}

    def record_video(self):
        """
        Record a video with the action camera.
        """
        print(f"Recording video with Action Camera: {self.brand} {self.model}")

    def take_photo(self):
        """
        Take a photo using the action camera.

        Returns:
            str: A string representing the details of the taken photo.
        """
        return (
            f"Action Camera: {self.brand} {self.model}, Lens: {self.lens}, "
            f"Resolution: {self.resolution}, Zoom: {self.zoom}, Waterproof: {self.waterproof}"
        )
