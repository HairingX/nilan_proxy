from .basemodel import ( GenvexNabtoBaseModel, GenvexNabtoDatapointKey, GenvexNabtoDatapoint, GenvexNabtoSetpointKey, GenvexNabtoSetpoint )

class GenvexNabtoCTS602(GenvexNabtoBaseModel):
    def __init__(self, device_number:int, slave_device_number:int, slave_device_model:int):
        super().__init__()

        self._attr_manufacturer="Nilan"
        self._attr_model_name="CTS 602"

        self.datapoints = {
            GenvexNabtoDatapointKey.BYPASS_ACTIVE: GenvexNabtoDatapoint(read_address=187, divider=1, signed=False),
            GenvexNabtoDatapointKey.CO2_LEVEL: GenvexNabtoDatapoint(read_address=53, divider=1, signed=False),
            GenvexNabtoDatapointKey.FAN_LEVEL_EXTRACT: GenvexNabtoDatapoint(read_address=100, divider=1, signed=False),
            GenvexNabtoDatapointKey.FAN_LEVEL_SUPPLY: GenvexNabtoDatapoint(read_address=99, divider=1, signed=False),
            GenvexNabtoDatapointKey.FILTER_REPLACE_TIME_REMAIN: GenvexNabtoDatapoint(read_address=102, divider=1, signed=False),
            GenvexNabtoDatapointKey.HUMIDITY: GenvexNabtoDatapoint(read_address=52, divider=100, signed=False),
            GenvexNabtoDatapointKey.STATE_CODE: GenvexNabtoDatapoint(read_address=86, divider=1, signed=False),
            GenvexNabtoDatapointKey.TEMP_CONDENSER: GenvexNabtoDatapoint(read_address=36, divider=100, signed=True),
            GenvexNabtoDatapointKey.TEMP_EVAPORATOR: GenvexNabtoDatapoint(read_address=37, divider=100, signed=True),
            GenvexNabtoDatapointKey.TEMP_EXTRACT: GenvexNabtoDatapoint(read_address=35, divider=100, signed=True),
            GenvexNabtoDatapointKey.TEMP_OUTSIDE: GenvexNabtoDatapoint(read_address=39, divider=100, signed=True),
            GenvexNabtoDatapointKey.TEMP_ROOM: GenvexNabtoDatapoint(read_address=41, divider=100, signed=True),
            GenvexNabtoDatapointKey.TEMP_SUPPLY: GenvexNabtoDatapoint(read_address=38, divider=100, signed=True),
        }

        self.setpoints = {
            GenvexNabtoSetpointKey.FAN_LEVEL: GenvexNabtoSetpoint(read_address=139, write_address=139, divider=1, min=0, max=4, signed=False),
            GenvexNabtoSetpointKey.FILTER_REPLACE_INTERVAL: GenvexNabtoSetpoint(read_address=159, write_address=159, divider=1, min=0, max=365, signed=False),
            GenvexNabtoSetpointKey.FILTER_REPLACE_RESET: GenvexNabtoSetpoint(read_address=71, write_address=71, divider=1, min=0, max=1, signed=False),
            GenvexNabtoSetpointKey.TEMP_TARGET: GenvexNabtoSetpoint(read_address=140, write_address=140, divider=100, min=0, max=3000, step=5, signed=True),
        }
        
        #device quirks
        if self.device_has_quirk("hotwaterTempSensor", slave_device_model):
            self.datapoints[GenvexNabtoDatapointKey.TEMP_HOTWATER_TOP] = GenvexNabtoDatapoint(read_address=42, divider=100, signed=True)
            self.datapoints[GenvexNabtoDatapointKey.TEMP_HOTWATER_BOTTOM] = GenvexNabtoDatapoint(read_address=43, divider=100, signed=True)

        if self.device_has_quirk("sacrificialAnode", slave_device_model):  
            self.datapoints[GenvexNabtoDatapointKey.SACRIFICIAL_ANODE_OK] = GenvexNabtoDatapoint(read_address=142, divider=1, signed=False)
            
        if self.device_has_quirk("reheat", slave_device_model):  
            self.setpoints[GenvexNabtoSetpointKey.REHEAT_ENABLE] = GenvexNabtoSetpoint(read_address=281, write_address=281, divider=1, min=0, max=1, signed=False)

        if self.device_has_quirk("exhaustTempSensor", slave_device_model):  
            self.datapoints[GenvexNabtoDatapointKey.TEMP_EXHAUST] = GenvexNabtoDatapoint(read_address=34, divider=100, signed=True)

        if self.device_has_quirk("antiLegionella", slave_device_model):  
            self.setpoints[GenvexNabtoSetpointKey.ANTILEGIONELLA_DAY] = GenvexNabtoSetpoint(read_address=194, write_address=194, divider=1, min=0, max=7, signed=False)

        if self.device_has_quirk("hotwaterTempSet", slave_device_model):  
            self.setpoints[GenvexNabtoSetpointKey.TEMP_HOTWATER] = GenvexNabtoSetpoint(read_address=190, write_address=190, divider=100, min=2000, max=7000, step=10, signed=True)
            self.setpoints[GenvexNabtoSetpointKey.TEMP_HOTWATER_BOOST] = GenvexNabtoSetpoint(read_address=189, write_address=189, divider=100, min=2000, max=7000, step=10, signed=True)

        if self.device_has_quirk("summerTemperatures", slave_device_model):
            self.setpoints[GenvexNabtoSetpointKey.TEMP_SUMMER_SUPPLY_MIN] = GenvexNabtoSetpoint(read_address=171, write_address=171, divider=100, min=0, max=4000, step=10, signed=True)
            self.setpoints[GenvexNabtoSetpointKey.TEMP_SUMMER_SUPPLY_MAX] = GenvexNabtoSetpoint(read_address=173, write_address=173, divider=100, min=0, max=4000, step=10, signed=True)

        if self.device_has_quirk("coolingPriority", slave_device_model):
            self.setpoints[GenvexNabtoSetpointKey.COMPRESSOR_PRIORITY] = GenvexNabtoSetpoint(read_address=191, write_address=191, divider=1, min=0, max=1, signed=False)

        if self.device_has_quirk("coolingOffset", slave_device_model):
            self.setpoints[GenvexNabtoSetpointKey.TEMP_COOLING_START_OFFSET] = GenvexNabtoSetpoint(read_address=170, write_address=170, divider=1, min=0, max=8, signed=True)
        
        self.set_default_configs()

        #place config modifiers here

        
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
        
        
    def device_has_quirk(self, quirk:str, device:int) -> bool:
        if quirk not in self._quirks: return False
        return device in self._quirks[quirk]