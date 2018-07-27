import argparse
import cv2

_WINDOW_NAME = 'preview'


def main(camera_index):
    print('Opening camera %d' % camera_index)
    cap = cv2.VideoCapture(camera_index)

    while True:
        ret, frame = cap.read()
        if not ret:
            print('Failed to read camera %d' % camera_index)
            break

        # Display the resulting frame
        cv2.imshow(_WINDOW_NAME, frame)
        # Pressing 'q' or ESC.
        key = cv2.waitKey(5) & 0xFF
        if key == ord('q') or key == 27:
            break
        # User closed window.
        if cv2.getWindowProperty(_WINDOW_NAME, cv2.WND_PROP_VISIBLE) < 1:
            break

    cap.release()  # Close camera.
    cv2.destroyAllWindows()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Show camera preview")
    parser.add_argument('-c', '--camera', dest='camera_index', default='0',
                        help='camera index')
    args = parser.parse_args()
    main(int(args.camera_index))
