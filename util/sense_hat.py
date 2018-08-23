from sense_hat import SenseHat


class Hat(object):
    def __init__(self):
        self._sense = None

    def open(self):
        self._sense = SenseHat()

    def close(self):
        if self._sense:
            self._sense.clear()

    def update_led(self, detected):
        if not self._sense:
            return

        if detected:
            self._sense.clear((0, 100, 0))
        else:
            self._sense.clear((255, 0, 255))
