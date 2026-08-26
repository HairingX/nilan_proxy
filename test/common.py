import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from nilan_proxy import *
from nilan_proxy.models import *


def make_offline_proxy():
    """A proxy with its listen thread stopped and socket closed.

    Tests drive the state machine directly instead of talking to a device, so nothing
    must be listening or broadcasting while they do.
    """
    proxy = NilanProxy()
    proxy.stop_listening()
    if proxy._listen_thread is not None:
        proxy._listen_thread.join(timeout=5)
    proxy.close_socket()
    proxy._discovered_devices = {}
    proxy._device_ip = None
    return proxy
