from typing import Dict, List
from collections.abc import Callable
from .models import ( GenvexNabtoBaseModel, GenvexNabtoOptima314, GenvexNabtoOptima312, GenvexNabtoOptima301, GenvexNabtoOptima270, GenvexNabtoOptima260, GenvexNabtoOptima251, GenvexNabtoOptima250, GenvexNabtoCTS400, GenvexNabtoCTS602, GenvexNabtoCTS602Light,GenvexNabtoDatapoint, GenvexNabtoDatapointKey, GenvexNabtoSetpoint, GenvexNabtoSetpointKey )

class GenvexNabtoModelAdapter:
    _loaded_model: GenvexNabtoBaseModel
    _current_datapoint_list: Dict[int, List[GenvexNabtoDatapointKey]] = {}
    _current_setpoint_list: Dict[int, List[GenvexNabtoSetpointKey]] = {}
    _update_handlers: Dict[GenvexNabtoDatapointKey|GenvexNabtoSetpointKey, List[Callable[[float|int, float|int], None]]] = {}
    """Callable[old_value, new_value]"""

    values: Dict[GenvexNabtoDatapointKey|GenvexNabtoSetpointKey, float|int] = {}

    def __init__(self, model:int, device_number:int, slave_device_number:int, slave_device_model:int) -> None:
        model_to_load = GenvexNabtoModelAdapter.translate_to_model(model, device_number, slave_device_number, slave_device_model)
        if model_to_load == None:
            raise Exception("Invalid model")
        self._loaded_model = model_to_load(device_number, slave_device_number, slave_device_model)
            
        self._current_datapoint_list = {100: self._loaded_model.get_datapoints_for_read()}
        self._current_setpoint_list = {200: self._loaded_model.get_setpoints_for_read()}

    def get_model_name(self) -> str:
        return self._loaded_model.get_model_name()
    
    def get_manufacturer(self) -> str:
        return self._loaded_model.get_manufacturer()

    @staticmethod
    def translate_to_model(model:int, device_number:int, slave_device_number:int, slave_device_model:int) -> Callable[[int,int,int], GenvexNabtoBaseModel]|None:
        if model == 2010:
            if device_number == 79265:
                return GenvexNabtoOptima270
        if model == 2020:
            if device_number == 79280:
                return GenvexNabtoOptima314
        if model == 1040:
            if slave_device_number == 70810:
                if slave_device_model == 26:
                    return GenvexNabtoOptima260
            if slave_device_number == 79250:
                if slave_device_model == 9:
                    return GenvexNabtoOptima312
                if slave_device_model == 8:
                    return GenvexNabtoOptima251
                if slave_device_model == 5:
                    return GenvexNabtoOptima301
                if slave_device_model == 1:
                    return GenvexNabtoOptima250
        if model == 1140 or model == 1141:
            if slave_device_number == 72270:
                if slave_device_model == 1:
                    return GenvexNabtoCTS400
            if slave_device_number == 2763306:
                if slave_device_model == 2:
                    return GenvexNabtoCTS602Light
                return GenvexNabtoCTS602
            
        return None

    @staticmethod
    def provides_model(model:int, device_number:int, slave_device_number:int, slave_device_model:int) -> bool:
        return GenvexNabtoModelAdapter.translate_to_model(model, device_number, slave_device_number, slave_device_model) is not None
    
    def provides_value(self, key: GenvexNabtoDatapointKey|GenvexNabtoSetpointKey) -> bool:
        if isinstance(key, GenvexNabtoDatapointKey): return self._loaded_model.model_provides_datapoint(key) 
        return self._loaded_model.model_provides_setpoint(key)

    def has_value(self, key: GenvexNabtoDatapointKey|GenvexNabtoSetpointKey) -> bool:
        return key in self.values
    
    def get_value(self, key: GenvexNabtoDatapointKey|GenvexNabtoSetpointKey) -> float|int|None:
        return self.values.get(key)
    
    def get_min_value(self, key: GenvexNabtoSetpointKey) -> float|int|None:
        if self._loaded_model.model_provides_setpoint(key): 
            return self.parse_from_modbus_value(point=self._loaded_model.setpoints[key], value=self._loaded_model.setpoints[key]['min'])
        return None
    
    def get_max_value(self, key: GenvexNabtoSetpointKey) -> float|int|None:
        if self._loaded_model.model_provides_setpoint(key): 
            return self.parse_from_modbus_value(point=self._loaded_model.setpoints[key], value=self._loaded_model.setpoints[key]['max'])
        return None
    
    def get_unit_of_measure(self, key: GenvexNabtoDatapointKey|GenvexNabtoSetpointKey) -> str|None:
        return self._loaded_model.get_unit_of_measure(key)
    
    def get_setpoint(self, key:GenvexNabtoSetpointKey) -> GenvexNabtoSetpoint|None:
        if not self._loaded_model.model_provides_setpoint(key): return None
        return self._loaded_model.setpoints[key]
    
    def get_setpoint_step(self, key: GenvexNabtoSetpointKey) -> float|int:
        if self._loaded_model.model_provides_setpoint(key):
            if 'step' in self._loaded_model.setpoints[key]:
                divider = self.get_point_divider(self._loaded_model.setpoints[key])    
                step = self.get_point_step(self._loaded_model.setpoints[key]) 
                if divider > 1: return step / divider
                return step
        return 1
    
    def register_update_handler(self, key: GenvexNabtoDatapointKey|GenvexNabtoSetpointKey, update_method: Callable[[float|int, float|int], None]):
        if key not in self._update_handlers:
            self._update_handlers[key] = []
        self._update_handlers[key].append(update_method)

    def notify_all_update_handlers(self) -> None:
        for key in self._update_handlers:
            for method in self._update_handlers[key]:
                method(-1, self.values[key])

    def getDatapointRequestList(self, sequence_id:int) -> List[GenvexNabtoDatapoint]|None:
        if sequence_id not in self._current_datapoint_list: return None
        return_list:List[GenvexNabtoDatapoint] = []
        for key in self._current_datapoint_list[sequence_id]:
            return_list.append(self._loaded_model.datapoints[key])
        return return_list
    
    def get_setpoint_request_list(self, sequence_id:int) -> List[GenvexNabtoSetpoint]|None:
        if sequence_id not in self._current_setpoint_list: return None
        return_list:List[GenvexNabtoSetpoint] = []
        for key in self._current_setpoint_list[sequence_id]:
            return_list.append(self._loaded_model.setpoints[key])
        return return_list
    
    def parse_data_response(self, response_seq:int, response_payload:bytes) -> None:
        print(f"Got dataresponse with sequence id: {response_seq}")
        if response_seq in self._current_datapoint_list:
            print(f"Is a datapoint response")
            self.parse_datapoint_response(response_seq, response_payload)
        if response_seq in self._current_setpoint_list:
            print(f"Is a setpoint response")
            self.parse_setpoint_response(response_seq, response_payload)

    def parse_datapoint_response(self, response_seq:int, response_payload:bytes) -> None:
        if response_seq not in self._current_datapoint_list: return None
        decoding_keys = self._current_datapoint_list[response_seq]
        print(decoding_keys)
        response_length = int.from_bytes(response_payload[0:2])
        for position in range(response_length):
            valueKey = decoding_keys[position]
            payload_slice = response_payload[2+position*2:4+position*2]
            old_value = -1
            if valueKey in self.values:
                old_value = self.values[valueKey]
            point = self._loaded_model.datapoints[valueKey]
            signed = False if 'signed' not in point else point['signed']
            self.values[valueKey] = self.parse_from_modbus_value(point=point, value=int.from_bytes(payload_slice, 'big', signed=signed))
            if old_value != self.values[valueKey]:
                if valueKey in self._update_handlers:
                    for method in self._update_handlers[valueKey]:
                        method(old_value, self.values[valueKey])
     
    def parse_setpoint_response(self, response_seq:int, response_payload:bytes) -> None:
        if response_seq not in self._current_setpoint_list: return None
        decoding_keys = self._current_setpoint_list[response_seq]
        response_length = int.from_bytes(response_payload[1:3])
        for position in range(response_length):
            valueKey = decoding_keys[position]
            payload_slice = response_payload[3+position*2:5+position*2]
            old_value = -1
            if valueKey in self.values:
                old_value = self.values[valueKey]
            point = self._loaded_model.setpoints[valueKey]
            signed = self.get_point_signed(point)
            self.values[valueKey] = self.parse_from_modbus_value(point=point, value=int.from_bytes(payload_slice, 'big', signed=signed))
            if old_value != self.values[valueKey]:
                if valueKey in self._update_handlers:
                    for method in self._update_handlers[valueKey]:
                        method(old_value, self.values[valueKey])

    def parseToModbusValue(self, point:GenvexNabtoDatapoint|GenvexNabtoSetpoint, value: float|int) -> int:
        divider = self.get_point_divider(point)
        invert_from = self.get_point_invertFrom(point)
        offset = self.get_point_offset(point)
        new_value:float|int = value
        if divider > 1: new_value *= divider
        if offset != 0: new_value -= offset 
        if invert_from is not None: new_value = invert_from - new_value
        return int(new_value) #cast to int, modbus writes only accept an int

    def parse_from_modbus_value(self, point:GenvexNabtoDatapoint|GenvexNabtoSetpoint, value: int) -> float|int:
        divider = self.get_point_divider(point)
        invert_from = self.get_point_invertFrom(point)
        offset = self.get_point_offset(point)
        new_value:float|int = value
        if invert_from is not None: new_value = invert_from - value
        if offset != 0: new_value += offset 
        if divider > 1: new_value /= divider
        return new_value

    def get_point_divider(self, point:GenvexNabtoDatapoint|GenvexNabtoSetpoint) -> int: 
        return 1 if 'divider' not in point else point['divider']
    def get_point_invertFrom(self, point:GenvexNabtoDatapoint|GenvexNabtoSetpoint) -> int|None: 
        return None if 'invert_from' not in point else point['invert_from']
    def get_point_offset(self, point:GenvexNabtoDatapoint|GenvexNabtoSetpoint) -> int: 
        return 0 if 'offset' not in point else point['offset']
    def get_point_read_address(self, point:GenvexNabtoDatapoint) -> int: 
        return point['read_address']
    def get_point_read_obj(self, point:GenvexNabtoDatapoint|GenvexNabtoSetpoint) -> int: 
        return 0 if 'read_obj' not in point else point['read_obj']
    def get_point_write_address(self, point:GenvexNabtoSetpoint) -> int: 
        return point['write_address']
    def get_point_write_obj(self, point:GenvexNabtoSetpoint) -> int: 
        return 0 if 'write_obj' not in point else point['write_obj']
    def get_point_signed(self, point:GenvexNabtoDatapoint|GenvexNabtoSetpoint) -> bool: 
        return point['signed']
    def get_point_step(self, point:GenvexNabtoSetpoint) -> int: 
        return 1 if 'step' not in point else point['step']
    def get_point_max(self, point:GenvexNabtoSetpoint) -> int: 
        return point['max']
    def get_point_min(self, point:GenvexNabtoSetpoint) -> int: 
        return point['min']