from typing import Dict, List
from .basemodel import ( GenvexNabtoBaseModel, GenvexNabtoDatapointKey, GenvexNabtoDatapoint, GenvexNabtoSetpointKey, GenvexNabtoSetpoint )

class GenvexNabtoOptima301(GenvexNabtoBaseModel):
    def __init__(self):
        super().__init__()

        self._datapoints = {
            GenvexNabtoDatapointKey.TEMP_SUPPLY: GenvexNabtoDatapoint(obj=0, address=0, divider=10, offset=-300), #T1
            GenvexNabtoDatapointKey.TEMP_OUTSIDE: GenvexNabtoDatapoint(obj=0, address=2, divider=10, offset=-300), #T3
            GenvexNabtoDatapointKey.TEMP_EXHAUST: GenvexNabtoDatapoint(obj=0, address=3, divider=10, offset=-300), #T4
            GenvexNabtoDatapointKey.TEMP_EXTRACT: GenvexNabtoDatapoint(obj=0, address=6, divider=10, offset=-300), #T7
            GenvexNabtoDatapointKey.HUMIDITY: GenvexNabtoDatapoint(obj=0, address=10, divider=1, offset=0),
            GenvexNabtoDatapointKey.FAN_DUTYCYCLE_SUPPLY: GenvexNabtoDatapoint(obj=0, address=102, divider=1, offset=0),
            GenvexNabtoDatapointKey.FAN_DUTYCYCLE_EXTRACT: GenvexNabtoDatapoint(obj=0, address=103, divider=1, offset=0),
            GenvexNabtoDatapointKey.FAN_RPM_SUPPLY: GenvexNabtoDatapoint(obj=0, address=108, divider=1, offset=0),
            GenvexNabtoDatapointKey.FAN_RPM_EXTRACT: GenvexNabtoDatapoint(obj=0, address=109, divider=1, offset=0),
            GenvexNabtoDatapointKey.BYPASS_ACTIVE: GenvexNabtoDatapoint(obj=0, address=104, divider=1, offset=0)
        }

        self._setpoints = {
            GenvexNabtoSetpointKey.FAN_LEVEL: GenvexNabtoSetpoint(read_obj=0, read_address=100, write_obj=0, write_address=100, divider=1, offset=0, min=0, max=4),
            GenvexNabtoSetpointKey.TEMP_TARGET: GenvexNabtoSetpoint(read_obj=0, read_address=0, write_obj=0, write_address=0, divider=10, offset=100, min=0, max=200, step=0.5),         
            GenvexNabtoSetpointKey.FILTER_REPLACE_RESET: GenvexNabtoSetpoint(read_obj=0, read_address=105, write_obj=0, write_address=105, divider=1, offset=0, min=0, max=1),
            GenvexNabtoSetpointKey.PREHEATING_ENABLE: GenvexNabtoSetpoint(read_obj=0, read_address=20, write_obj=0, write_address=20, divider=1, offset=0, min=0, max=1),         
            GenvexNabtoSetpointKey.FAN_LEVEL1_SUPPLY_PRESET: GenvexNabtoSetpoint(read_obj=0, read_address=6, write_obj=0, write_address=6, divider=1, offset=0, min=0, max=100, step=1),
            GenvexNabtoSetpointKey.FAN_LEVEL2_SUPPLY_PRESET: GenvexNabtoSetpoint(read_obj=0, read_address=7, write_obj=0, write_address=7, divider=1, offset=0, min=0, max=100, step=1),
            GenvexNabtoSetpointKey.FAN_LEVEL3_SUPPLY_PRESET: GenvexNabtoSetpoint(read_obj=0, read_address=8, write_obj=0, write_address=8, divider=1, offset=0, min=0, max=100, step=1),
            GenvexNabtoSetpointKey.FAN_LEVEL1_EXTRACT_PRESET: GenvexNabtoSetpoint(read_obj=0, read_address=9, write_obj=0, write_address=9, divider=1, offset=0, min=0, max=100, step=1),
            GenvexNabtoSetpointKey.FAN_LEVEL2_EXTRACT_PRESET: GenvexNabtoSetpoint(read_obj=0, read_address=10, write_obj=0, write_address=10, divider=1, offset=0, min=0, max=100, step=1),
            GenvexNabtoSetpointKey.FAN_LEVEL3_EXTRACT_PRESET: GenvexNabtoSetpoint(read_obj=0, read_address=11, write_obj=0, write_address=11, divider=1, offset=0, min=0, max=100, step=1),
            GenvexNabtoSetpointKey.COOLING_ENABLE: GenvexNabtoSetpoint(read_obj=0, read_address=2, write_obj=0, write_address=2, divider=1, offset=0, min=0, max=1),
            GenvexNabtoSetpointKey.TEMP_COOLING_START_OFFSET: GenvexNabtoSetpoint(read_obj=0, read_address=1, write_obj=0, write_address=1, divider=10, offset=0, min=30, max=100, step=0.1),
        }

    def getModelName(self):
        return "Optima 301"
    
    def getManufacturer(self):
        return "Genvex"

    def getDefaultDatapointRequest(self) -> List[GenvexNabtoDatapointKey]:
        return [
            GenvexNabtoDatapointKey.TEMP_SUPPLY,
            GenvexNabtoDatapointKey.TEMP_OUTSIDE,
            GenvexNabtoDatapointKey.TEMP_EXHAUST,
            GenvexNabtoDatapointKey.TEMP_EXTRACT,
            GenvexNabtoDatapointKey.HUMIDITY,
            GenvexNabtoDatapointKey.FAN_DUTYCYCLE_SUPPLY,
            GenvexNabtoDatapointKey.FAN_DUTYCYCLE_EXTRACT,
            GenvexNabtoDatapointKey.FAN_RPM_SUPPLY,            
            GenvexNabtoDatapointKey.FAN_RPM_EXTRACT,
            GenvexNabtoDatapointKey.BYPASS_ACTIVE
        ]
    
    def getDefaultSetpointRequest(self) -> List[GenvexNabtoSetpointKey]:
        return [
            GenvexNabtoSetpointKey.FAN_LEVEL,
            GenvexNabtoSetpointKey.TEMP_TARGET,
            GenvexNabtoSetpointKey.PREHEATING_ENABLE,
            GenvexNabtoSetpointKey.FAN_LEVEL1_SUPPLY_PRESET,
            GenvexNabtoSetpointKey.FAN_LEVEL2_SUPPLY_PRESET,
            GenvexNabtoSetpointKey.FAN_LEVEL3_SUPPLY_PRESET,
            GenvexNabtoSetpointKey.FAN_LEVEL1_EXTRACT_PRESET,
            GenvexNabtoSetpointKey.FAN_LEVEL2_EXTRACT_PRESET,
            GenvexNabtoSetpointKey.FAN_LEVEL3_EXTRACT_PRESET,
            GenvexNabtoSetpointKey.COOLING_ENABLE,
            GenvexNabtoSetpointKey.TEMP_COOLING_START_OFFSET
        ]