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
        int(self._config.get('BH1750', 'bus'))

    def get_device(self):
        int(self._config.get('BH1750', 'device'))

    def get_mode(self):
        int(self._config.get('BH1750', 'mode'))

    def get_pin(self):
        int(self._config.get('DHT11', 'pin'))

    def get_hostname(self):
        self._config.get('STATSD', 'hostname')

    def get_port(self):
        int(self._config.get('STATSD', 'port'))

    def get_prefix(self):
        self._config.get('STATSD', 'prefix')
