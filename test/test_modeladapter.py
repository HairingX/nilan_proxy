import unittest
from common import NilanProxyDatapointKey, NilanProxySetpointKey
from nilan_proxy.nilan_proxy_modeladapter import NilanProxyModelAdapter

# model, device_number, slave_device_number, slave_device_model -> expected model name
SUPPORTED_DEVICES = [
    ((2010, 79265, 0, 0), "Optima 270"),
    ((2020, 79280, 0, 0), "Optima 314"),
    ((1040, 0, 70810, 26), "Optima 260"),
    ((1040, 0, 79250, 9), "Optima 312"),
    ((1040, 0, 79250, 8), "Optima 251"),
    ((1040, 0, 79250, 5), "Optima 301"),
    ((1040, 0, 79250, 1), "Optima 250"),
    ((1140, 0, 72270, 1), "CTS 400"),
    ((1141, 0, 72270, 1), "CTS 400"),
    ((1140, 0, 2763306, 2), "CTS 602 light"),
    ((1140, 0, 2763306, 12), "CTS 602"),
    ((1141, 0, 2763306, 0), "CTS 602"),
]

CTS400 = (1140, 0, 72270, 1)


def build_datapoint_payload(values):
    """Payload as the device sends it: 2 byte count, then one 16 bit register each."""
    return len(values).to_bytes(2, 'big') + b''.join(v.to_bytes(2, 'big') for v in values)


def build_setpoint_payload(values):
    """Setpoint payloads carry a leading byte before the count."""
    return b'\x00' + len(values).to_bytes(2, 'big') + b''.join(v.to_bytes(2, 'big') for v in values)


class SupportedDeviceTest(unittest.TestCase):
    def test_every_supported_device_loads(self):
        """Loading must not raise. A model that raises here is silently swallowed by the
        receive thread, and the user only sees a setup timeout."""
        for args, expected_name in SUPPORTED_DEVICES:
            with self.subTest(device=args):
                self.assertTrue(NilanProxyModelAdapter.provides_model(*args))
                self.assertEqual(NilanProxyModelAdapter(*args).get_model_name(), expected_name)

    def test_unknown_device_is_rejected(self):
        self.assertFalse(NilanProxyModelAdapter.provides_model(9999, 0, 0, 0))
        with self.assertRaises(Exception):
            NilanProxyModelAdapter(9999, 0, 0, 0)

    def test_adapters_do_not_share_values(self):
        first = NilanProxyModelAdapter(*CTS400)
        second = NilanProxyModelAdapter(1040, 0, 79250, 1)
        first.parse_datapoint_response(100, build_datapoint_payload([1] * len(first._current_datapoint_list[100])))
        for key in second._current_datapoint_list[100]:
            self.assertIsNone(second.get_value(key), f"{key.value} leaked from another adapter")


class DatapointDecodingTest(unittest.TestCase):
    def setUp(self):
        self.adapter = NilanProxyModelAdapter(*CTS400)
        self.keys = self.adapter._current_datapoint_list[100]

    def payload_with(self, raw_by_key):
        values = [raw_by_key.get(key, 0) for key in self.keys]
        return build_datapoint_payload(values)

    def test_request_order_matches_decoding_order(self):
        """The response is decoded by position, so the request must be built from the
        same list in the same order or every value lands on the wrong key."""
        points = self.adapter.getDatapointRequestList(100)
        self.assertEqual(len(points), len(self.keys))
        for point, key in zip(points, self.keys):
            self.assertIs(point, self.adapter._loaded_model.datapoints[key])

    def test_divider_is_applied(self):
        self.adapter.parse_datapoint_response(100, self.payload_with({NilanProxyDatapointKey.HUMIDITY: 445}))
        self.assertEqual(self.adapter.get_value(NilanProxyDatapointKey.HUMIDITY), 44.5)

    def test_signed_values_decode_negative(self):
        self.adapter.parse_datapoint_response(100, self.payload_with({NilanProxyDatapointKey.TEMP_OUTSIDE: 0x10000 - 50}))
        self.assertEqual(self.adapter.get_value(NilanProxyDatapointKey.TEMP_OUTSIDE), -5.0)

    def test_unsigned_values_do_not_decode_negative(self):
        self.adapter.parse_datapoint_response(100, self.payload_with({NilanProxyDatapointKey.CO2_LEVEL: 0xFFFF}))
        self.assertEqual(self.adapter.get_value(NilanProxyDatapointKey.CO2_LEVEL), 0xFFFF)

    def test_average_humidity_decodes_from_its_own_register(self):
        """humidity and humidity_average are separate registers and must not shadow
        each other. A zero here means the register is zero, not that decoding failed."""
        self.assertIn(NilanProxyDatapointKey.HUMIDITY_AVG, self.keys)
        self.adapter.parse_datapoint_response(100, self.payload_with({
            NilanProxyDatapointKey.HUMIDITY: 445,
            NilanProxyDatapointKey.HUMIDITY_AVG: 512,
        }))
        self.assertEqual(self.adapter.get_value(NilanProxyDatapointKey.HUMIDITY), 44.5)
        self.assertEqual(self.adapter.get_value(NilanProxyDatapointKey.HUMIDITY_AVG), 51.2)

    def test_read_modifier_is_applied(self):
        """filter_ok flips the raw register value."""
        self.adapter.parse_datapoint_response(100, self.payload_with({NilanProxyDatapointKey.FILTER_OK: 1}))
        self.assertEqual(self.adapter.get_value(NilanProxyDatapointKey.FILTER_OK), 0)
        self.adapter.parse_datapoint_response(100, self.payload_with({NilanProxyDatapointKey.FILTER_OK: 0}))
        self.assertEqual(self.adapter.get_value(NilanProxyDatapointKey.FILTER_OK), 1)

    def test_short_response_leaves_later_points_untouched(self):
        """A truncated response must not shift the remaining values onto wrong keys."""
        self.adapter.parse_datapoint_response(100, build_datapoint_payload([7]))
        self.assertIsNone(self.adapter.get_value(self.keys[1]))

    def test_unknown_sequence_is_ignored(self):
        self.adapter.parse_datapoint_response(999, self.payload_with({NilanProxyDatapointKey.HUMIDITY: 445}))
        self.assertIsNone(self.adapter.get_value(NilanProxyDatapointKey.HUMIDITY))


