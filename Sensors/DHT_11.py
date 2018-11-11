# -*- coding: utf-8 -*-
import Adafruit_DHT


class DHT_11:

    def __init__(self, pin):
        self._sensor = Adafruit_DHT.DHT11
        self._pin = pin

    def read_humidity_temperature(self):
        Adafruit_DHT.read_retry(self._sensor, self._pin)
