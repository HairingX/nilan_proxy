import time
import unittest
from common import make_offline_proxy
from nilan_proxy.const import SECONDS_UNTILUNAVAILABLE


class AvailabilityTest(unittest.TestCase):
    """Availability must reflect whether the device actually answers.

    Showing the last known reading as if it were current is worse than showing
    nothing, so this drives the state machine directly and checks both the flag
    and the notification that pushes it out to consumers.
    """

    def setUp(self):
        self.proxy = make_offline_proxy()
        self.seen = []
        self.proxy.register_connection_state_handler(self.seen.append)

    def set_silence(self, seconds):
        """Pretend the last response arrived this many seconds ago."""
        self.proxy._last_response = time.time() - seconds

    def test_starts_unavailable(self):
        self.assertFalse(self.proxy.is_available())

    def test_becomes_available_after_a_response(self):
        self.set_silence(0)
        self.proxy._update_availability()
        self.assertTrue(self.proxy.is_available())
        self.assertEqual(self.seen, [True])

    def test_stays_available_just_below_the_threshold(self):
        self.set_silence(SECONDS_UNTILUNAVAILABLE - 1)
        self.proxy._update_availability()
        self.assertTrue(self.proxy.is_available())

    def test_becomes_unavailable_after_the_threshold(self):
        self.set_silence(0)
        self.proxy._update_availability()
        self.set_silence(SECONDS_UNTILUNAVAILABLE + 1)
        self.proxy._update_availability()
        self.assertFalse(self.proxy.is_available())
        self.assertEqual(self.seen, [True, False])

    def test_recovers_when_the_device_answers_again(self):
        for silence in (0, SECONDS_UNTILUNAVAILABLE + 1, 0):
            self.set_silence(silence)
            self.proxy._update_availability()
        self.assertTrue(self.proxy.is_available())
        self.assertEqual(self.seen, [True, False, True])

    def test_handler_only_fires_on_change(self):
        self.set_silence(0)
        for _ in range(5):
            self.proxy._update_availability()
        self.assertEqual(self.seen, [True])

    def test_deregistered_handler_stops_firing(self):
        self.proxy.deregister_connection_state_handler(self.seen.append)
        self.set_silence(0)
        self.proxy._update_availability()
        self.assertTrue(self.proxy.is_available())
        self.assertEqual(self.seen, [])

    def test_registering_twice_notifies_once(self):
        self.proxy.register_connection_state_handler(self.seen.append)
        self.set_silence(0)
        self.proxy._update_availability()
        self.assertEqual(self.seen, [True])

    def test_a_raising_handler_does_not_stop_the_others(self):
        """The receive thread notifies through these. One bad listener must not
        take the connection down with it."""
        def boom(available):
            raise RuntimeError("handler blew up")
        self.proxy.register_connection_state_handler(boom)
        self.set_silence(0)
        self.proxy._update_availability()
        self.assertEqual(self.seen, [True])
        self.assertTrue(self.proxy.is_available())

    def test_availability_does_not_gate_the_reconnect_logic(self):
        """_is_connected drives polling and reconnecting in the receive thread.
        Going unavailable must leave it alone, or the device never comes back."""
        self.proxy._is_connected = True
        self.set_silence(SECONDS_UNTILUNAVAILABLE + 1)
        self.proxy._update_availability()
        self.assertFalse(self.proxy.is_available())
        self.assertTrue(self.proxy.is_connected())

    def test_handlers_are_not_shared_between_proxies(self):
        other = make_offline_proxy()
        other_seen = []
        other.register_connection_state_handler(other_seen.append)
        self.set_silence(0)
        self.proxy._update_availability()
        self.assertEqual(self.seen, [True])
        self.assertEqual(other_seen, [])


if __name__ == '__main__':
    unittest.main()
