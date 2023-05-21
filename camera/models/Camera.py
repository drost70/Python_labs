from abc import ABC, abstractmethod

# pylint: disable=too-few-public-methods
class Camera(ABC):
    """
    Abstract base class representing a camera.
    """
    def __init__(self, brand, model, lens):
        self.brand = brand
        self.model = model
        self.lens = lens

    @abstractmethod
    def take_photo(self):
        pass
      
