from typing import Dict, List
from .basemodel import ( GenvexNabtoBaseModel, GenvexNabtoDatapointKey, GenvexNabtoDatapoint, GenvexNabtoSetpointKey, GenvexNabtoSetpoint, GenvexNabtoPointConfig, GenvexNabtoUnits )

class GenvexNabtoCTS602(GenvexNabtoBaseModel):
    def __init__(self):
        super().__init__()

        self._datapoints = {
            GenvexNabtoDatapointKey.BYPASS_ACTIVE: GenvexNabtoDatapoint(obj=0, address=187, divider=1, offset=0, signed=False),
            GenvexNabtoDatapointKey.CO2_LEVEL: GenvexNabtoDatapoint(obj=0, address=53, divider=1, offset=0, signed=False),
            GenvexNabtoDatapointKey.FAN_LEVEL_EXTRACT: GenvexNabtoDatapoint(obj=0, address=100, divider=1, offset=0, signed=False),
            GenvexNabtoDatapointKey.FAN_LEVEL_SUPPLY: GenvexNabtoDatapoint(obj=0, address=99, divider=1, offset=0, signed=False),
            GenvexNabtoDatapointKey.FILTER_REPLACE_TIME_REMAIN: GenvexNabtoDatapoint(obj=0, address=102, divider=1, offset=0, signed=False),
            GenvexNabtoDatapointKey.HUMIDITY: GenvexNabtoDatapoint(obj=0, address=52, divider=100, offset=0, signed=False),
            GenvexNabtoDatapointKey.STATE_CODE: GenvexNabtoDatapoint(obj=0, address=86, divider=1, offset=0, signed=False),
            GenvexNabtoDatapointKey.TEMP_CONDENSER: GenvexNabtoDatapoint(obj=0, address=36, divider=100, offset=0, signed=True),
            GenvexNabtoDatapointKey.TEMP_EVAPORATOR: GenvexNabtoDatapoint(obj=0, address=37, divider=100, offset=0, signed=True),
            GenvexNabtoDatapointKey.TEMP_EXTRACT: GenvexNabtoDatapoint(obj=0, address=35, divider=100, offset=0, signed=True),
            GenvexNabtoDatapointKey.TEMP_OUTSIDE: GenvexNabtoDatapoint(obj=0, address=39, divider=100, offset=0, signed=True),
            GenvexNabtoDatapointKey.TEMP_ROOM: GenvexNabtoDatapoint(obj=0, address=41, divider=100, offset=0, signed=True),
            GenvexNabtoDatapointKey.TEMP_SUPPLY: GenvexNabtoDatapoint(obj=0, address=38, divider=100, offset=0, signed=True),
        }

        self._setpoints = {
            GenvexNabtoSetpointKey.FAN_LEVEL: GenvexNabtoSetpoint(read_obj=0, read_address=139, write_obj=0, write_address=139, divider=1, offset=0, min=0, max=4, signed=False),
            GenvexNabtoSetpointKey.FILTER_REPLACE_INTERVAL: GenvexNabtoSetpoint(read_obj=0, read_address=159, write_obj=0, write_address=159, divider=1, offset=0, min=0, max=365, signed=False),
            GenvexNabtoSetpointKey.FILTER_REPLACE_RESET: GenvexNabtoSetpoint(read_obj=0, read_address=71, write_obj=0, write_address=71, divider=1, offset=0, min=0, max=1, signed=False),
            GenvexNabtoSetpointKey.TEMP_TARGET: GenvexNabtoSetpoint(read_obj=0, read_address=140, write_obj=0, write_address=140, divider=100, offset=0, min=0, max=3000, step=5, signed=True),
        }

        self.setDefaultConfigs()

        
        self._quirks = {
            "hotwaterTempSensor": [
                9, 10, 11,  12,  18, 19,
                20, 21, 23,  30,  32, 34,
                38, 43, 44, 144, 244
            ],
            "sacrificialAnode": [
                9, 10,  11,  12, 18, 19,
                20, 21,  23,  30, 34, 38,
                43, 44, 144, 244
            ],
            "reheat": [
                2,   3,   4,  9, 10, 11, 12, 13, 18,
                19,  20,  21, 23, 26, 27, 30, 31, 33,
                34,  35,  36, 38, 39, 40, 41, 43, 44,
                45, 144, 244
            ],
            "exhaustTempSensor": [ 2, 13, 27, 31 ],
            "antiLegionella": [
                3,  4,  9, 10,  11,  12, 18,
                19, 20, 21, 23,  30,  32, 34,
                38, 43, 44, 45, 144, 244
            ],
            "hotwaterTempSet": [
                9, 10, 11,  12,  13, 18, 19,
                20, 21, 23,  30,  31, 32, 34,
                38, 43, 44, 144, 244
            ],
            "summerTemperatures": [
                2,  4,  9, 10, 12, 13, 19,  21,
                26, 30, 31, 32, 33, 34, 35,  36,
                38, 39, 40, 41, 43, 44, 45, 144,
                244
            ],
            "coolingPriority": [
                2,  9, 10, 12, 13,  30,
                31, 32, 38, 43, 44, 144,
                244
            ],
            "coolingOffset": [
                4,  9, 10, 12, 19,  21,  26,
                30, 32, 33, 35, 36,  38,  39,
                40, 41, 43, 44, 45, 144, 244
            ]
        }
        
    
    def addDeviceQuirks(self, deviceNumber, slaveDeviceNumber, slaveDeviceModel):
        # Add quirks unique to the connected device
        if self.deviceHasQuirk("hotwaterTempSensor", slaveDeviceModel):
            self._datapoints[GenvexNabtoDatapointKey.TEMP_HOTWATER_TOP] = GenvexNabtoDatapoint(obj=0, address=42, divider=100, offset=0, signed=True)
            self._datapoints[GenvexNabtoDatapointKey.TEMP_HOTWATER_BOTTOM] = GenvexNabtoDatapoint(obj=0, address=43, divider=100, offset=0, signed=True)

        if self.deviceHasQuirk("sacrificialAnode", slaveDeviceModel):  
            self._datapoints[GenvexNabtoDatapointKey.SACRIFICIAL_ANODE_OK] = GenvexNabtoDatapoint(obj=0, address=142, divider=1, offset=0, signed=False)
            
        if self.deviceHasQuirk("reheat", slaveDeviceModel):  
            self._setpoints[GenvexNabtoSetpointKey.REHEAT_ENABLE] = GenvexNabtoSetpoint(read_obj=0, read_address=281, write_obj=0, write_address=281, divider=1, offset=0, min=0, max=1, signed=False)

        if self.deviceHasQuirk("exhaustTempSensor", slaveDeviceModel):  
            self._datapoints[GenvexNabtoDatapointKey.TEMP_EXHAUST] = GenvexNabtoDatapoint(obj=0, address=34, divider=100, offset=0, signed=True)

        if self.deviceHasQuirk("antiLegionella", slaveDeviceModel):  
            self._setpoints[GenvexNabtoSetpointKey.ANTILEGIONELLA_DAY] = GenvexNabtoSetpoint(read_obj=0, read_address=194, write_obj=0, write_address=194, divider=1, offset=0, min=0, max=7, signed=False)

        if self.deviceHasQuirk("hotwaterTempSet", slaveDeviceModel):  
            self._setpoints[GenvexNabtoSetpointKey.TEMP_HOTWATER] = GenvexNabtoSetpoint(read_obj=0, read_address=190, write_obj=0, write_address=190, divider=100, offset=0, min=2000, max=7000, step=10, signed=True)
            self._setpoints[GenvexNabtoSetpointKey.TEMP_HOTWATER_BOOST] = GenvexNabtoSetpoint(read_obj=0, read_address=189, write_obj=0, write_address=189, divider=100, offset=0, min=2000, max=7000, step=10, signed=True)

        if self.deviceHasQuirk("summerTemperatures", slaveDeviceModel):
            self._setpoints[GenvexNabtoSetpointKey.TEMP_SUMMER_SUPPLY_MIN] = GenvexNabtoSetpoint(read_obj=0, read_address=171, write_obj=0, write_address=171, divider=100, offset=0, min=0, max=4000, step=10, signed=True)
            self._setpoints[GenvexNabtoSetpointKey.TEMP_SUMMER_SUPPLY_MAX] = GenvexNabtoSetpoint(read_obj=0, read_address=173, write_obj=0, write_address=173, divider=100, offset=0, min=0, max=4000, step=10, signed=True)

        if self.deviceHasQuirk("coolingPriority", slaveDeviceModel):
            self._setpoints[GenvexNabtoSetpointKey.COMPRESSOR_PRIORITY] = GenvexNabtoSetpoint(read_obj=0, read_address=191, write_obj=0, write_address=191, divider=1, offset=0, min=0, max=1, signed=False)

        if self.deviceHasQuirk("coolingOffset", slaveDeviceModel):
            self._setpoints[GenvexNabtoSetpointKey.TEMP_COOLING_START_OFFSET] = GenvexNabtoSetpoint(read_obj=0, read_address=170, write_obj=0, write_address=170, divider=1, offset=0, min=0, max=8, signed=True)
        
        self.setDefaultConfigs()
        
        return

    def getModelType(self):
        return "CTS602"
    
    def getModelName(self):
        return "CTS 602"
    
    def getManufacturer(self):
        return "Nilan"
    