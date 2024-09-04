from typing import Dict, List
from .basemodel import (
    GenvexNabtoBaseModel,
    GenvexNabtoDatapointKey,
    GenvexNabtoDatapoint,
    GenvexNabtoSetpointKey,
    GenvexNabtoSetpoint,
    GenvexNabtoUnits,
    GenvexNabtoPointConfig,
)


class GenvexNabtoCTS400(GenvexNabtoBaseModel):
    def __init__(self):
        super().__init__()

        self._datapoints = {
            GenvexNabtoDatapointKey.ALARM_1: GenvexNabtoDatapoint(obj=0, address=79, divider=1, offset=0),
            GenvexNabtoDatapointKey.ALARM_2: GenvexNabtoDatapoint(obj=0, address=80, divider=1, offset=0),
            GenvexNabtoDatapointKey.ALARM_3: GenvexNabtoDatapoint(obj=0, address=82, divider=1, offset=0),             
            GenvexNabtoDatapointKey.BYPASS_ACTIVE: GenvexNabtoDatapoint(obj=0, address=23, divider=1, offset=0),
            GenvexNabtoDatapointKey.CO2_LEVEL: GenvexNabtoDatapoint(obj=0, address=47, divider=1, offset=0),
            GenvexNabtoDatapointKey.DEFROST_ACTIVE: GenvexNabtoDatapoint(obj=0, address=91, divider=1, offset=0),
            GenvexNabtoDatapointKey.DEFROST_TIME_AGO: GenvexNabtoDatapoint(obj=0, address=89, divider=1, offset=0),
            GenvexNabtoDatapointKey.FAN_DUTYCYCLE_EXTRACT: GenvexNabtoDatapoint(obj=0, address=24, divider=10, offset=0),
            GenvexNabtoDatapointKey.FAN_DUTYCYCLE_SUPPLY: GenvexNabtoDatapoint(obj=0, address=25, divider=10, offset=0),
            GenvexNabtoDatapointKey.FILTER_REPLACE_TIME_REMAIN: GenvexNabtoDatapoint(obj=0, address=110, divider=1, offset=0),
            GenvexNabtoDatapointKey.HUMIDITY: GenvexNabtoDatapoint(obj=0, address=31, divider=10, offset=0),
            GenvexNabtoDatapointKey.TEMP_EXHAUST: GenvexNabtoDatapoint(obj=0, address=30, divider=10, offset=0),
            GenvexNabtoDatapointKey.TEMP_EXTRACT: GenvexNabtoDatapoint(obj=0, address=29, divider=10, offset=0),
            GenvexNabtoDatapointKey.TEMP_OUTSIDE: GenvexNabtoDatapoint(obj=0, address=27, divider=10, offset=0),
            GenvexNabtoDatapointKey.TEMP_SUPPLY: GenvexNabtoDatapoint(obj=0, address=28, divider=10, offset=0),
            GenvexNabtoDatapointKey.WINTER_MODE_ACTIVE: GenvexNabtoDatapoint(obj=0, address=72, divider=1, offset=0),
        }

        self._setpoints = {
            GenvexNabtoSetpointKey.ENABLE: GenvexNabtoSetpoint(read_obj=0, read_address=70, write_obj=0, write_address=70, divider=1, offset=0, min=0, max=1, step=1),
            GenvexNabtoSetpointKey.FAN_LEVEL: GenvexNabtoSetpoint(read_obj=0, read_address=69, write_obj=0, write_address=69, divider=1, offset=0, min=1, max=4),
            GenvexNabtoSetpointKey.FAN_LEVEL1_EXTRACT_PRESET: GenvexNabtoSetpoint(read_obj=0, read_address=63, write_obj=0, write_address=63, divider=10, offset=0, min=200, max=1000, step=1),
            GenvexNabtoSetpointKey.FAN_LEVEL1_SUPPLY_PRESET: GenvexNabtoSetpoint(read_obj=0, read_address=59, write_obj=0, write_address=59, divider=10, offset=0, min=200, max=1000, step=1),
            GenvexNabtoSetpointKey.FAN_LEVEL2_EXTRACT_PRESET: GenvexNabtoSetpoint(read_obj=0, read_address=64, write_obj=0, write_address=64, divider=10, offset=0, min=200, max=1000, step=1),
            GenvexNabtoSetpointKey.FAN_LEVEL2_SUPPLY_PRESET: GenvexNabtoSetpoint(read_obj=0, read_address=60, write_obj=0, write_address=60, divider=10, offset=0, min=200, max=1000, step=1),
            GenvexNabtoSetpointKey.FAN_LEVEL3_EXTRACT_PRESET: GenvexNabtoSetpoint(read_obj=0, read_address=65, write_obj=0, write_address=65, divider=10, offset=0, min=200, max=1000, step=1),
            GenvexNabtoSetpointKey.FAN_LEVEL3_SUPPLY_PRESET: GenvexNabtoSetpoint(read_obj=0, read_address=61, write_obj=0, write_address=61, divider=10, offset=0, min=200, max=1000, step=1),
            GenvexNabtoSetpointKey.FAN_LEVEL4_EXTRACT_PRESET: GenvexNabtoSetpoint(read_obj=0, read_address=66, write_obj=0, write_address=66, divider=10, offset=0, min=200, max=1000, step=1),
            GenvexNabtoSetpointKey.FAN_LEVEL4_SUPPLY_PRESET: GenvexNabtoSetpoint(read_obj=0, read_address=62, write_obj=0, write_address=62, divider=10, offset=0, min=200, max=1000, step=1),
            GenvexNabtoSetpointKey.FILTER_REPLACE_RESET: GenvexNabtoSetpoint(read_obj=0, read_address=51, write_obj=0, write_address=51, divider=1, offset=0, min=0, max=1),
            GenvexNabtoSetpointKey.TEMP_TARGET: GenvexNabtoSetpoint(read_obj=0, read_address=37, write_obj=0, write_address=37, divider=10, offset=0, min=0, max=300, step=0.5),
        }

        self.setDefaultConfigs()
        
    def getModelType(self):
        return "CTS400"

    def getModelName(self):
        return "CTS 400"

    def getManufacturer(self):
        return "Nilan"
