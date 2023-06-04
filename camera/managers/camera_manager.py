"""
Camera Manager

This class represents a camera manager.
"""

from decorators.decorators import write_dictionary_of_kwargs, exception_writer, logged

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

    @write_dictionary_of_kwargs
    def add_camera(self, camera):
        """
        Add a camera to the camera manager.

        Args:
            camera: The camera object to add.

        Returns:
            None
        """
        self.cameras.append(camera)

    @exception_writer
    def __getitem__(self, index):
        """
        Get a camera from the camera manager at the specified index.

        Args:
            index: The index of the camera to retrieve.

        Returns:
            The camera object at the specified index.
        """
        return self.cameras[index]

    @logged('file')
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

    @logged('file')
    def get_attributes_by_type(self, attribute_type):
        attributes_by_type = {}
        for camera in self.cameras:
            for attribute, value in camera.__dict__.items():
                if isinstance(value, attribute_type):
                    if attribute not in attributes_by_type:
                        attributes_by_type[attribute] = {str(value)}
                    else:
                        attributes_by_type[attribute].add(str(value))

        with open("camera_attributes.txt", "w", encoding="utf-8") as file:
            for attribute, values in attributes_by_type.items():
                file.write(f"{attribute}: ")
                file.write(", ".join(str(value) for value in values))
                file.write("\n")

        return attributes_by_type

    def __len__(self):
        """
        Get the length of the camera manager.

        Returns:
            The number of cameras in the manager.
        """
        return len(self.cameras)

    def __iter__(self):
        """
        Iterate over the cameras in the camera manager.

        Returns:
            An iterator over the cameras.
        """
        return iter(self.cameras)

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
