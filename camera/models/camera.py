"""
Camera Module

This module defines the Camera abstract base class and its subclasses for diferent types of cameras.
"""

from abc import ABC, abstractmethod
# pylint: disable=too-few-public-methods
class Camera(ABC):
    """
    Abstract base class representing a camera.
    """

    def __init__(self, brand, model, lens):
        """
        Initialize a Camera object.

        Args:
            brand (str): The brand of the camera.
            model (str): The model of the camera.
            lens (str): The lens of the camera.
        """
        self.brand = brand
        self.model = model
        self.lens = lens

    @abstractmethod
    def take_photo(self):
        """
        Abstract method to take a photo.

        This method must be implemented by subclasses.
        """
      
