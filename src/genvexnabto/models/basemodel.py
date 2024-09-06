from enum import Enum
from typing import Dict, List, TypedDict, NotRequired


class GenvexNabtoDatapointKey(Enum):
    ALARM_1_CODE = "alarm_1_code"
    ALARM_1_INFO = "alarm_1_info"
    ALARM_2_CODE = "alarm_2_code"
    ALARM_2_INFO = "alarm_2_info"
    ALARM_3_CODE = "alarm_3_code"
    ALARM_3_INFO = "alarm_3_info"
    ALARM_STATUS = "alarm_status"
    """Indicates if an alarm is active"""
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
    FAN_LEVEL_CURRENT = "fan_level_current" 
    """The fan level currently active"""
    FAN_LEVEL_EXTRACT = "fan_level_extract"
    FAN_LEVEL_SUPPLY = "fan_level_supply"
    FAN_RPM_EXTRACT = "fan_rpm_extract"
    FAN_RPM_SUPPLY = "fan_rpm_supply"
    FILTER_REPLACE_TIME_AGO = "filter_replace_time_ago"
    """
    (default=days)
    """
    FILTER_REPLACE_TIME_REMAIN = "filter_replace_time_remain"
    """
    (default=days)
    """
    FILTER_OK = "filter_ok"
    HUMIDITY = "humidity"
    HUMIDITY_AVG = "humidity_average"
    HUMIDITY_AVG_OK = "humidity_average_ok"
    HUMIDITY_HIGH_LEVEL = "humidity_high_level"
    HUMIDITY_HIGH_LEVEL_TIME = "humidity_high_level_time"
    SACRIFICIAL_ANODE_OK = "sacrificial_anode_ok"
    STATE_CODE = "state_code"
    TEMP_CONDENSER = "temp_condenser"
    TEMP_EVAPORATOR = "temp_evaporator"
    TEMP_EXHAUST = "temp_exhaust"
    TEMP_EXTRACT = "temp_extract"
    TEMP_HOTWATER_BOTTOM = "temp_hotwater_bottom"
    TEMP_HOTWATER_TOP = "temp_hotwater_top"
    TEMP_OUTSIDE = "temp_outside"
    TEMP_ROOM = "temp_room"
    TEMP_SUPPLY = "temp_supply"
    VOC_LEVEL = "voc_level"
    WINTER_MODE_ACTIVE = "winter_mode_active"
    
    UNKNOWN_VALUE_1 = "unknown_value_1"


