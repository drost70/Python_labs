"""
Camera Management System

This module demonstrates the functionality of a camera management system.
"""
# pylint: disable=line-too-long
# pylint: disable=too-many-locals

from models.digital_сamera import DigitalCamera
from models.mirrorless_camera import MirrorlessCamera
from models.film_camera import FilmCamera
from models.action_camera import ActionCamera
from managers.camera_manager import CameraManager


def main():
    """
    Main function to test the camera functionality.
    """
    camera1 = DigitalCamera("Canon", "EOS R", "24-105mm", "20MP", "4x", "SD")
    camera2 = MirrorlessCamera("Sony", "A7 III", "24-70mm", "24MP", "3x", "SD")
    camera3 = FilmCamera("Nikon", "F6", "50mm", "35mm", "400")
    camera4 = ActionCamera("GoPro", "HERO9", "Wide", "12MP", "2x", True)

    manager = CameraManager()

    manager.add_camera(camera1)
    manager.add_camera(camera2)
    manager.add_camera(camera3)
    manager.add_camera(camera4)

    for camera in manager:
        photo_details = camera.take_photo()
        print(photo_details)

    digital_camera = manager[0]
    digital_camera.save_photo()

    action_camera = manager[3]
    action_camera.record_video()

    num_cameras = len(manager)
    print("Number of cameras:", num_cameras)

    cameras_with_indices = manager.get_camera_with_index()
    for index, camera in cameras_with_indices:
        print("Camera index:", index)
        print(camera.model)

    cameras_with_results = manager.get_camera_with_action_result(lambda camera: camera.zoom if hasattr(camera, 'zoom') else None)
    for camera, result in cameras_with_results:
        if not isinstance(camera, FilmCamera):
            print(camera.model)
            print("Zoom value:", result)

    digital_camera_attributes = manager.get_attributes_by_type(str)
    print("Digital camera attributes:")
    print(digital_camera_attributes)

    def resolution_condition(camera):
        return camera.resolution == "24MP"

    resolution_check = manager.check_conditions(resolution_condition)
    print("Resolution condition check:")
    print("All cameras:", resolution_check['all'])
    print("Any camera:", resolution_check['any'])


if __name__ == "__main__":
    main()
