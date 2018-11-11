# -*- coding: utf-8 -*-
import smbus


class BH1750:

    def __init__(self, bus, device, mode):
        self._bus = smbus.SMBus(bus)
        self._device = device
        self._mode = mode

    @staticmethod
    def _convert_to_number(data):
        result = (data[1] + (256 * data[0])) / 1.2
        return result

    def get_luminosity(self):
        data = self._bus.read_i2c_block_data(self._device, self._mode)
        return self._convert_to_number(data)

