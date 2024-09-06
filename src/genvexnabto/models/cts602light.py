from .basemodel import ( GenvexNabtoBaseModel, GenvexNabtoDatapointKey, GenvexNabtoDatapoint, GenvexNabtoSetpointKey, GenvexNabtoSetpoint )

class GenvexNabtoCTS602Light(GenvexNabtoBaseModel):
    def __init__(self, device_number:int, slave_device_number:int, slave_device_model:int):
        super().__init__()

        self._attr_manufacturer="Nilan"
        self._attr_model_name="CTS 602 light"


        self.datapoints = {
            GenvexNabtoDatapointKey.BYPASS_ACTIVE: GenvexNabtoDatapoint(read_address=129, divider=1, signed=False),
            GenvexNabtoDatapointKey.FAN_DUTYCYCLE_EXTRACT: GenvexNabtoDatapoint(read_address=99, divider=1, signed=False),
            GenvexNabtoDatapointKey.FAN_DUTYCYCLE_SUPPLY: GenvexNabtoDatapoint(read_address=98, divider=1, signed=False),
            GenvexNabtoDatapointKey.FILTER_REPLACE_TIME_REMAIN: GenvexNabtoDatapoint(read_address=101, divider=1, signed=False),
            GenvexNabtoDatapointKey.HUMIDITY: GenvexNabtoDatapoint(read_address=51, divider=100, signed=False),
            GenvexNabtoDatapointKey.TEMP_EXHAUST: GenvexNabtoDatapoint(read_address=33, divider=100, signed=True),
            GenvexNabtoDatapointKey.TEMP_EXTRACT: GenvexNabtoDatapoint(read_address=34, divider=100, signed=True),
            GenvexNabtoDatapointKey.TEMP_OUTSIDE: GenvexNabtoDatapoint(read_address=38, divider=100, signed=True),
            GenvexNabtoDatapointKey.TEMP_SUPPLY: GenvexNabtoDatapoint(read_address=37, divider=100, signed=True),
        }

        self.setpoints = {
            GenvexNabtoSetpointKey.FAN_LEVEL: GenvexNabtoSetpoint(read_address=135, write_address=135, divider=1, min=0, max=4, signed=False),
            GenvexNabtoSetpointKey.FILTER_REPLACE_INTERVAL: GenvexNabtoSetpoint(read_address=153, write_address=153, divider=1, min=0, max=365, signed=False),
            GenvexNabtoSetpointKey.FILTER_REPLACE_RESET: GenvexNabtoSetpoint(read_address=67, write_address=67, divider=1, min=0, max=1, signed=False),            
            GenvexNabtoSetpointKey.TEMP_TARGET: GenvexNabtoSetpoint(read_address=136, write_address=136, divider=100, min=0, max=3000, step=5, signed=True),
        }

        self.set_default_configs()