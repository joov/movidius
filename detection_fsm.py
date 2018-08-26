import time


BOUNCE_TIME = 2000  # millisecs


def _current_millis():
    return int(round(time.time() * 1000))


class DetectionFSM(object):
    def __init__(self):
        self.last_detection_time = None

    def update_status(self, detected):
        """It only reports False after not detected for BOUNCE_TIME."""
        now = _current_millis()
        if detected:
            self.last_detection_time = now
            return True
        if (self.last_detection_time is not None and
                now - self.last_detection_time < BOUNCE_TIME):
            return True
        return False
