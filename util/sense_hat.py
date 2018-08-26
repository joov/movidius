import time
from threading import Thread

try:
    from sense_hat import SenseHat
except ImportError:
    print('Raspberry Pi sense_hat is not installed')


class BlinkingThread(object):
    def __init__(self, led_on, led_off):
        self._stop = True
        self._thread = None
        self._led_on = led_on
        self._led_off = led_off

    def start(self):
        if self._thread:
            return
        self._stop = False
        self._thread = Thread(target=self._run)
        self._thread.start()

    def stop(self):
        if not self._thread:
            return
        self._stop = True
        self._thread.join()
        self._thread = None

    def _run(self):
        light = False
        while not self._stop:
            time.sleep(.5)
            if light:
                self._led_off()
            else:
                self._led_on()
            light = not light


class Hat(object):
    def __init__(self):
        self._sense = None
        self._thread = None

    def open(self):
        self._sense = SenseHat()
        self._thread = BlinkingThread(
                lambda: self._sense.clear((255, 0, 255)),
                lambda: self._sense.clear())

    def close(self):
        if self._thread:
            self._thread.stop()
        if self._sense:
            self._sense.clear()

    def update_led(self, detected):
        if not self._sense:
            return

        if detected:
            self._thread.stop()
            self._sense.clear((0, 100, 0))
        else:
            self._thread.start()
