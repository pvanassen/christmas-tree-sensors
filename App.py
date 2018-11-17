import time
from app.sensors import BH1750
from app.sensors import DHT_11
from app.statsdsender import StatsdSender
from app.config import Config


def main():

    _config = Config()
    _bh1750 = BH1750(bus=_config.get_bus(), device=_config.get_device(), mode=_config.get_mode())
    _dht11 = DHT_11(pin=_config.get_pin())
    _statsdsender = StatsdSender(host=_config.get_hostname(), port=_config.get_port(), prefix=_config.get_prefix())
    print("Sending stats to %s:%s with prefix %s" % (_config.get_hostname(), _config.get_port(), _config.get_prefix()))

    while True:
        luminosity = _bh1750.get_luminosity()
        (humidity, temperature) = _dht11.read_humidity_temperature()
        _statsdsender.send_luminosity(luminosity)
        _statsdsender.send_humidity(humidity)
        _statsdsender.send_temperature(temperature)
        time.sleep(5)


if __name__ == '__main__':
    main()
