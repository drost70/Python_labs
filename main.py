from camera import Camera

if __name__ == '__main__':
    cameras = [
        Camera(),
        Camera("", "1920x1080", 3, "SD Card", 100)
    ]

    print(cameras[1].getinstance("Sony", "1280x720", 2, "Micro SD", 50))
    cameras[0].reset_zoom()
    cameras[1].save_photo(10)
    cameras[1].erase_memory(True)
    cameras[1].change_settings("2560x1440", 4)

    for camera in cameras:
        print(camera)
