import statsd


class StatsdSender:

    def __init__(self, host, port, prefix):
        self._statsdclient = statsd.StatsClient(host=host, port=port, prefix=prefix)

    def send_temperature(self, temperature):
        self._statsdclient.gauge('temperature', temperature)

    def send_humidity(self, humidity):
        self._statsdclient.gauge('humidity', humidity)

    def send_luminosity(self, luminosity):
        self._statsdclient.gauge('luminosity', luminosity)
