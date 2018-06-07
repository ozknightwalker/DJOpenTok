from __future__ import unicode_literals

from unittest import mock

class SignalCatcher:

    def __init__(self, signal):
        self.signal = signal
        self.handler = mock.Mock()

    def __enter__(self):
        self.signal.connect(self.handler)
        return self.handler

    def __exit__(self, *args, **kwargs):
        self.signal.disconnect(self.handler)
