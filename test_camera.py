import argparse
import cv2
import sys

from camera import camera_factory

if sys.version_info.major < 3:
    print('Error: please use python3.')
    sys.exit(1)


def main(camera_id):
    camera = camera_factory(camera_id)
    camera.open()

    while True:
        ret, frame = camera.read()
        if not ret:
            break
        cv2.imshow('preview', frame)
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break
        # This check can detect window closing, but it doesn't works reliably on Gtk+.
        # if cv2.getWindowProperty('preview', cv2.WND_PROP_VISIBLE) < 1:
        #    break

    # When everything done, release the capture
    camera.close()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Show camera preview")
    parser.add_argument('-c', '--camera', dest='camera_id', default='0',
                        help='camera id')
    args = parser.parse_args()
    main(args.camera_id)