class UpdateHandlerTest(unittest.TestCase):
    def setUp(self):
        self.adapter = NilanProxyModelAdapter(*CTS400)
        self.keys = self.adapter._current_datapoint_list[100]
        self.seen = []
        self.adapter.register_update_handler(NilanProxyDatapointKey.HUMIDITY, lambda old, new: self.seen.append((old, new)))

    def payload_with(self, raw_by_key):
        return build_datapoint_payload([raw_by_key.get(key, 0) for key in self.keys])

    def test_handler_fires_on_change(self):
        self.adapter.parse_datapoint_response(100, self.payload_with({NilanProxyDatapointKey.HUMIDITY: 445}))
        self.assertEqual(self.seen, [(-1, 44.5)])

    def test_handler_does_not_fire_when_value_is_unchanged(self):
        payload = self.payload_with({NilanProxyDatapointKey.HUMIDITY: 445})
        self.adapter.parse_datapoint_response(100, payload)
        self.adapter.parse_datapoint_response(100, payload)
        self.assertEqual(len(self.seen), 1)

    def test_deregistered_handler_stops_firing(self):
        handler = self.adapter._update_handlers[NilanProxyDatapointKey.HUMIDITY][0]
        self.adapter.deregister_update_handler(NilanProxyDatapointKey.HUMIDITY, handler)
        self.adapter.parse_datapoint_response(100, self.payload_with({NilanProxyDatapointKey.HUMIDITY: 445}))
        self.assertEqual(self.seen, [])


class SetpointTest(unittest.TestCase):
    def setUp(self):
        self.adapter = NilanProxyModelAdapter(*CTS400)
        self.keys = self.adapter._current_setpoint_list[200]

    def test_setpoint_response_decodes(self):
        key = NilanProxySetpointKey.TEMP_TARGET
        self.assertIn(key, self.keys)
        point = self.adapter.get_setpoint(key)
        divider = self.adapter.get_point_divider(point)
        values = [0] * len(self.keys)
        values[self.keys.index(key)] = 21 * divider
        self.adapter.parse_setpoint_response(200, build_setpoint_payload(values))
        self.assertEqual(self.adapter.get_value(key), 21)

    def test_min_and_max_are_converted_like_values(self):
        for key in self.keys:
            with self.subTest(setpoint=key.value):
                self.assertLessEqual(self.adapter.get_min_value(key), self.adapter.get_max_value(key))

    def test_write_conversion_round_trips(self):
        for key in self.keys:
            point = self.adapter.get_setpoint(key)
            if self.adapter.get_point_read_modifier(point) is not None:
                continue  # modifiers are lossy by design, eg hours to days
            with self.subTest(setpoint=key.value):
                raw = self.adapter.get_point_min(point)
                value = self.adapter.parse_from_modbus_value(point, raw)
                self.assertEqual(self.adapter.parseToModbusValue(point, value), raw)


if __name__ == '__main__':
    unittest.main()
