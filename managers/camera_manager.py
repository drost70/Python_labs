"""
Camera Manager

This class represents a camera manager.
"""

# pylint: disable=line-too-long
class CameraManager:
    """
    Class representing a camera manager.
    """

    def __init__(self):
        """
        Initialize a new instance of the CameraManager class.
        """
        self.cameras = []

    def add_camera(self, camera):
        """
        Add a camera to the camera manager.

        Args:
            camera: The camera object to add.

        Returns:
            None
        """
        self.cameras.append(camera)

    def __len__(self):
        """
        Get the length of the camera manager.

        Returns:
            The number of cameras in the manager.
        """
        return len(self.cameras)

    def __getitem__(self, index):
        """
        Get a camera from the camera manager at the specified index.

        Args:
            index: The index of the camera to retrieve.

        Returns:
            The camera object at the specified index.
        """
        return self.cameras[index]

    def __iter__(self):
        """
        Iterate over the cameras in the camera manager.

        Returns:
            An iterator over the cameras.
        """
        return iter(self.cameras)

    def perform_action_for_all_cameras(self, action):
        """
        Perform a custom action for all cameras in the manager.
        Returns a list of results from the action.

        Args:
            action: The action to perform on each camera.

        Returns:
            A list of results from the action.
        """
        return [action(camera) for camera in self.cameras]

    def get_camera_with_index(self):
        """
        Get a concatenation of the camera and its index in the manager using enumerate.
        Returns a list of tuples (index, camera).

        Returns:
            A list of tuples (index, camera) containing the index and camera object.
        """
        return list(enumerate(self.cameras))

    def get_camera_with_action_result(self, action):
        """
        Get a concatenation of the camera and the result of the specified action using zip.
        Returns a list of tuples (camera, action_result).

        Args:
            action: The action to perform on each camera.

        Returns:
            A list of tuples (camera,action_result) containing the camera object and the result of the action.
        """
        action_results = self.perform_action_for_all_cameras(action)
        return list(zip(self.cameras, action_results))

    def get_attributes_by_type(self, attribute_type):
        """
        Get a dictionary of all attributes and their values for a given attribute type.
        Only attributes with values of the specified type are included.
        Returns a dictionary of attribute names and values.

        Args:
            attribute_type: The type of attribute values to include.

        Returns:
            A dictionary of attribute names and values.
        """
        attributes = {}
        for camera in self.cameras:
            camera_attributes = camera.__dict__
            for attribute, value in camera_attributes.items():
                if isinstance(value, attribute_type):
                    attributes[attribute] = value
        return attributes

    def check_conditions(self, condition):
        """
        Check if all cameras or any camera satisfy a given condition.
        Returns a dictionary with keys 'all' and 'any' containing boolean values.

        Args:
            condition: The condition to check for each camera.

        Returns:
            A dictionary with keys 'all' and 'any' containing boolean values.
        """
        all_condition = all(condition(camera) for camera in self.cameras)
        any_condition = any(condition(camera) for camera in self.cameras)
        return {'all': all_condition, 'any': any_condition}
      
