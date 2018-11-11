from six.moves import configparser
import six

if six.PY2:
    ConfigParser = configparser.SafeConfigParser
else:
    ConfigParser = configparser.ConfigParser


class Config:

    def __init__(self):
        self._config = ConfigParser()
        self._config.read('config/default.ini')
        self._config.read('config/user.ini')

    def get_bus(self):
        return int(self._config.get('BH1750', 'bus'), 0)

    def get_device(self):
        return int(self._config.get('BH1750', 'device'), 0)

    def get_mode(self):
        return int(self._config.get('BH1750', 'mode'), 0)

    def get_pin(self):
        return int(self._config.get('DHT11', 'pin'), 0)

    def get_hostname(self):
        return self._config.get('STATSD', 'hostname')

    def get_port(self):
        return int(self._config.get('STATSD', 'port'), 0)

    def get_prefix(self):
        return self._config.get('STATSD', 'prefix')
