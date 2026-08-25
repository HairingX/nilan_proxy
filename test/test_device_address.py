import unittest
from common import NilanProxy, make_offline_proxy


class DeviceAddressTest(unittest.TestCase):
    """Covers the address handling that made setup fail with socket.gaierror.

    An unset ip in a config entry used to reach set_device as the literal string
    "None", which was stored as a valid address and later handed to socket.sendto
    as a hostname to resolve.
    """

    def test_sanitize_device_ip_accepts_ipv4(self):
        self.assertEqual(NilanProxy.sanitize_device_ip("192.168.1.50"), "192.168.1.50")
        self.assertEqual(NilanProxy.sanitize_device_ip("  192.168.1.50  "), "192.168.1.50")

    def test_sanitize_device_ip_rejects_unusable(self):
        for value in (None, "", "   ", "None", "nilan.local", "999.1.1.1", "192.168.1"):
            with self.subTest(value=value):
                self.assertIsNone(NilanProxy.sanitize_device_ip(value))

    def test_sanitize_device_port_accepts_valid(self):
        self.assertEqual(NilanProxy.sanitize_device_port(5570), 5570)
        self.assertEqual(NilanProxy.sanitize_device_port("5570"), 5570)

    def test_sanitize_device_port_rejects_unusable(self):
        for value in (None, 0, -1, 65536, "", "abc"):
            with self.subTest(value=value):
                self.assertIsNone(NilanProxy.sanitize_device_port(value))


    def test_set_device_ignores_unset_address(self):
        """An unset address must leave the proxy waiting for discovery, not poisoned."""
        proxy = make_offline_proxy()
        proxy.set_device("abcd.remote.lscontrol.dk", "None", 0)
        self.assertIsNone(proxy.get_device_ip())
        self.assertEqual(proxy.get_discovered_devices(), {})

    def test_set_device_keeps_manual_address(self):
        proxy = make_offline_proxy()
        proxy.set_device("abcd.remote.lscontrol.dk", "192.168.1.50", 5570)
        self.assertEqual(proxy.get_device_ip(), "192.168.1.50")
        self.assertEqual(proxy.get_device_port(), 5570)
        self.assertEqual(proxy.get_discovered_devices(), {"abcd.remote.lscontrol.dk": ("192.168.1.50", 5570)})

    def test_connect_without_address_returns_false(self):
        """Must fail cleanly instead of raising socket.gaierror out of setup."""
        proxy = make_offline_proxy()
        proxy.set_device("abcd.remote.lscontrol.dk", None, None)
        # Isolate the address check by satisfying the guards in front of it. Without
        # the check this would reach sendto on this object and raise instead.
        proxy._socket = object()
        proxy._listen_thread_open = True
        self.assertFalse(proxy.connect_to_device())


if __name__ == '__main__':
    unittest.main()
