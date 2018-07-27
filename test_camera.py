import argparse
import cv2


def main(camera_index):

    print('Opening camera %d' % camera_index)
    cap = cv2.VideoCapture(camera_index)

    while True:
        ret, frame = cap.read()
        if not ret:
            print('Failed to read camera')
            break
        cv2.imshow('preview', frame)
        if cv2.waitKey(5) & 0xFF == ord('q'):
            break
        if cv2.getWindowProperty('preview', cv2.WND_PROP_VISIBLE) < 1:
            break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Show camera preview")
    parser.add_argument('-c', '--camera', dest='camera_index', default='0',
                        help='camera index')
    args = parser.parse_args()
    main(int(args.camera_index))
