from models.ActionCamera import ActionCamera
from models.DigitalCamera import DigitalCamera
from models.MirrorlessCamera import MirrorlessCamera


class CameraManager:
    """
    Class representing a camera manager.
    """

    def __init__(self):
        self.cameras = []

    def add_camera(self, camera):
        """
        Add a camera to the camera manager.
        """
        self.cameras.append(camera)

    def find_cameras_with_resolution(self, resolution):
        """
        Find cameras with a specific resolution.
        """
        return list(filter(lambda c: isinstance(c, (DigitalCamera, MirrorlessCamera))
                                     and c.resolution == resolution, self.cameras))

    def find_water_resistant_cameras(self):
        """
        Find water-resistant cameras.
        """
        return list(filter(lambda c: isinstance(c, ActionCamera)
                                     and c.water_resistant, self.cameras))

    def print_cameras(self):
        """
        Print information about all the cameras in the manager.
        """
        for camera in self.cameras:
            print(camera)
