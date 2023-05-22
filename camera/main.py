"""
Camera Management System

This module demonstrates the functionality of a camera management system.
"""

from managers.camera_manager import CameraManager
from models.action_camera import ActionCamera
from models.digital_сamera import DigitalCamera
from models.film_camera import FilmCamera
from models.mirrorless_camera import MirrorlessCamera



def main():
    """
    Main function to test the camera functionality.
    """
    manager = CameraManager()

    digital_camera_1 = DigitalCamera("Nikon", "D750", "24-70mm", "24MP", "5x", "SD")
    digital_camera_2 = DigitalCamera("Canon", "EOS 5D Mark IV", "24-105mm", "30MP", "4.3x", "CF")

    film_camera_1 = FilmCamera("Nikon", "F6", "50mm", "35mm", "200")
    film_camera_2 = FilmCamera("Leica", "M6", "35mm", "35mm", "400")

    mirrorless_camera_1 = MirrorlessCamera("Sony", "A7 III", "24-70mm", "24MP", "3x", "SD")
    mirrorless_camera_2 = MirrorlessCamera("Fujifilm", "X-T3", "18-55mm", "26MP", "3x", "SD")

    action_camera_1 = ActionCamera("GoPro", "Hero 9", "Wide Angle", "12MP", "4x", True)
    action_camera_2 = ActionCamera("DJI", "Osmo Action", "Wide Angle", "12MP", "4x", True)

    manager.add_camera(digital_camera_1)
    manager.add_camera(digital_camera_2)
    manager.add_camera(film_camera_1)
    manager.add_camera(film_camera_2)
    manager.add_camera(mirrorless_camera_1)
    manager.add_camera(mirrorless_camera_2)
    manager.add_camera(action_camera_1)
    manager.add_camera(action_camera_2)

    print("Cameras with resolution 24MP:")
    cameras_with_resolution_24mp = manager.find_cameras_with_resolution("24MP")
    for camera in cameras_with_resolution_24mp:
        print(camera.take_photo())

    print("\nWater-resistant cameras:")
    water_resistant_cameras = manager.find_water_resistant_cameras()
    for camera in water_resistant_cameras:
        print(camera.take_photo())


if __name__ == "__main__":
    main()

