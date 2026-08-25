import unittest
from common import NilanProxyCTS602, NilanProxyCTS602Light, NilanProxyDatapointKey, NilanProxySetpointKey
from modelTester import modelTester

# slave device models, picked from the quirk tables in cts602.py
NO_QUIRKS = 0
HOTWATER = 12


class CTS602WithNoQuirksTest(modelTester):
    def setUp(self):
        self.loadedModel = NilanProxyCTS602(0, 0, NO_QUIRKS)
        self.expectedName = "CTS 602"
        self.expectedManufacturer = "Nilan"

    def test_quirks_not_loaded(self):
        self.assertNotIn(NilanProxyDatapointKey.TEMP_HOTWATER_TOP, self.loadedModel.datapoints)


class CTS602WithQuirksTest(modelTester):
    def setUp(self):
        self.loadedModel = NilanProxyCTS602(0, 0, HOTWATER)
        self.expectedName = "CTS 602"
        self.expectedManufacturer = "Nilan"

    def test_hotwater_temp_quirk_loaded(self):
        self.assertIn(NilanProxyDatapointKey.TEMP_HOTWATER_TOP, self.loadedModel.datapoints)
        self.assertIn(NilanProxyDatapointKey.TEMP_HOTWATER_BOTTOM, self.loadedModel.datapoints)

    def test_quirk_points_are_configured_and_read(self):
        """A quirk point that never gets a config would silently never be read."""
        for key in (NilanProxyDatapointKey.TEMP_HOTWATER_TOP, NilanProxyDatapointKey.TEMP_HOTWATER_BOTTOM):
            with self.subTest(datapoint=key.value):
                self.assertIn(key, self.loadedModel._configs)
                self.assertIn(key, self.loadedModel.get_datapoints_for_read())


class CTS602QuirkSelectionTest(unittest.TestCase):
    """Quirks are looked up during __init__, so they must be defined before use."""

    def test_all_quirk_devices_load(self):
        quirk_devices = sorted({d for devices in NilanProxyCTS602(0, 0, NO_QUIRKS)._quirks.values() for d in devices})
        self.assertTrue(quirk_devices)
        for device in quirk_devices:
            with self.subTest(slave_device_model=device):
                model = NilanProxyCTS602(0, 0, device)
                self.assertEqual(model.get_model_name(), "CTS 602")

    def test_quirks_only_add_points(self):
        base = NilanProxyCTS602(0, 0, NO_QUIRKS)
        quirked = NilanProxyCTS602(0, 0, HOTWATER)
        self.assertLessEqual(set(base.datapoints), set(quirked.datapoints))
        self.assertLessEqual(set(base.setpoints), set(quirked.setpoints))


class CTS602LightTest(modelTester):
    def setUp(self):
        self.loadedModel = NilanProxyCTS602Light(0, 0, 2)
        self.expectedName = "CTS 602 light"
        self.expectedManufacturer = "Nilan"


if __name__ == '__main__':
    unittest.main()
