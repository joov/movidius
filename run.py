import argparse
import cv2
import sys

from camera import camera_factory

if sys.version_info.major < 3:
    print('Error: please use python3.')
    sys.exit(1)


_WINDOW_NAME = 'preview'


def backend_factory(backend_id):
    print('Using backend %r' % backend_id)
    backend_index = int(backend_id)
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


def main(camera_id, backend_id):
    backend = backend_factory(backend_id)
    camera = camera_factory(camera_id)
    camera.open()

    while True:
        ret, frame = camera.read()
        if not ret:
            break

        cv2.imshow(_WINDOW_NAME, backend.process_frame(frame))

        # Pressing 'q' or ESC.
        key = cv2.waitKey(5) & 0xFF
        if key == ord('q') or key == 27:
            break

    camera.close()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Show camera preview")
    parser.add_argument('-c', '--camera', dest='camera_id', default='0',
                        help='camera id')
    parser.add_argument('-b', '--backend', dest='backend_id', default='0',
                        help='backend id')
    args = parser.parse_args()
    main(args.camera_id, args.backend_id)
