from six.moves import configparser
import six

if six.PY2:
    ConfigParser = configparser.SafeConfigParser
else:
    ConfigParser = configparser.ConfigParser


class Config:

    def __init__(self):
        _config = ConfigParser()
        self._bh1750 = _config['BH1750']
        self._dht11 = _config['dht11']
        self._statsd = _config['statsd']

    def get_bus(self):
        int(self._bh1750.get('bus', 1))

    def get_device(self):
        int(self._bh1750.get('device', 0x23))

    def get_mode(self):
        int(self._bh1750.get('mode', 0x20))

    def get_pin(self):
        int(self._dht11.get('pin', 4))

    def get_hostname(self):
        self._statsd.get('hostname', 'localhost')

    def get_port(self):
        int(self._statsd.get('port', 8125))

    def get_prefix(self):
        self._statsd.get('prefix', 'christmas_tree')
