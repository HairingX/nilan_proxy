from typing import Dict, List
from .basemodel import ( GenvexNabtoBaseModel, GenvexNabtoDatapointKey, GenvexNabtoDatapoint, GenvexNabtoSetpointKey, GenvexNabtoSetpoint, GenvexNabtoUnits )

class GenvexNabtoOptima314(GenvexNabtoBaseModel):
    def __init__(self):
        super().__init__()

        self._datapoints = {
            GenvexNabtoDatapointKey.BYPASS_ACTIVE: GenvexNabtoDatapoint(obj=0, address=12, divider=1, offset=0, signed=False),
            GenvexNabtoDatapointKey.FAN_DUTYCYCLE_EXTRACT: GenvexNabtoDatapoint(obj=0, address=19, divider=100, offset=0, signed=False),
            GenvexNabtoDatapointKey.FAN_DUTYCYCLE_SUPPLY: GenvexNabtoDatapoint(obj=0, address=18, divider=100, offset=0, signed=False),
            GenvexNabtoDatapointKey.FAN_RPM_EXTRACT: GenvexNabtoDatapoint(obj=0, address=36, divider=1, offset=0, signed=False),
            GenvexNabtoDatapointKey.FAN_RPM_SUPPLY: GenvexNabtoDatapoint(obj=0, address=35, divider=1, offset=0, signed=False),
            GenvexNabtoDatapointKey.HUMIDITY: GenvexNabtoDatapoint(obj=0, address=26, divider=1, offset=0, signed=False),
            GenvexNabtoDatapointKey.TEMP_EXHAUST: GenvexNabtoDatapoint(obj=0, address=22, divider=10, offset=-300, signed=True),
            GenvexNabtoDatapointKey.TEMP_EXTRACT: GenvexNabtoDatapoint(obj=0, address=64, divider=10, offset=-300, signed=True),
            GenvexNabtoDatapointKey.TEMP_OUTSIDE: GenvexNabtoDatapoint(obj=0, address=21, divider=10, offset=-300, signed=True),
            GenvexNabtoDatapointKey.TEMP_SUPPLY: GenvexNabtoDatapoint(obj=0, address=20, divider=10, offset=-300, signed=True),
        }

        self._setpoints = {
            GenvexNabtoSetpointKey.BOOST_ENABLE: GenvexNabtoSetpoint(read_obj=0, read_address=30, write_obj=0, write_address=70, divider=1, offset=0, min=0, max=1, signed=False),
            GenvexNabtoSetpointKey.BOOST_TIME: GenvexNabtoSetpoint(read_obj=0, read_address=70, write_obj=0, write_address=150, divider=1, offset=0, min=1, max=120, signed=False),
            GenvexNabtoSetpointKey.FAN_LEVEL: GenvexNabtoSetpoint(read_obj=0, read_address=7, write_obj=0, write_address=24, divider=1, offset=0, min=0, max=4, signed=False),
            GenvexNabtoSetpointKey.FAN_LEVEL1_EXTRACT_PRESET: GenvexNabtoSetpoint(read_obj=0, read_address=13, write_obj=0, write_address=36, divider=1, offset=0, min=0, max=100, signed=False),
            GenvexNabtoSetpointKey.FAN_LEVEL1_SUPPLY_PRESET: GenvexNabtoSetpoint(read_obj=0, read_address=10, write_obj=0, write_address=30, divider=1, offset=0, min=0, max=100, signed=False),
            GenvexNabtoSetpointKey.FAN_LEVEL2_EXTRACT_PRESET: GenvexNabtoSetpoint(read_obj=0, read_address=14, write_obj=0, write_address=38, divider=1, offset=0, min=0, max=100, signed=False),
            GenvexNabtoSetpointKey.FAN_LEVEL2_SUPPLY_PRESET: GenvexNabtoSetpoint(read_obj=0, read_address=11, write_obj=0, write_address=32, divider=1, offset=0, min=0, max=100, signed=False),
            GenvexNabtoSetpointKey.FAN_LEVEL3_EXTRACT_PRESET: GenvexNabtoSetpoint(read_obj=0, read_address=15, write_obj=0, write_address=40, divider=1, offset=0, min=0, max=100, signed=False),
            GenvexNabtoSetpointKey.FAN_LEVEL3_SUPPLY_PRESET: GenvexNabtoSetpoint(read_obj=0, read_address=12, write_obj=0, write_address=34, divider=1, offset=0, min=0, max=100, signed=False),
            GenvexNabtoSetpointKey.FAN_LEVEL4_EXTRACT_PRESET: GenvexNabtoSetpoint(read_obj=0, read_address=9, write_obj=0, write_address=28, divider=1, offset=0, min=0, max=100, signed=False),
            GenvexNabtoSetpointKey.FAN_LEVEL4_SUPPLY_PRESET: GenvexNabtoSetpoint(read_obj=0, read_address=8, write_obj=0, write_address=26, divider=1, offset=0, min=0, max=100, signed=False),
            GenvexNabtoSetpointKey.FILTER_REPLACE_INTERVAL: GenvexNabtoSetpoint(read_obj=0, read_address=100, write_obj=0, write_address=210, divider=1, offset=0, min=0, max=12, signed=False),
            GenvexNabtoSetpointKey.FILTER_REPLACE_RESET: GenvexNabtoSetpoint(read_obj=0, read_address=50, write_obj=0, write_address=110, divider=1, offset=0, min=0, max=1, signed=False),
            GenvexNabtoSetpointKey.HUMIDITY_CONTROL_ENABLE: GenvexNabtoSetpoint(read_obj=0, read_address=6, write_obj=0, write_address=22, divider=1, offset=0, min=0, max=1, signed=False),
            GenvexNabtoSetpointKey.REHEAT_ENABLE: GenvexNabtoSetpoint(read_obj=0, read_address=3, write_obj=0, write_address=16, divider=1, offset=0, min=0, max=1, signed=False),
            GenvexNabtoSetpointKey.TEMP_HOTWATER: GenvexNabtoSetpoint(read_obj=0, read_address=122, write_obj=0, write_address=254, divider=10, offset=0, min=0, max=550, signed=True),
            GenvexNabtoSetpointKey.TEMP_TARGET: GenvexNabtoSetpoint(read_obj=0, read_address=1, write_obj=0, write_address=12, divider=10, offset=100, min=0, max=200, step=5, signed=True),
        }
        
        self.setDefaultConfigs()
        self._configs[GenvexNabtoSetpointKey.FILTER_REPLACE_INTERVAL]["unit_of_measurement"] = GenvexNabtoUnits.MONTHS
        

    def getModelName(self):
        return "Optima 314"
    
    def getManufacturer(self):
        return "Genvex"