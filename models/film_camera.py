"""
Film Camera Module

This module defines the FilmCamera class, which represents a film camera.
"""

from models.camera import Camera

# pylint: disable=too-many-arguments
# pylint: disable=too-few-public-methods
class FilmCamera(Camera):
    """
    Class representing a film camera.
    """

    def __init__(self, brand, model, lens, film_type, film_iso):
        super().__init__(brand, model, lens)
        self.film_type = film_type
        self.film_iso = film_iso
        self.data_set = {"35mm", "120mm", "4x5"}

    def take_photo(self):
        """
        Take a photo using the film camera.

        Returns:
            str: A string representing the details of the taken photo.
        """
        return (
            f"Taking photo with Film Camera: {self.brand} {self.model}, Lens: {self.lens},"
            f" Film Type: {self.film_type}, Film ISO: {self.film_iso}"
        )

    def __str__(self):
        """
        Return a string representation of the film camera.

        Returns:
            str: A string representation of the film camera.
        """
        return (
            f"Film Camera: {self.brand} {self.model}, Lens: {self.lens},"
            f" Film Type: {self.film_type}, Film ISO: {self.film_iso}"
        )
