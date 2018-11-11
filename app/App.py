import time
import sensors
from statsdsender import StatsdSender
from config import Config

def main():
    config = Config()
    bh1750 = sensors.BH1750(bus=config.get_bus(), device=config.get_device(), mode=config.get_mode())
    dht11 = sensors.DHT_11(pin=config.get_pin())
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