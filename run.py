import argparse
import cv2
import sys

if sys.version_info.major < 3:
    print('Error: please use python3.')
    sys.exit(1)


_WINDOW_NAME = 'preview'


def backend_factory(backend_index):
    if backend_index == 0:
        return KerasBackend()
    elif backend_index == 1:
        return YoloV2NCS_Backend()


class KerasBackend(object):
    def __init__(self):
        from vendor.keras_yolo3.yolo import YOLO
        self.yolo = YOLO()

    def __del__(self):
        self.yolo.close_session()

    def process_frame(self, frame):
        import numpy as np
        from PIL import Image
        image = Image.fromarray(frame)
        image = self.yolo.detect_image(image)
        return np.asarray(image)


class YoloV2NCS_Backend(object):
    def __init__(self):
        from vendor.YoloV2NCS.detectionExample.ObjectWrapper import ObjectWrapper
        self.wrapper = ObjectWrapper('vendor/YoloV2NCS/graph')

    def process_frame(self, frame):
        from vendor.YoloV2NCS.detectionExample.Visualize import Visualize
        return Visualize(frame, self.wrapper.Detect(frame))


def main(camera_index, backend_index):
    print('Using backend %d' % backend_index)
    backend = backend_factory(backend_index)

    print('Using camera %d' % camera_index)
    cap = cv2.VideoCapture(camera_index)

    while True:
        ret, frame = cap.read()
        if not ret:
            print('Failed to read camera %d' % camera_index)
            break

        cv2.imshow(_WINDOW_NAME, backend.process_frame(frame))

        # Pressing 'q' or ESC.
        key = cv2.waitKey(5) & 0xFF
        if key == ord('q') or key == 27:
            break

    cap.release()  # Close camera.
    cv2.destroyAllWindows()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Show camera preview")
    parser.add_argument('-c', '--camera', dest='camera_index', default='0',
                        help='camera index')
    parser.add_argument('-b', '--backend', dest='backend_index', default='0',
                        help='backend index')
    args = parser.parse_args()
    main(int(args.camera_index), int(args.backend_index))
