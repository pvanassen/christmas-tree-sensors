import time
from Sensors.DHT_11 import DHT_11
from Sensors.BH1750 import BH1750
from StatsdSender import StatsdSender
from Config import Config

def main():
    config = Config()
    bh1750 = BH1750(bus=config.get_bus(), device=config.get_device(), mode=config.get_mode())
    dht11 = DHT_11(pin=config.get_pin())
    statsdsender = StatsdSender(host=config.get_hostname(), port=config.get_port(), prefix=config.get_prefix())

    while True:
        luminosity = bh1750.get_luminosity()
        (humidity, temperature) = dht11.read_humidity_temperature()
        statsdsender.send_luminosity(luminosity)
        statsdsender.send_humidity(humidity)
        statsdsender.send_temperature(temperature)
        time.sleep(15)


if __name__ == '__main__':
    main()