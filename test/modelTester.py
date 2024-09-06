from common import GenvexNabtoBaseModel, GenvexNabtoSetpointKey, GenvexNabtoDatapointKey
import sys
import unittest
import logging
logging.basicConfig( stream=sys.stderr )
logging.getLogger( "SomeTest.testSomething" ).setLevel( logging.DEBUG )
class modelTester(unittest.TestCase):

    def setUp(self):
        self.loadedModel = GenvexNabtoBaseModel()
        self.expectedName = "Basemodel"
        self.expectedManufacturer = ""

    def test_correct_name(self):
        self.assertEqual(self.expectedName, self.loadedModel.get_model_name())

    def test_correct_manufacturer(self):
        self.assertEqual(self.expectedManufacturer, self.loadedModel.get_manufacturer())    
    
    def test_valid_setpoint_keys(self):
        for key in self.loadedModel.setpoints:            
            currentSetpoint = self.loadedModel.setpoints[key]    
            self.assertIsNotNone(currentSetpoint["read_obj"])
            self.assertIsNotNone(currentSetpoint['read_address'])
            self.assertIsNotNone(currentSetpoint["write_obj"])
            self.assertIsNotNone(currentSetpoint['write_address'])
            self.assertIsNotNone(currentSetpoint['divider'])
            self.assertIsNotNone(currentSetpoint['min'])
            self.assertIsNotNone(currentSetpoint['max'])

            self.assertNotEqual(currentSetpoint['divider'], 0)
        
    def test_valid_datapoint_keys(self):
        for key in self.loadedModel.datapoints:
            currentDatapoint = self.loadedModel.datapoints[key]
            self.assertIsNotNone(currentDatapoint['obj'])
            self.assertIsNotNone(currentDatapoint['address'])
            self.assertIsNotNone(currentDatapoint['divider'])
            self.assertIsNotNone(currentDatapoint['offset'])

            self.assertNotEqual(currentDatapoint['divider'], 0)
        
    def test_datapoint_request_is_list(self):
        self.assertIsInstance(self.loadedModel.get_datapoints_for_read(), list)

    def test_valid_datapoint_request(self):
        datapointRequest = self.loadedModel.get_datapoints_for_read()
        for key in datapointRequest:
            self.assertIn(key, self.loadedModel.datapoints)

    def test_setpoint_request_is_list(self):
        self.assertIsInstance(self.loadedModel.get_setpoints_for_read(), list)

    def test_valid_setpoint_request(self):
        setpointRequest = self.loadedModel.get_setpoints_for_read()
        for key in setpointRequest:
            self.assertIn(key, self.loadedModel.setpoints)