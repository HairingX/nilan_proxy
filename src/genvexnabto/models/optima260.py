from .basemodel import ( GenvexNabtoBaseModel, GenvexNabtoDatapointKey, GenvexNabtoDatapoint, GenvexNabtoSetpointKey, GenvexNabtoSetpoint, GenvexNabtoUnits )

class GenvexNabtoOptima260(GenvexNabtoBaseModel):
    def __init__(self, device_number:int, slave_device_number:int, slave_device_model:int):
        super().__init__()

        self._attr_manufacturer="Genvex"
        self._attr_model_name="Optima 260"

        self.datapoints = {
            GenvexNabtoDatapointKey.BYPASS_ACTIVE: GenvexNabtoDatapoint(read_address=11, divider=1, signed=False),
            GenvexNabtoDatapointKey.FAN_DUTYCYCLE_EXTRACT: GenvexNabtoDatapoint(read_address=10, divider=1, signed=False),
            GenvexNabtoDatapointKey.FAN_DUTYCYCLE_SUPPLY: GenvexNabtoDatapoint(read_address=9, divider=1, signed=False),
            GenvexNabtoDatapointKey.HUMIDITY: GenvexNabtoDatapoint(read_address=13, divider=1, signed=False),
            GenvexNabtoDatapointKey.TEMP_EXHAUST: GenvexNabtoDatapoint(read_address=3, divider=10, offset=-300, signed=True), #T4
            GenvexNabtoDatapointKey.TEMP_EXTRACT: GenvexNabtoDatapoint(read_address=6, divider=10, offset=-300, signed=True), #T7
            GenvexNabtoDatapointKey.TEMP_OUTSIDE: GenvexNabtoDatapoint(read_address=2, divider=10, offset=-300, signed=True), #T3
            GenvexNabtoDatapointKey.TEMP_SUPPLY: GenvexNabtoDatapoint(read_address=0, divider=10, offset=-300, signed=True), #T1
        }

        self.setpoints = {
            GenvexNabtoSetpointKey.FAN_LEVEL: GenvexNabtoSetpoint(read_address=0, write_address=0, divider=1, min=0, max=4, signed=False),
            GenvexNabtoSetpointKey.FAN_LEVEL1_EXTRACT_PRESET: GenvexNabtoSetpoint(read_address=10, write_address=10, divider=1, min=0, max=100, signed=False),
            GenvexNabtoSetpointKey.FAN_LEVEL1_SUPPLY_PRESET: GenvexNabtoSetpoint(read_address=7, write_address=7, divider=1, min=0, max=100, signed=False),
            GenvexNabtoSetpointKey.FAN_LEVEL2_EXTRACT_PRESET: GenvexNabtoSetpoint(read_address=11, write_address=11, divider=1, min=0, max=100, signed=False),
            GenvexNabtoSetpointKey.FAN_LEVEL2_SUPPLY_PRESET: GenvexNabtoSetpoint(read_address=8, write_address=8, divider=1, min=0, max=100, signed=False),
            GenvexNabtoSetpointKey.FAN_LEVEL3_EXTRACT_PRESET: GenvexNabtoSetpoint(read_address=12, write_address=12, divider=1, min=0, max=100, signed=False),
            GenvexNabtoSetpointKey.FAN_LEVEL3_SUPPLY_PRESET: GenvexNabtoSetpoint(read_address=9, write_address=9, divider=1, min=0, max=100, signed=False),
            GenvexNabtoSetpointKey.FILTER_REPLACE_INTERVAL: GenvexNabtoSetpoint(read_address=5, write_address=5, divider=1, min=0, max=12, signed=False),            
            GenvexNabtoSetpointKey.FILTER_REPLACE_RESET: GenvexNabtoSetpoint(read_address=47, write_address=47, divider=1, min=0, max=1, signed=False),          
            GenvexNabtoSetpointKey.HUMIDITY_CONTROL_ENABLE: GenvexNabtoSetpoint(read_address=5, write_address=5, divider=1, min=0, max=1, signed=False),
            GenvexNabtoSetpointKey.TEMP_BYPASS_OPEN_OFFSET: GenvexNabtoSetpoint(read_address=18, write_address=18, divider=10, min=10, max=100, signed=True),
            GenvexNabtoSetpointKey.TEMP_TARGET: GenvexNabtoSetpoint(read_address=2, write_address=2, divider=10, offset=100, min=0, max=200, step=5, signed=True),
        }
        
        self.set_default_configs()
        self._configs[GenvexNabtoSetpointKey.FILTER_REPLACE_INTERVAL]["unit_of_measurement"] = GenvexNabtoUnits.MONTHS