class GenvexNabtoSetpointKey(Enum):
    """
    Setpoints that can be read/written.

    If a key has double underscore '__' followed by a number, it contains preset values that can be different from the read value.
    """
    ALARM_RESET = "alarm_reset"

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
    """Enable the boost function for the unit."""
    BOOST_TIME = "boost_time"
    """Time the boost function will run when triggered. (default=minutes)."""
    CO2_THRESHOLD = "co2_threshold"
    COOLING_ENABLE = "cooling_enable"
    """Enable the cooling function for the unit.
    
    Typically this will be active cooling, bypass has its own key.
    """
    COMPRESSOR_PRIORITY = "compressor_priority"
    """Priority for the compressor.
    """
    DEFROST_BREAK_TIME = "defrost_break_time"
    DEFROST_MAX_TIME = "defrost_max_time"
    ENABLE = "enable"
    """Enable the unit."""
    FAN_LEVEL = "fan_level"
    """Select the fan level.
    Typically this activates a preset configuration.
    """
    FAN_LEVEL_LOW_HUMIDITY = "fan_level_low_humidity"
    FAN_LEVEL_HIGH_CO2 = "fan_level_high_co2"
    FAN_LEVEL_HIGH_HUMIDITY = "fan_level_high_humidity"
    FAN_LEVEL_HIGH_HUMIDITY_TIME = "fan_level_high_humidity_time"
    FAN_LEVEL1_EXTRACT_PRESET = "fan_level1_extract_preset"
    FAN_LEVEL1_SUPPLY_PRESET = "fan_level1_supply_preset"
    FAN_LEVEL2_EXTRACT_PRESET = "fan_level2_extract_preset"
    FAN_LEVEL2_SUPPLY_PRESET = "fan_level2_supply_preset"
    FAN_LEVEL3_EXTRACT_PRESET = "fan_level3_extract_preset"
    FAN_LEVEL3_SUPPLY_PRESET = "fan_level3_supply_preset"
    FAN_LEVEL4_EXTRACT_PRESET = "fan_level4_extract_preset"
    FAN_LEVEL4_SUPPLY_PRESET = "fan_level4_supply_preset"
    FILTER_REPLACE_INTERVAL = "filter_replace_interval"
    """Time interval between filter replacements/maintenance (default=days)"""
    FILTER_REPLACE_RESET = "filter_replace_reset"
    """Resets/restarts the timer for filter replacements/maintenance."""
    HUMIDITY_CONTROL_ENABLE = "humidity_control_enable"
    """Enable the humidity function for the unit.
    
    Typically this will be extra fan level when showering or alike.
    """
    HUMIDITY_LOW_THRESHOLD = "humidity_low_threshold"
    PREHEAT_ENABLE = "preheat_enable"
    """Enable the preheat function for the unit.
    
    Typically this will be a heating element for the outside air.
    """
    PREHEAT_CYCLE_TIME = "preheat_cycle_time"
    PREHEAT_PID_P = "preheat_pid_p"
    PREHEAT_PID_I = "preheat_pid_i"
    PREHEAT_PID_D = "preheat_pid_d"
    REHEAT_ENABLE = "reheat_enable"
    """Enable the prehet function for the unit.
    
    Typically this will be a heating element for the extract air.
    """
    REHEAT_CYCLE_TIME = "reheat_cycle_time"
    REHEAT_PID_P = "reheat_pid_p"
    REHEAT_PID_I = "reheat_pid_i"
    REHEAT_PID_D = "reheat_pid_d"
    TEMP_BYPASS_OPEN_OFFSET = "temp_bypass_open_offset"
    """Temperature offset for when the bypass function.
    
    Typically the bypass function will be a passive function to keep indoor temperature near the target.
    """
    TEMP_COOLING_START_OFFSET = "temp_cooling_start_offset"
    """Temperature increase amount before cooling is started.
    
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
    TEMP_DEFROST_LOW_THRESHOLD = "temp_defrost_low_threshold"
    """Temperature below this will start defrost function."""
    TEMP_DEFROST_HIGH_THRESHOLD = "temp_defrost_high_threshold"
    """Temperature above this will stop defrost function."""
    TEMP_HOTWATER = "temp_hotwater"
    """Temperature setpoint for the hot water.
    
    Typically this is used when a hot water container is installed.
    
    This is the main heating element.
    """
    TEMP_HOTWATER_BOOST = "temp_hotwater_boost"
    """Temperature boost setpoint for the hot water.
    
    Typically this is used when a hot water container is installed.
    
    This is the auxiliary (boosting) heating element.
    """
    TEMP_REGULATION_DEAD_BAND = "temp_regulation_dead_band"
    """Temperature dead band for regulation to prevent mode switching oscillations."""
    TEMP_REHEAT_OFFSET = "temp_reheat_offset"
    """Temperature offset relative to indoor for the reheating."""
    TEMP_TARGET = "temp_target"
    """Temperature setpoint for the home."""
    TEMP_SUMMER_SUPPLY_MAX = "temp_summer_supply_max"
    """Temperature limit for summer supply air.
    
    Typically this is used when a heater is heating the air.
    """
    TEMP_SUMMER_SUPPLY_MIN = "temp_summer_supply_min"
    """Temperature limit for summer supply air.
    
    Typically this is used when a heater is heating the air.
    """
    TEMP_SUPPLY_MAX = "temp_supply_max"
    TEMP_SUPPLY_MIN = "temp_supply_min"
    TEMP_WINTER_SUPPLY_MAX = "temp_winter_supply_max"
    """Temperature limit for winter supply air.
    
    Typically this is used when a heater is heating the air.
    """
    TEMP_WINTER_SUPPLY_MIN = "temp_winter_supply_min"
    """Temperature limit for winter supply air.
    
    Typically this is used when a heater is heating the air.
    """
    TEMP_WINTER_MODE_THRESHOLD = "temp_winter_mode_threshold"
    """Temperature for switching between summer and winter modes.
    
    - When outside temperature is above, summer mode is active.
    - When outside temperature is below, winter mode is active.
    """
    VOC_THRESHOLD = "voc_threshold"
    
    
class GenvexNabtoDatapoint(TypedDict):
    divider: NotRequired[int]
    """Applied to the register value in the order: 1: invert_from, 2: divider, 3: offset"""
    offset: NotRequired[int]
    """Applied to the register value in the order: 1: invert_from, 2: divider, 3: offset"""
    read_address: int
    read_obj: NotRequired[int]
    """default is 0"""
    signed: bool
    """indication of the data being signed or unsigned"""
    invert_from: NotRequired[int]
    """Applied to the register value in the order: 1: invert_from, 2: divider, 3: offset
    
    Inverts the register value by setting this to the max value, ex. set to 1 to invert a bool"""

class GenvexNabtoSetpoint(GenvexNabtoDatapoint):
    max: int
    """max value in the register"""
    min: int
    """min value in the register"""
    step: NotRequired[int]
    """step size in register value, if unset will default to the divider"""
    write_address: int
    write_obj: NotRequired[int]
    """default is 0"""

class GenvexNabtoPointConfig(TypedDict):
    unit_of_measurement: str|None
    read: bool

class GenvexNabtoUnits:
    SECONDS = "seconds"
    MINUTES = "minutes"
    HOURS = "hours"
    DAYS = "days"
    MONTHS = "months"
    YEARS = "years"
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
    TEXT = "text"
    UNDEFINED = None
    
DEFAULT_CONFIGS:Dict[GenvexNabtoDatapointKey|GenvexNabtoSetpointKey, GenvexNabtoPointConfig] = {
            GenvexNabtoDatapointKey.ALARM_1_CODE: GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.UNDEFINED, read=True),
            GenvexNabtoDatapointKey.ALARM_1_INFO: GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.TEXT, read=True),
            GenvexNabtoDatapointKey.ALARM_2_CODE:GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.UNDEFINED, read=True),
            GenvexNabtoDatapointKey.ALARM_2_INFO: GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.TEXT, read=True),
            GenvexNabtoDatapointKey.ALARM_3_CODE:GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.UNDEFINED, read=True),
            GenvexNabtoDatapointKey.ALARM_3_INFO: GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.TEXT, read=True),
            GenvexNabtoDatapointKey.ALARM_STATUS:GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.BOOL, read=True),
            GenvexNabtoDatapointKey.ALARM_BITS:GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.BITMASK, read=True),
            GenvexNabtoDatapointKey.BYPASS_ACTIVE: GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.BOOL, read=True),
            GenvexNabtoDatapointKey.CO2_LEVEL: GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.PPM, read=True),
            GenvexNabtoDatapointKey.DEFROST_ACTIVE: GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.BOOL, read=True),
            GenvexNabtoDatapointKey.DEFROST_TIME_AGO:GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.DAYS, read=True),
            GenvexNabtoDatapointKey.FAN_DUTYCYCLE_EXTRACT: GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.PCT, read=True),
            GenvexNabtoDatapointKey.FAN_DUTYCYCLE_SUPPLY: GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.PCT, read=True),
            GenvexNabtoDatapointKey.FAN_LEVEL_CURRENT: GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.UNDEFINED, read=True),
            GenvexNabtoDatapointKey.FAN_LEVEL_EXTRACT: GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.UNDEFINED, read=True),
            GenvexNabtoDatapointKey.FAN_LEVEL_SUPPLY: GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.UNDEFINED, read=True),
            GenvexNabtoDatapointKey.FAN_RPM_EXTRACT: GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.RPM, read=True),
            GenvexNabtoDatapointKey.FAN_RPM_SUPPLY: GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.RPM, read=True),
            GenvexNabtoDatapointKey.FILTER_REPLACE_TIME_AGO: GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.DAYS, read=True),
            GenvexNabtoDatapointKey.FILTER_REPLACE_TIME_REMAIN: GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.DAYS, read=True),
            GenvexNabtoDatapointKey.FILTER_OK: GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.BOOL, read=True),
            GenvexNabtoDatapointKey.HUMIDITY: GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.PCT, read=True),
            GenvexNabtoDatapointKey.HUMIDITY_HIGH_LEVEL: GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.UNDEFINED, read=True),
            GenvexNabtoDatapointKey.HUMIDITY_HIGH_LEVEL_TIME: GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.SECONDS, read=True),
            GenvexNabtoDatapointKey.HUMIDITY_AVG: GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.PCT, read=True),
            GenvexNabtoDatapointKey.HUMIDITY_AVG_OK: GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.BOOL, read=True),
            GenvexNabtoDatapointKey.SACRIFICIAL_ANODE_OK: GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.BOOL, read=True),
            GenvexNabtoDatapointKey.STATE_CODE: GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.UNDEFINED, read=True),
            GenvexNabtoDatapointKey.TEMP_CONDENSER:GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.CELSIUS, read=True),
            GenvexNabtoDatapointKey.TEMP_EVAPORATOR:GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.CELSIUS, read=True),
            GenvexNabtoDatapointKey.TEMP_EXHAUST:GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.CELSIUS, read=True),
            GenvexNabtoDatapointKey.TEMP_EXTRACT: GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.CELSIUS, read=True),
            GenvexNabtoDatapointKey.TEMP_HOTWATER_BOTTOM: GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.CELSIUS, read=True),
            GenvexNabtoDatapointKey.TEMP_HOTWATER_TOP: GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.CELSIUS, read=True),
            GenvexNabtoDatapointKey.TEMP_OUTSIDE: GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.CELSIUS, read=True),
            GenvexNabtoDatapointKey.TEMP_ROOM: GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.CELSIUS, read=True),
            GenvexNabtoDatapointKey.TEMP_SUPPLY: GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.CELSIUS, read=True),
            GenvexNabtoDatapointKey.VOC_LEVEL: GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.PPM, read=True),
            GenvexNabtoDatapointKey.WINTER_MODE_ACTIVE:GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.BOOL, read=True),
            
            GenvexNabtoDatapointKey.UNKNOWN_VALUE_1:GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.UNDEFINED, read=True),
            
            GenvexNabtoSetpointKey.ALARM_RESET: GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.BOOL, read=False),
            GenvexNabtoSetpointKey.ANTILEGIONELLA_DAY: GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.UNDEFINED, read=True),
            GenvexNabtoSetpointKey.BOOST_ENABLE: GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.BOOL, read=True),
            GenvexNabtoSetpointKey.BOOST_TIME: GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.MINUTES, read=True),
            GenvexNabtoSetpointKey.CO2_THRESHOLD: GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.PPM, read=True),
            GenvexNabtoSetpointKey.COOLING_ENABLE: GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.BOOL, read=True),
            GenvexNabtoSetpointKey.COMPRESSOR_PRIORITY: GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.UNDEFINED, read=True),
            GenvexNabtoSetpointKey.DEFROST_MAX_TIME: GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.MINUTES, read=True),
            GenvexNabtoSetpointKey.DEFROST_BREAK_TIME: GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.MINUTES, read=True),
            GenvexNabtoSetpointKey.ENABLE: GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.BOOL, read=True),
            GenvexNabtoSetpointKey.FAN_LEVEL: GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.UNDEFINED, read=True),
            GenvexNabtoSetpointKey.FAN_LEVEL_LOW_HUMIDITY: GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.UNDEFINED, read=True),
            GenvexNabtoSetpointKey.FAN_LEVEL_HIGH_CO2: GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.UNDEFINED, read=True),
            GenvexNabtoSetpointKey.FAN_LEVEL_HIGH_HUMIDITY: GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.UNDEFINED, read=True),
            GenvexNabtoSetpointKey.FAN_LEVEL_HIGH_HUMIDITY_TIME: GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.MINUTES, read=True),
            GenvexNabtoSetpointKey.FAN_LEVEL1_EXTRACT_PRESET:GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.PCT, read=True),
            GenvexNabtoSetpointKey.FAN_LEVEL1_SUPPLY_PRESET: GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.PCT, read=True),
            GenvexNabtoSetpointKey.FAN_LEVEL2_EXTRACT_PRESET:GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.PCT, read=True),
            GenvexNabtoSetpointKey.FAN_LEVEL2_SUPPLY_PRESET: GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.PCT, read=True),
            GenvexNabtoSetpointKey.FAN_LEVEL3_EXTRACT_PRESET:GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.PCT, read=True),
            GenvexNabtoSetpointKey.FAN_LEVEL3_SUPPLY_PRESET: GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.PCT, read=True),
            GenvexNabtoSetpointKey.FAN_LEVEL4_EXTRACT_PRESET:GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.PCT, read=True),
            GenvexNabtoSetpointKey.FAN_LEVEL4_SUPPLY_PRESET: GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.PCT, read=True),
            GenvexNabtoSetpointKey.FILTER_REPLACE_INTERVAL: GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.DAYS, read=True),
            GenvexNabtoSetpointKey.FILTER_REPLACE_RESET: GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.BOOL, read=False),
            GenvexNabtoSetpointKey.HUMIDITY_CONTROL_ENABLE: GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.BOOL, read=True),
            GenvexNabtoSetpointKey.HUMIDITY_LOW_THRESHOLD: GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.PCT, read=True),
            GenvexNabtoSetpointKey.PREHEAT_ENABLE: GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.BOOL, read=True),
            GenvexNabtoSetpointKey.PREHEAT_CYCLE_TIME: GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.SECONDS, read=True),
            GenvexNabtoSetpointKey.PREHEAT_PID_D: GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.UNDEFINED, read=True),
            GenvexNabtoSetpointKey.PREHEAT_PID_I: GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.UNDEFINED, read=True),
            GenvexNabtoSetpointKey.PREHEAT_PID_P: GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.UNDEFINED, read=True),
            GenvexNabtoSetpointKey.REHEAT_ENABLE: GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.BOOL, read=True),
            GenvexNabtoSetpointKey.REHEAT_CYCLE_TIME: GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.SECONDS, read=True),
            GenvexNabtoSetpointKey.REHEAT_PID_D: GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.UNDEFINED, read=True),
            GenvexNabtoSetpointKey.REHEAT_PID_I: GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.UNDEFINED, read=True),
            GenvexNabtoSetpointKey.REHEAT_PID_P: GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.UNDEFINED, read=True),
            GenvexNabtoSetpointKey.TEMP_BYPASS_OPEN_OFFSET: GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.CELSIUS, read=True),
            GenvexNabtoSetpointKey.TEMP_COOLING_START_OFFSET: GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.CELSIUS, read=True),
            GenvexNabtoSetpointKey.TEMP_DEFROST_LOW_THRESHOLD: GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.CELSIUS, read=True),
            GenvexNabtoSetpointKey.TEMP_DEFROST_HIGH_THRESHOLD: GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.CELSIUS, read=True),
            GenvexNabtoSetpointKey.TEMP_HOTWATER: GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.CELSIUS, read=True),
            GenvexNabtoSetpointKey.TEMP_HOTWATER_BOOST: GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.CELSIUS, read=True),
            GenvexNabtoSetpointKey.TEMP_REGULATION_DEAD_BAND: GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.CELSIUS, read=True),
            GenvexNabtoSetpointKey.TEMP_REHEAT_OFFSET: GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.CELSIUS, read=True),
            GenvexNabtoSetpointKey.TEMP_TARGET: GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.CELSIUS, read=True),
            GenvexNabtoSetpointKey.TEMP_SUMMER_SUPPLY_MAX: GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.CELSIUS, read=True),
            GenvexNabtoSetpointKey.TEMP_SUMMER_SUPPLY_MIN: GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.CELSIUS, read=True),
            GenvexNabtoSetpointKey.TEMP_SUPPLY_MAX: GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.CELSIUS, read=True),
            GenvexNabtoSetpointKey.TEMP_SUPPLY_MIN: GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.CELSIUS, read=True),
            GenvexNabtoSetpointKey.TEMP_WINTER_SUPPLY_MAX: GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.CELSIUS, read=True),
            GenvexNabtoSetpointKey.TEMP_WINTER_SUPPLY_MIN: GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.CELSIUS, read=True),
            GenvexNabtoSetpointKey.TEMP_WINTER_MODE_THRESHOLD: GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.CELSIUS, read=True),
            GenvexNabtoSetpointKey.VOC_THRESHOLD: GenvexNabtoPointConfig(unit_of_measurement=GenvexNabtoUnits.PPM, read=True),
        }

class GenvexNabtoBaseModel:
    
    _attr_manufacturer:str = ""
    _attr_model_name:str = "Basemodel"
    
    datapoints: Dict[GenvexNabtoDatapointKey, GenvexNabtoDatapoint] = {}
    setpoints: Dict[GenvexNabtoSetpointKey, GenvexNabtoSetpoint] = {}
    _configs: Dict[GenvexNabtoDatapointKey|GenvexNabtoSetpointKey, GenvexNabtoPointConfig] = {}
    _valueMap: Dict[GenvexNabtoDatapointKey|GenvexNabtoSetpointKey, Dict[float | int, float | int | str]] = {}

    def __init__(self) -> None:
        return

    def get_model_name(self) -> str:
        return self._attr_model_name

    def get_manufacturer(self) -> str:
        return self._attr_manufacturer

    def model_provides_datapoint(self, datapoint: GenvexNabtoDatapointKey) -> bool:
        return datapoint in self.datapoints

    def get_datapoints_for_read(self) -> List[GenvexNabtoDatapointKey]:
        return [key for key, value in self._configs.items() if key in self.datapoints and value.get("read", False) == True]

    def model_provides_setpoint(self, datapoint: GenvexNabtoSetpointKey) -> bool:
        return datapoint in self.setpoints

    def get_setpoints_for_read(self) -> List[GenvexNabtoSetpointKey]:
        return [key for key, value in self._configs.items() if key in self.setpoints and value.get("read", False) == True]

    def get_unit_of_measure(self, key:GenvexNabtoDatapointKey|GenvexNabtoSetpointKey) -> str|None:
        if key in self._configs: return self._configs[key].get("unit_of_measurement", None)
        return GenvexNabtoUnits.UNDEFINED
    
    def set_default_configs(self) -> None:
        """Sets the point configurations to the standard setup, will not override already assigned records"""
    #     # only keep the points supported by the unit
    #     self._configs = {key: value for key, value in DEFAULT_CONFIGS.items() if key in self._setpoints or key in self._datapoints}

    # def addMissingDefaultConfigs(self):
        # Update self._configs with missing items from DEFAULT_CONFIGS
        self._configs.update({
            key: value for key, value in DEFAULT_CONFIGS.items()
            if key not in self._configs and (key in self.setpoints or key in self.datapoints)
        })