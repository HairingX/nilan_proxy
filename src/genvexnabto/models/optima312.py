from typing import Dict, List
from .basemodel import ( GenvexNabtoBaseModel, GenvexNabtoDatapointKey, GenvexNabtoDatapoint, GenvexNabtoSetpointKey, GenvexNabtoSetpoint, GenvexNabtoUnits )

class GenvexNabtoOptima312(GenvexNabtoBaseModel):
    def __init__(self):
        super().__init__()

        self._datapoints = {
            GenvexNabtoDatapointKey.BYPASS_ACTIVE: GenvexNabtoDatapoint(obj=0, address=104, divider=1, offset=0, signed=False),
            GenvexNabtoDatapointKey.FAN_DUTYCYCLE_EXTRACT: GenvexNabtoDatapoint(obj=0, address=103, divider=1, offset=0, signed=False),
            GenvexNabtoDatapointKey.FAN_DUTYCYCLE_SUPPLY: GenvexNabtoDatapoint(obj=0, address=102, divider=1, offset=0, signed=False),
            GenvexNabtoDatapointKey.FAN_RPM_EXTRACT: GenvexNabtoDatapoint(obj=0, address=109, divider=1, offset=0, signed=False),
            GenvexNabtoDatapointKey.FAN_RPM_SUPPLY: GenvexNabtoDatapoint(obj=0, address=108, divider=1, offset=0, signed=False),
            GenvexNabtoDatapointKey.HUMIDITY: GenvexNabtoDatapoint(obj=0, address=10, divider=1, offset=0, signed=False),
            GenvexNabtoDatapointKey.TEMP_EXHAUST: GenvexNabtoDatapoint(obj=0, address=3, divider=10, offset=-300, signed=True), #T4
            GenvexNabtoDatapointKey.TEMP_EXTRACT: GenvexNabtoDatapoint(obj=0, address=6, divider=10, offset=-300, signed=True), #T7
            GenvexNabtoDatapointKey.TEMP_OUTSIDE: GenvexNabtoDatapoint(obj=0, address=2, divider=10, offset=-300, signed=True), #T3
            GenvexNabtoDatapointKey.TEMP_SUPPLY: GenvexNabtoDatapoint(obj=0, address=0, divider=10, offset=-300, signed=True), #T1
        }

        self._setpoints = {
            GenvexNabtoSetpointKey.FAN_LEVEL: GenvexNabtoSetpoint(read_obj=0, read_address=100, write_obj=0, write_address=100, divider=1, offset=0, min=0, max=4, signed=False),
            GenvexNabtoSetpointKey.FAN_LEVEL1_EXTRACT_PRESET: GenvexNabtoSetpoint(read_obj=0, read_address=9, write_obj=0, write_address=9, divider=1, offset=0, min=0, max=100, signed=False),
            GenvexNabtoSetpointKey.FAN_LEVEL1_SUPPLY_PRESET: GenvexNabtoSetpoint(read_obj=0, read_address=6, write_obj=0, write_address=6, divider=1, offset=0, min=0, max=100, signed=False),
            GenvexNabtoSetpointKey.FAN_LEVEL2_EXTRACT_PRESET: GenvexNabtoSetpoint(read_obj=0, read_address=10, write_obj=0, write_address=10, divider=1, offset=0, min=0, max=100, signed=False),
            GenvexNabtoSetpointKey.FAN_LEVEL2_SUPPLY_PRESET: GenvexNabtoSetpoint(read_obj=0, read_address=7, write_obj=0, write_address=7, divider=1, offset=0, min=0, max=100, signed=False),
            GenvexNabtoSetpointKey.FAN_LEVEL3_EXTRACT_PRESET: GenvexNabtoSetpoint(read_obj=0, read_address=11, write_obj=0, write_address=11, divider=1, offset=0, min=0, max=100, signed=False),
            GenvexNabtoSetpointKey.FAN_LEVEL3_SUPPLY_PRESET: GenvexNabtoSetpoint(read_obj=0, read_address=8, write_obj=0, write_address=8, divider=1, offset=0, min=0, max=100, signed=False),
            GenvexNabtoSetpointKey.FILTER_REPLACE_RESET: GenvexNabtoSetpoint(read_obj=0, read_address=105, write_obj=0, write_address=105, divider=1, offset=0, min=0, max=1, signed=False),          
            GenvexNabtoSetpointKey.REHEAT_ENABLE: GenvexNabtoSetpoint(read_obj=0, read_address=21, write_obj=0, write_address=21, divider=1, offset=0, min=0, max=1, signed=False),
            GenvexNabtoSetpointKey.TEMP_HOTWATER: GenvexNabtoSetpoint(read_obj=0, read_address=1, write_obj=0, write_address=1, divider=10, offset=0, min=0, max=550, signed=True),
            GenvexNabtoSetpointKey.TEMP_TARGET: GenvexNabtoSetpoint(read_obj=0, read_address=0, write_obj=0, write_address=0, divider=10, offset=100, min=0, max=200, step=5, signed=True),         
        }
      
        self.setDefaultConfigs()
        self._configs[GenvexNabtoSetpointKey.FILTER_REPLACE_INTERVAL]["unit_of_measurement"] = GenvexNabtoUnits.MONTHS
        

    def getModelName(self):
        return "Optima 312"
    
    def getManufacturer(self):
        return "Genvex"