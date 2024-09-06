from .basemodel import ( GenvexNabtoBaseModel, GenvexNabtoDatapointKey, GenvexNabtoDatapoint, GenvexNabtoSetpointKey, GenvexNabtoSetpoint, GenvexNabtoUnits )

class GenvexNabtoOptima270(GenvexNabtoBaseModel):
    def __init__(self, device_number:int, slave_device_number:int, slave_device_model:int):
        super().__init__()

        self._attr_manufacturer="Genvex"
        self._attr_model_name="Optima 270"

        self.datapoints = {
            GenvexNabtoDatapointKey.ALARM_BITS: GenvexNabtoDatapoint(read_address=38, divider=1, signed=False),        
            GenvexNabtoDatapointKey.BYPASS_ACTIVE: GenvexNabtoDatapoint(read_address=53, divider=1, signed=False),
            GenvexNabtoDatapointKey.FAN_DUTYCYCLE_EXTRACT: GenvexNabtoDatapoint(read_address=19, divider=100, signed=False),
            GenvexNabtoDatapointKey.FAN_DUTYCYCLE_SUPPLY: GenvexNabtoDatapoint(read_address=18, divider=100, signed=False),
            GenvexNabtoDatapointKey.FAN_RPM_EXTRACT: GenvexNabtoDatapoint(read_address=36, divider=1, signed=False),
            GenvexNabtoDatapointKey.FAN_RPM_SUPPLY: GenvexNabtoDatapoint(read_address=35, divider=1, signed=False),
            GenvexNabtoDatapointKey.HUMIDITY: GenvexNabtoDatapoint(read_address=26, divider=1, signed=False),
            GenvexNabtoDatapointKey.TEMP_EXHAUST: GenvexNabtoDatapoint(read_address=22, divider=10, offset=-300, signed=True),
            GenvexNabtoDatapointKey.TEMP_EXTRACT: GenvexNabtoDatapoint(read_address=23, divider=10, offset=-300, signed=True),
            GenvexNabtoDatapointKey.TEMP_OUTSIDE: GenvexNabtoDatapoint(read_address=21, divider=10, offset=-300, signed=True),
            GenvexNabtoDatapointKey.TEMP_SUPPLY: GenvexNabtoDatapoint(read_address=20, divider=10, offset=-300, signed=True),
            # The following 2 i cannot find documentation on, the type and function is therefore unknown.
            # GenvexNabtoDatapointKey.REHEAT_PWM: GenvexNabtoDatapoint(read_address=41, divider=100, signed=False),
            # GenvexNabtoDatapointKey.REHEAT_PWM: GenvexNabtoDatapoint(read_address=42, divider=100, signed=False),
        }

        self.setpoints = {
            GenvexNabtoSetpointKey.BOOST_ENABLE: GenvexNabtoSetpoint(read_address=30, write_address=70, divider=1, min=0, max=1, signed=False),
            GenvexNabtoSetpointKey.BOOST_TIME: GenvexNabtoSetpoint(read_address=70, write_address=150, divider=1, min=1, max=120, signed=False),
            GenvexNabtoSetpointKey.FAN_LEVEL: GenvexNabtoSetpoint(read_address=7, write_address=24, divider=1, min=0, max=4, signed=False),
            GenvexNabtoSetpointKey.FAN_LEVEL1_EXTRACT_PRESET: GenvexNabtoSetpoint(read_address=13, write_address=36, divider=1, min=0, max=100, signed=False),
            GenvexNabtoSetpointKey.FAN_LEVEL1_SUPPLY_PRESET: GenvexNabtoSetpoint(read_address=10, write_address=30, divider=1, min=0, max=100, signed=False),
            GenvexNabtoSetpointKey.FAN_LEVEL2_EXTRACT_PRESET: GenvexNabtoSetpoint(read_address=14, write_address=38, divider=1, min=0, max=100, signed=False),
            GenvexNabtoSetpointKey.FAN_LEVEL2_SUPPLY_PRESET: GenvexNabtoSetpoint(read_address=11, write_address=32, divider=1, min=0, max=100, signed=False),
            GenvexNabtoSetpointKey.FAN_LEVEL3_EXTRACT_PRESET: GenvexNabtoSetpoint(read_address=15, write_address=40, divider=1, min=0, max=100, signed=False),
            GenvexNabtoSetpointKey.FAN_LEVEL3_SUPPLY_PRESET: GenvexNabtoSetpoint(read_address=12, write_address=34, divider=1, min=0, max=100, signed=False),
            GenvexNabtoSetpointKey.FAN_LEVEL4_EXTRACT_PRESET: GenvexNabtoSetpoint(read_address=9, write_address=28, divider=1, min=0, max=100, signed=False),
            GenvexNabtoSetpointKey.FAN_LEVEL4_SUPPLY_PRESET: GenvexNabtoSetpoint(read_address=8, write_address=26, divider=1, min=0, max=100, signed=False),
            GenvexNabtoSetpointKey.FILTER_REPLACE_INTERVAL: GenvexNabtoSetpoint(read_address=100, write_address=210, divider=1, min=0, max=12, signed=False),
            GenvexNabtoSetpointKey.FILTER_REPLACE_RESET: GenvexNabtoSetpoint(read_address=50, write_address=110, divider=1, min=0, max=1, signed=False),
            GenvexNabtoSetpointKey.HUMIDITY_CONTROL_ENABLE: GenvexNabtoSetpoint(read_address=6, write_address=22, divider=1, min=0, max=1, signed=False),
            GenvexNabtoSetpointKey.REHEAT_ENABLE: GenvexNabtoSetpoint(read_address=3, write_address=16, divider=1, min=0, max=1, signed=False),
            GenvexNabtoSetpointKey.TEMP_BYPASS_OPEN_OFFSET: GenvexNabtoSetpoint(read_address=21, write_address=52, divider=10, min=10, max=100, signed=True),
            GenvexNabtoSetpointKey.TEMP_TARGET: GenvexNabtoSetpoint(read_address=1, write_address=12, divider=10, offset=100, min=0, max=200, step=5, signed=True),
        }
        
        self.set_default_configs()
        self._configs[GenvexNabtoSetpointKey.FILTER_REPLACE_INTERVAL]["unit_of_measurement"] = GenvexNabtoUnits.MONTHS