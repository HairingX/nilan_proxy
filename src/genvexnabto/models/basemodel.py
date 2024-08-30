from typing import Dict, List, TypedDict


class GenvexNabtoDatapointKey:
    ALARM_1 = "alarm_1"
    ALARM_2 = "alarm_2"
    ALARM_3 = "alarm_3"
    ALARM_ACTIVE = "alarm_active"
    ALARM_BITS = "alarm_bits"
    BYPASS_ACTIVE = "bypass_active"
    CO2_LEVEL = "co2_level"
    DEFROST_ACTIVE = "defrost_active"
    DEFROST_TIME_AGO = "defrost_time_ago"
    """
    (default=days)
    """
    FAN_DUTYCYCLE_EXTRACT = "fan_dutycycle_extract"
    FAN_DUTYCYCLE_SUPPLY = "fan_dutycycle_supply"
    FAN_LEVEL_EXTRACT = "fan_level_extract"
    FAN_LEVEL_SUPPLY = "fan_level_supply"
    FAN_RPM_EXTRACT = "fan_rpm_extract"
    FAN_RPM_SUPPLY = "fan_rpm_supply"
    FILTER_REPLACE_TIME_REMAIN = "filter_replace_time_remain"
    """
    (default=days)
    """
    FILTER_REPLACE_TIME_AGO = "filter_replace_time_ago"
    """
    (default=days)
    """
    HUMIDITY = "humidity"
    PREHEAT_PWM = "preheat_pwm"
    REHEAT_PWM = "reheat_pwm"
    SACRIFICIAL_ANODE_OK = "sacrificial_anode_ok"
    STATE_CODE = "state_code"
    WINTER_MODE_ACTIVE = "winter_mode_active"
    TEMP_CONDENSER = "temp_condenser"
    TEMP_EVAPORATOR = "temp_evaporator"
    TEMP_EXHAUST = "temp_exhaust"
    TEMP_EXTRACT = "temp_extract"
    TEMP_HOTWATER_BOTTOM = "temp_hotwater_bottom"
    TEMP_HOTWATER_TOP = "temp_hotwater_top"
    TEMP_OUTSIDE = "temp_outside"
    TEMP_ROOM = "temp_room"
    TEMP_SUPPLY = "temp_supply"


class GenvexNabtoSetpointKey:
    """
    Setpoints that can be read/written.

    If a key has double underscore '__' followed by a number, it contains preset values that can be different from the read value.
    """

    ANTILEGIONELLA_DAY = "antilegionella_day"
    """
    Day of the week the legionella treatment is performed.
    
    Typically this is used when a hot water tank is installed.
    
    Values:
    - 0: "OFF",
    - 1: "+0",
    - 2: "+1",
    - 3: "+2",
    - 4: "+3",
    - 5: "+4",
    - 6: "+5",
    - 7: "+7",
    - 8: "+10"
    """
    BOOST_ENABLE = "boost_enable"
    """
    Enable the boost function for the unit.
    """
    BOOST_TIME = "boost_time"
    """
    Time the boost function will run when triggered. (default=minutes)
    """
    COOLING_ENABLE = "cooling_enable"
    """
    Enable the cooling function for the unit.
    
    Typically this will be active cooling, bypass has its own key.
    """
    COMPRESSOR_PRIORITY = "compressor_priority"
    """
    Priority for the compressor.
    """
    ENABLE = "enable"
    """
    Enable the unit.
    """
    FAN_LEVEL = "fan_level"
    """
    Select the fan level.
    
    Typically this activates a preset configuration.
    """
    FAN_LEVEL1_EXTRACT_PRESET = "fan_level1_extract_preset"
    """
    Fan level preset.
    """
    FAN_LEVEL1_SUPPLY_PRESET = "fan_level1_supply_preset"
    """
    Fan level preset.
    """
    FAN_LEVEL2_EXTRACT_PRESET = "fan_level2_extract_preset"
    """
    Fan level preset.
    """
    FAN_LEVEL2_SUPPLY_PRESET = "fan_level2_supply_preset"
    """
    Fan level preset.
    """
    FAN_LEVEL3_EXTRACT_PRESET = "fan_level3_extract_preset"
    """
    Fan level preset.
    """
    FAN_LEVEL3_SUPPLY_PRESET = "fan_level3_supply_preset"
    """
    Fan level preset.
    """
    FAN_LEVEL4_EXTRACT_PRESET = "fan_level4_extract_preset"
    """
    Fan level preset.
    """
    FAN_LEVEL4_SUPPLY_PRESET = "fan_level4_supply_preset"
    """
    Fan level preset.
    """
    FILTER_REPLACE_INTERVAL = "filter_replace_interval_months"
    """
    Time interval between filter replacements/maintenance (default=days)
    """
    FILTER_REPLACE_RESET = "filter_replace_reset"
    """
    Resets/restarts the timer for filter replacements/maintenance.
    """
    HUMIDITY_CONTROL_ENABLE = "humidity_control_enable"
    """
    Enable the humidity function for the unit.
    
    Typically this will be extra fan level when showering or alike.
    """
    PREHEATING_ENABLE = "preheating_enable"
    """
    Enable the prehet function for the unit.
    
    Typically this will be a heating element for the outside air.
    """
    REHEATING_ENABLE = "reheating_enable"
    """
    Enable the prehet function for the unit.
    
    Typically this will be a heating element for the extract air.
    """
    TEMP_BYPASS_OPEN_OFFSET = "temp_bypass_open_offset"
    """
    Temperature offset for when the bypass function.
    
    Typically the bypass function will be a passive function to keep indoor temperature near the target.
    """
    TEMP_COOLING_START_OFFSET = "temp_cooling_start_offset"
    """
    Temperature increase amount before cooling is started.
    
    Values:
    - 0: "OFF",
    - 1: "+0",
    - 2: "+1",
    - 3: "+2",
    - 4: "+3",
    - 5: "+4",
    - 6: "+5",
    - 7: "+7",
    - 8: "+10"
    """
    TEMP_HOTWATER = "temp_hotwater"
    """
    Temperature setpoint for the hot water.
    
    Typically this is used when a hot water container is installed
    
    This is the main heating element
    """
    TEMP_HOTWATER_BOOST = "temp_hotwater_boost"
    """
    Temperature boost setpoint for the hot water.
    
    Typically this is used when a hot water container is installed
    
    This is the auxiliary (boosting) heating element
    """
    TEMP_TARGET = "temp_target"
    """
    Temperature setpoint for the home
    """
    TEMP_SUMMER_SUPPLY_MAX = "temp_summer_supply_max"
    """
    Temperature limit for summer supply air.
    
    Typically this is used when a heater is heating the air.
    """
    TEMP_SUMMER_SUPPLY_MIN = "temp_summer_supply_min"
    """
    Temperature limit for summer supply air.
    
    Typically this is used when a heater is heating the air.
    """
    TEMP_SUPPLY_MAX = "temp_supply_max"
    TEMP_SUPPLY_MIN = "temp_supply_min"
    TEMP_WINTER_SUPPLY_MAX = "temp_winter_supply_max"
    """
    Temperature limit for winter supply air.
    
    Typically this is used when a heater is heating the air.
    """
    TEMP_WINTER_SUPPLY_MIN = "temp_winter_supply_min"
    """
    Temperature limit for winter supply air.
    
    Typically this is used when a heater is heating the air.
    """
    TEMP_WINTER_MODE_THRESHOLD = "temp_winter_mode_threshold"
    """
    Temperature for switching between summer and winter modes.
    
    - When outside temperature is above, summer mode is active.
    - When outside temperature is below, winter mode is active.
    """
