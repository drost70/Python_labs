from models.Camera import Camera

# pylint: disable=too-few-public-methods
class FilmCamera(Camera):
    """
    Class representing a film camera.
    """

    # pylint: disable=too-many-arguments
    def __init__(self, brand, model, lens, film_type, film_iso):
        super().__init__(brand, model, lens)
        self.film_type = film_type
        self.film_iso = film_iso

    def take_photo(self):
        """
        Take a photo using the film camera.
        """
        return f"Taking photo with Film Camera: {self.brand} {self.model}, Lens: {self.lens}," \
               f" Film Type: {self.film_type}, Film ISO: {self.film_iso}"
