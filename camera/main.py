from models.digital_сamera import DigitalCamera
from models.mirrorless_camera import MirrorlessCamera
from models.film_camera import FilmCamera
from models.action_camera import ActionCamera
from managers.camera_manager import CameraManager
from managers.set_manager import SetManager

# pylint: disable=line-too-long

if __name__ == "__main__":
    camera_manager = CameraManager()
    digital_camera = DigitalCamera("Canon", "EOS R", "24-105mm", 20, 4, "SD")
    action_camera = ActionCamera("GoPro", "HERO9", "Wide", 12, 2, True)
    film_camera = FilmCamera("Nikon", "F6", "50mm", "35", "400")
    mirrorless_camera = MirrorlessCamera("Sony", "A7 III", "24-70mm", "20", "2", "SD")

    camera_manager.add_camera(action_camera)
    camera_manager.add_camera(film_camera)
    camera_manager.add_camera(mirrorless_camera)
    camera_manager.add_camera(digital_camera)

    print(f"Total number of cameras: {len(camera_manager)}")

    print("\nPrinting camera attributes by type:")
    attributes_by_type = camera_manager.get_attributes_by_type(str)
    for camera_type, attributes in attributes_by_type.items():
        print(f"Camera type: {camera_type}")
        for value in list(attributes):
            print(value)

    print("\nPerforming action for all cameras:")
    camera_manager.perform_action_for_all_cameras(lambda camera: camera.take_photo())

    print("\nGetting camera with index:")
    camera_with_index = camera_manager.get_camera_with_index()
    for index, camera in camera_with_index:
        print(f"Index: {index}, Camera: {camera}")

    print("\nGetting camera with action result:")
    camera_with_action_result = camera_manager.get_camera_with_action_result(lambda camera: camera.take_photo())
    for camera, action_result in camera_with_action_result:
        print(f"Camera: {camera}, Action Result: {action_result}")

    print("\nChecking conditions:")
    conditions = [
        lambda camera: isinstance(camera, (DigitalCamera, MirrorlessCamera)) and camera.memory_card_type == "SD"
    ]
    for condition in conditions:
        result = camera_manager.check_conditions(condition)
        print(f"Condition: {condition.__name__}, All: {result['all']}, Any: {result['any']}")

    print("\nIterating over cameras using SetManager:")
    set_manager = SetManager(camera_manager)
    for camera in set_manager:
        print(camera)