class GenvexNabtoDatapoint(TypedDict):
    address: int
    divider: int
    obj: int
    offset: int

class GenvexNabtoSetpoint(TypedDict):
    divider: int
    max: int
    min: int
    offset: int
    read_address: int
    read_obj: int
    step: float
    write_address: int
    write_obj: int


class GenvexNabtoUnits:
    DAYS = "d"
    MONTHS = "m"
    YEARS = "y"
    CELSIUS = "celsius"
    BOOL = "bool"
    BITMASK = "bitmask"
    PPM = "ppm"
    """CONCENTRATION PARTS PER MILLION"""
    RPM = "rpm"
    """REVOLUTIONS PER MINUTE"""
    # INT = "int"
    # FLOAT = "float"
    PCT = "percent"
    UNDEFINED = None


class GenvexNabtoBaseModel:
    _datapoints: Dict[GenvexNabtoDatapointKey, GenvexNabtoDatapoint] = {}
    _setpoints: Dict[GenvexNabtoSetpointKey, GenvexNabtoSetpoint] = {}
    _unitOfMeasures: Dict[GenvexNabtoDatapointKey|GenvexNabtoSetpointKey, str] = {}
    _valueMap: Dict[GenvexNabtoDatapointKey|GenvexNabtoSetpointKey, Dict[float | int, float | int | str]] = {}
    _quirks: Dict[str, list[int]] = {}

    _defaultDatapointRequest: List[GenvexNabtoDatapointKey] = []
    _defaultSetpointRequest: List[GenvexNabtoDatapointKey] = []

    def __init__(self):
        return

    def getModelName(self):
        return "Basemodel"

    def getModelType(self):
        return ""

    def getManufacturer(self):
        return ""

    def modelProvidesDatapoint(self, datapoint: GenvexNabtoDatapointKey) -> bool:
        return datapoint in self._datapoints

    def getDefaultDatapointRequest(self) -> List[GenvexNabtoDatapointKey]:
        return self._defaultDatapointRequest

    def modelProvidesSetpoint(self, datapoint: GenvexNabtoSetpointKey) -> bool:
        return datapoint in self._setpoints

    def getDefaultSetpointRequest(self) -> List[GenvexNabtoSetpointKey]:
        return self._defaultSetpointRequest

    def deviceHasQuirk(self, quirk, device) -> bool:
        if quirk not in self._quirks:
            return False
        return device in self._quirks[quirk]

    def addDeviceQuirks(self, deviceNumber, slaveDeviceNumber, slaveDeviceModel):
        return

    def getUnitOfMeasure(self, key:GenvexNabtoDatapointKey|GenvexNabtoSetpointKey) -> str:
        if key in self._unitOfMeasures:
            return self._unitOfMeasures[key]
        return None

