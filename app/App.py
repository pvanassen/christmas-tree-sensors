import time
import sensors
import statsdsender
import config


def main():

    _config = config.Config()
    _bh1750 = sensors.BH1750(bus=_config.get_bus(), device=_config.get_device(), mode=_config.get_mode())
    _dht11 = sensors.DHT_11(pin=_config.get_pin())
    _statsdsender = statsdsender.StatsdSender(host=_config.get_hostname(), port=_config.get_port(), prefix=_config.get_prefix())

    while True:
        luminosity = _bh1750.get_luminosity()
        (humidity, temperature) = _dht11.read_humidity_temperature()
        _statsdsender.send_luminosity(luminosity)
        _statsdsender.send_humidity(humidity)
        _statsdsender.send_temperature(temperature)
        time.sleep(15)


if __name__ == '__main__':
    main()
