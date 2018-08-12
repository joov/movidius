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
