import argparse
import cv2
import numpy as np
from vendor.keras_yolo3.yolo import YOLO
from PIL import Image

_WINDOW_NAME = 'preview'


def process_frame(yolo, frame):
    image = Image.fromarray(frame)
    image = yolo.detect_image(image)
    return np.asarray(image)


def main(camera_index):
    print('Opening camera %d' % camera_index)
    cap = cv2.VideoCapture(camera_index)
    yolo = YOLO()

    while True:
        ret, frame = cap.read()
        if not ret:
            print('Failed to read camera %d' % camera_index)
            break

        cv2.imshow(_WINDOW_NAME, process_frame(yolo, frame))

        # Pressing 'q' or ESC.
        key = cv2.waitKey(5) & 0xFF
        if key == ord('q') or key == 27:
            break
        # This check can detect window closing, but it only works for Qt, not Gtk+.
        # if cv2.getWindowProperty(_WINDOW_NAME, cv2.WND_PROP_VISIBLE) < 1:
        #     break

    cap.release()  # Close camera.
    yolo.close_session()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Show camera preview")
    parser.add_argument('-c', '--camera', dest='camera_index', default='0',
                        help='camera index')
    args = parser.parse_args()
    main(int(args.camera_index))
