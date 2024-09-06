from .basemodel import ( GenvexNabtoBaseModel, GenvexNabtoDatapointKey, GenvexNabtoDatapoint, GenvexNabtoSetpointKey, GenvexNabtoSetpoint )


class GenvexNabtoCTS400(GenvexNabtoBaseModel):
    def __init__(self, device_number:int, slave_device_number:int, slave_device_model:int):
        super().__init__()

        self._attr_manufacturer="Nilan"
        self._attr_model_name="CTS 400"

        self.datapoints = {
            GenvexNabtoDatapointKey.BYPASS_ACTIVE: GenvexNabtoDatapoint(read_address=23, divider=1, signed=False),
            GenvexNabtoDatapointKey.FAN_DUTYCYCLE_EXTRACT: GenvexNabtoDatapoint(read_address=24, divider=10, signed=False),
            GenvexNabtoDatapointKey.FAN_DUTYCYCLE_SUPPLY: GenvexNabtoDatapoint(read_address=25, divider=10, signed=False),
            GenvexNabtoDatapointKey.TEMP_OUTSIDE: GenvexNabtoDatapoint(read_address=27, divider=10, signed=True),
            GenvexNabtoDatapointKey.TEMP_SUPPLY: GenvexNabtoDatapoint(read_address=28, divider=10, signed=True),
            GenvexNabtoDatapointKey.TEMP_EXTRACT: GenvexNabtoDatapoint(read_address=29, divider=10, signed=True),
            GenvexNabtoDatapointKey.TEMP_EXHAUST: GenvexNabtoDatapoint(read_address=30, divider=10, signed=True),
            GenvexNabtoDatapointKey.HUMIDITY: GenvexNabtoDatapoint(read_address=31, divider=10, signed=False),
            GenvexNabtoDatapointKey.HUMIDITY_AVG: GenvexNabtoDatapoint(read_address=46, divider=10, signed=False),
            GenvexNabtoDatapointKey.CO2_LEVEL: GenvexNabtoDatapoint(read_address=47, divider=1, signed=False),
            GenvexNabtoDatapointKey.VOC_LEVEL: GenvexNabtoDatapoint(read_address=48, divider=1, signed=False),
            GenvexNabtoDatapointKey.FILTER_OK: GenvexNabtoDatapoint(read_address=49, divider=1, signed=False, invert_from=1),
            GenvexNabtoDatapointKey.ALARM_STATUS: GenvexNabtoDatapoint(read_address=50, divider=1, signed=False),
            GenvexNabtoDatapointKey.ALARM_1_CODE: GenvexNabtoDatapoint(read_address=51, divider=1, signed=False),
            GenvexNabtoDatapointKey.ALARM_2_CODE: GenvexNabtoDatapoint(read_address=52, divider=1, signed=False),
            GenvexNabtoDatapointKey.ALARM_3_CODE: GenvexNabtoDatapoint(read_address=53, divider=1, signed=False),     
            GenvexNabtoDatapointKey.ALARM_1_INFO: GenvexNabtoDatapoint(read_address=56, divider=1, signed=False),
            GenvexNabtoDatapointKey.ALARM_2_INFO: GenvexNabtoDatapoint(read_address=57, divider=1, signed=False),
            GenvexNabtoDatapointKey.ALARM_3_INFO: GenvexNabtoDatapoint(read_address=58, divider=1, signed=False),             
            GenvexNabtoDatapointKey.FAN_LEVEL_CURRENT: GenvexNabtoDatapoint(read_address=63, divider=1, signed=False),             
            GenvexNabtoDatapointKey.HUMIDITY_AVG_OK: GenvexNabtoDatapoint(read_address=64, divider=1, signed=False),             
            GenvexNabtoDatapointKey.HUMIDITY_HIGH_LEVEL: GenvexNabtoDatapoint(read_address=66, divider=10, signed=False),             
            GenvexNabtoDatapointKey.HUMIDITY_HIGH_LEVEL_TIME: GenvexNabtoDatapoint(read_address=70, divider=1, signed=False),             
            GenvexNabtoDatapointKey.WINTER_MODE_ACTIVE: GenvexNabtoDatapoint(read_address=72, divider=1, signed=False),
            GenvexNabtoDatapointKey.FILTER_REPLACE_TIME_AGO: GenvexNabtoDatapoint(read_address=77, divider=1, signed=False),
            GenvexNabtoDatapointKey.DEFROST_ACTIVE: GenvexNabtoDatapoint(read_address=91, divider=1, signed=False),
            GenvexNabtoDatapointKey.FILTER_REPLACE_TIME_REMAIN: GenvexNabtoDatapoint(read_address=110, divider=1, signed=False),
        }

        self.setpoints = {
            GenvexNabtoSetpointKey.ALARM_RESET: GenvexNabtoSetpoint(read_address=30, write_address=30, divider=1, min=0, max=1, signed=False),
            GenvexNabtoSetpointKey.HUMIDITY_LOW_THRESHOLD: GenvexNabtoSetpoint(read_address=31, write_address=31, divider=10, min=150, max=450, step=5, signed=False),
            GenvexNabtoSetpointKey.FAN_LEVEL_LOW_HUMIDITY: GenvexNabtoSetpoint(read_address=32, write_address=32, divider=1, min=0, max=3, signed=False),
            GenvexNabtoSetpointKey.FAN_LEVEL_HIGH_HUMIDITY: GenvexNabtoSetpoint(read_address=33, write_address=33, divider=1, min=2, max=4, signed=False),
            GenvexNabtoSetpointKey.FAN_LEVEL_HIGH_HUMIDITY_TIME: GenvexNabtoSetpoint(read_address=34, write_address=34, divider=1, min=0, max=180, signed=False),
            GenvexNabtoSetpointKey.CO2_THRESHOLD: GenvexNabtoSetpoint(read_address=35, write_address=35, divider=1, min=500, max=2000, signed=False),
            GenvexNabtoSetpointKey.VOC_THRESHOLD: GenvexNabtoSetpoint(read_address=36, write_address=36, divider=1, min=500, max=2000, signed=False),
            GenvexNabtoSetpointKey.TEMP_TARGET: GenvexNabtoSetpoint(read_address=37, write_address=37, divider=10, min=100, max=300, step=5, signed=True),
            GenvexNabtoSetpointKey.TEMP_REGULATION_DEAD_BAND: GenvexNabtoSetpoint(read_address=38, write_address=38, divider=10, min=0, max=40, step=5, signed=True),
            GenvexNabtoSetpointKey.TEMP_DEFROST_LOW_THRESHOLD: GenvexNabtoSetpoint(read_address=39, write_address=39, divider=10, min=10, max=50, step=5, signed=True),
            GenvexNabtoSetpointKey.TEMP_DEFROST_HIGH_THRESHOLD: GenvexNabtoSetpoint(read_address=40, write_address=40, divider=10, min=50, max=100, step=5, signed=True),
            GenvexNabtoSetpointKey.DEFROST_MAX_TIME: GenvexNabtoSetpoint(read_address=41, write_address=41, divider=1, min=5, max=60, signed=False),
            GenvexNabtoSetpointKey.DEFROST_BREAK_TIME: GenvexNabtoSetpoint(read_address=43, write_address=43, divider=1, min=15, max=760, signed=False),
            GenvexNabtoSetpointKey.TEMP_WINTER_MODE_THRESHOLD: GenvexNabtoSetpoint(read_address=45, write_address=45, divider=10, min=50, max=200, step=5, signed=True),
            GenvexNabtoSetpointKey.FILTER_REPLACE_INTERVAL: GenvexNabtoSetpoint(read_address=50, write_address=50, divider=1, min=0, max=360, signed=False),
            GenvexNabtoSetpointKey.FILTER_REPLACE_RESET: GenvexNabtoSetpoint(read_address=51, write_address=51, divider=1, min=0, max=1, signed=False),
            GenvexNabtoSetpointKey.TEMP_SUPPLY_MIN: GenvexNabtoSetpoint(read_address=57, write_address=57, divider=10, min=100, max=200, step=5, signed=True),
            GenvexNabtoSetpointKey.TEMP_SUPPLY_MAX: GenvexNabtoSetpoint(read_address=58, write_address=58, divider=10, min=100, max=500, step=5, signed=True),
            GenvexNabtoSetpointKey.FAN_LEVEL1_SUPPLY_PRESET: GenvexNabtoSetpoint(read_address=59, write_address=59, divider=10, min=200, max=1000, signed=False),
            GenvexNabtoSetpointKey.FAN_LEVEL2_SUPPLY_PRESET: GenvexNabtoSetpoint(read_address=60, write_address=60, divider=10, min=200, max=1000, signed=False),
            GenvexNabtoSetpointKey.FAN_LEVEL3_SUPPLY_PRESET: GenvexNabtoSetpoint(read_address=61, write_address=61, divider=10, min=200, max=1000, signed=False),
            GenvexNabtoSetpointKey.FAN_LEVEL4_SUPPLY_PRESET: GenvexNabtoSetpoint(read_address=62, write_address=62, divider=10, min=200, max=1000, signed=False),
            GenvexNabtoSetpointKey.FAN_LEVEL1_EXTRACT_PRESET: GenvexNabtoSetpoint(read_address=63, write_address=63, divider=10, min=200, max=1000, signed=False),
            GenvexNabtoSetpointKey.FAN_LEVEL2_EXTRACT_PRESET: GenvexNabtoSetpoint(read_address=64, write_address=64, divider=10, min=200, max=1000, signed=False),
            GenvexNabtoSetpointKey.FAN_LEVEL3_EXTRACT_PRESET: GenvexNabtoSetpoint(read_address=65, write_address=65, divider=10, min=200, max=1000, signed=False),
            GenvexNabtoSetpointKey.FAN_LEVEL4_EXTRACT_PRESET: GenvexNabtoSetpoint(read_address=66, write_address=66, divider=10, min=200, max=1000, signed=False),
            GenvexNabtoSetpointKey.FAN_LEVEL: GenvexNabtoSetpoint(read_address=69, write_address=69, divider=1, min=1, max=4, signed=False),
            GenvexNabtoSetpointKey.FAN_LEVEL_HIGH_CO2: GenvexNabtoSetpoint(read_address=80, write_address=80, divider=1, min=2, max=4, signed=False),
            GenvexNabtoSetpointKey.ENABLE: GenvexNabtoSetpoint(read_address=70, write_address=70, divider=1, min=0, max=1, signed=False),
        }
        
        self.set_default_configs()