import unittest
from common import (
    NilanProxyBaseModel,
    NilanProxyCTS400,
    NilanProxyOptima270,
)


class modelTester(unittest.TestCase):
    """Checks every model must pass. Subclasses replace loadedModel in setUp."""

    def setUp(self):
        self.loadedModel = NilanProxyBaseModel()
        self.expectedName = "Basemodel"
        self.expectedManufacturer = ""

    # ------------------------------------------------------------------ identity

    def test_correct_name(self):
        self.assertEqual(self.expectedName, self.loadedModel.get_model_name())

    def test_correct_manufacturer(self):
        self.assertEqual(self.expectedManufacturer, self.loadedModel.get_manufacturer())

    # ------------------------------------------------------- point definitions

    def test_datapoints_have_required_fields(self):
        for key, point in self.loadedModel.datapoints.items():
            with self.subTest(datapoint=key.value):
                self.assertIsInstance(point.get('read_address'), int)
                self.assertGreaterEqual(point['read_address'], 0)
                self.assertIsInstance(point.get('signed'), bool)
                self.assertNotEqual(point.get('divider', 1), 0, "a divider of 0 would raise on every read")

    def test_setpoints_have_required_fields(self):
        for key, point in self.loadedModel.setpoints.items():
            with self.subTest(setpoint=key.value):
                self.assertIsInstance(point.get('read_address'), int)
                self.assertGreaterEqual(point['read_address'], 0)
                self.assertIsInstance(point.get('write_address'), int)
                self.assertGreaterEqual(point['write_address'], 0)
                self.assertIsInstance(point.get('signed'), bool)
                self.assertNotEqual(point.get('divider', 1), 0, "a divider of 0 would raise on every read")
                self.assertIsInstance(point.get('min'), int)
                self.assertIsInstance(point.get('max'), int)
                self.assertLessEqual(point['min'], point['max'])
                if 'step' in point:
                    self.assertGreater(point['step'], 0)

    def test_datapoint_addresses_are_unique(self):
        """Two datapoints reading the same register is almost always a copy/paste slip."""
        seen = {}
        for key, point in self.loadedModel.datapoints.items():
            address = (point.get('read_obj', 0), point['read_address'])
            self.assertNotIn(address, seen, f"{key.value} reads the same register as {seen.get(address)}")
            seen[address] = key.value

    # ------------------------------------------------------------- read lists

    def test_datapoint_request_is_list(self):
        self.assertIsInstance(self.loadedModel.get_datapoints_for_read(), list)

    def test_valid_datapoint_request(self):
        for key in self.loadedModel.get_datapoints_for_read():
            self.assertIn(key, self.loadedModel.datapoints)

    def test_setpoint_request_is_list(self):
        self.assertIsInstance(self.loadedModel.get_setpoints_for_read(), list)

    def test_valid_setpoint_request(self):
        for key in self.loadedModel.get_setpoints_for_read():
            self.assertIn(key, self.loadedModel.setpoints)

    # --------------------------------------------------------------- configs

    def test_every_point_has_a_config(self):
        """A point without a config is never requested and reports no unit."""
        for key in self.loadedModel.datapoints:
            with self.subTest(datapoint=key.value):
                self.assertIn(key, self.loadedModel._configs)
        for key in self.loadedModel.setpoints:
            with self.subTest(setpoint=key.value):
                self.assertIn(key, self.loadedModel._configs)

    def test_no_config_for_points_the_model_lacks(self):
        """Configuring a point the model does not have means it came from somewhere else."""
        for key in self.loadedModel._configs:
            with self.subTest(point=key.value):
                self.assertTrue(
                    key in self.loadedModel.datapoints or key in self.loadedModel.setpoints,
                    f"{key.value} is configured but is not a point on this model",
                )

    def test_readable_points_are_requested(self):
        readable_datapoints = self.loadedModel.get_datapoints_for_read()
        readable_setpoints = self.loadedModel.get_setpoints_for_read()
        for key, config in self.loadedModel._configs.items():
            if not config.get('read', False):
                continue
            with self.subTest(point=key.value):
                if key in self.loadedModel.datapoints:
                    self.assertIn(key, readable_datapoints)
                if key in self.loadedModel.setpoints:
                    self.assertIn(key, readable_setpoints)

    # -------------------------------------------------------------- isolation

    def test_loading_another_model_does_not_change_this_one(self):
        """Models must not share state. One model used to overwrite another's configs."""
        keys = list(self.loadedModel.datapoints) + list(self.loadedModel.setpoints)
        before_points = (dict(self.loadedModel.datapoints), dict(self.loadedModel.setpoints))
        before_units = {key: self.loadedModel.get_unit_of_measure(key) for key in keys}
        before_read = (self.loadedModel.get_datapoints_for_read(), self.loadedModel.get_setpoints_for_read())

        NilanProxyOptima270(0, 0, 0)
        NilanProxyCTS400(0, 0, 0)

        self.assertEqual(before_points, (dict(self.loadedModel.datapoints), dict(self.loadedModel.setpoints)))
        self.assertEqual(before_units, {key: self.loadedModel.get_unit_of_measure(key) for key in keys})
        self.assertEqual(before_read, (self.loadedModel.get_datapoints_for_read(), self.loadedModel.get_setpoints_for_read()))
