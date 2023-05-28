# pylint: disable=missing-module-docstring
# pylint: disable=line-too-long
class SetManager:
    """
    The SetManager class is a wrapper class that provides additional functionality
    for managing a collection of cameras. It is designed to work with an existing
    regular_manager object that represents a collection of cameras.
    """

    def __init__(self, regular_manager):
        """
        Initialize a SetManager object.

        Args:
            regular_manager (CameraManager): The regular_manager object representing a collection of cameras.
        """
        self.regular_manager = regular_manager
        self.current_camera_index = 0
        self.current_set = None
        self.current_set_index = 0

    def __iter__(self):
        """
        Iterate over the sets of cameras in the regular_manager.

        Returns:
            iter: An iterator over the sets of cameras.
        """
        self.current_camera_index = 0
        self.current_set_index = 0
        self.current_set = self._get_next_set()
        return self

    def __len__(self):
        """
        Get the total number of elements in all the sets of cameras.

        Returns:
            int: The total number of elements in all the sets of cameras.
        """
        return sum(len(camera_set) for camera_set in self.regular_manager)

    def __getitem__(self, index):
        """
        Get the camera object at the specified index.

        Args:
            index (int): The index of the camera to retrieve.

        Returns:
            object: The camera object at the specified index.

        Raises:
            IndexError: If the index is out of range.
        """
        if index >= len(self):
            raise IndexError("SetManager index out of range")

        current_index = 0
        for camera_set in self.regular_manager:
            if current_index + len(camera_set) > index:
                set_index = index - current_index
                return list(camera_set)[set_index]

            current_index += len(camera_set)

        return None

    def __next__(self):
        """
        Get the next camera object in the iteration.

        Returns:
            object: The next camera object.

        Raises:
            StopIteration: If there are no more camera objects to iterate over.
        """
        if self.current_set is None:
            raise StopIteration

        camera = self.current_set[self.current_camera_index]
        self.current_camera_index += 1

        if self.current_camera_index >= len(self.current_set):
            self.current_set = self._get_next_set()
            self.current_camera_index = 0

        return camera

    def _get_next_set(self):
        """
        Get the next set of cameras from the regular_manager.

        Returns:
            set: The next set of cameras.

        Raises:
            StopIteration: If there are no more sets of cameras.
        """
        if self.current_set_index >= len(self.regular_manager):
            raise StopIteration

        camera_set = self.regular_manager[self.current_set_index]
        self.current_set_index += 1
        return camera_set
      
