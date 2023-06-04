"""
Camera Module
This module defines the Camera abstract base class and its subclasses for diferent types of cameras.
"""
from abc import ABC, abstractmethod

class Camera(ABC):
  """
  Abstract base class representing a camera.
  Attributes:
  brand (str): The brand of the camera.
  model (str): The model of the camera.
  lens (str): The lens of the camera.
  data_set (set): A set to store a specific dataset.
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
      self.data_set = set()
      
    @abstractmethod
    def take_photo(self):
        """
        Abstract method to take a photo.
        This method must be implemented by subclasses.
        """
    def __iter__(self):
      """
      Iterate over the data_set.
      Returns:
      iter: An iterator over the data_set.
      """
      return iter(self.data_set)
    
    def all_values_with_type(self, type_of_value):
        return {k: v for k, v in self.__dict__.items() if type(v) == type_of_value}
