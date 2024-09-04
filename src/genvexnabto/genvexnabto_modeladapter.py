from typing import Dict, List
from collections.abc import Callable
from .models import ( GenvexNabtoBaseModel, GenvexNabtoOptima314, GenvexNabtoOptima312, GenvexNabtoOptima301, GenvexNabtoOptima270, GenvexNabtoOptima260, GenvexNabtoOptima251, GenvexNabtoOptima250, 
                     GenvexNabtoCTS400, GenvexNabtoCTS602, GenvexNabtoCTS602Light,
                     GenvexNabtoDatapoint, GenvexNabtoDatapointKey, GenvexNabtoSetpoint, GenvexNabtoSetpointKey )

class GenvexNabtoModelAdapter:
    _loadedModel: GenvexNabtoBaseModel = None

    _currentDatapointList: Dict[int, List[GenvexNabtoDatapointKey]] = {}
    _currentSetpointList: Dict[int, List[GenvexNabtoSetpointKey]] = {}

    _values = {}
    _update_handlers: Dict[GenvexNabtoDatapointKey|GenvexNabtoSetpointKey, List[Callable[[int, int], None]]] = {}

    def __init__(self, model, deviceNumber, slaveDeviceNumber, slaveDeviceModel):
        modelToLoad = GenvexNabtoModelAdapter.translateToModel(model, deviceNumber, slaveDeviceNumber, slaveDeviceModel)
        if modelToLoad == None:
            raise "Invalid model"
        self._loadedModel = modelToLoad()
        self._loadedModel.addDeviceQuirks(deviceNumber, slaveDeviceNumber, slaveDeviceModel)
            
        self._currentDatapointList = {100: self._loadedModel.getDatapointsForRead()}
        self._currentSetpointList = {200: self._loadedModel.getSetpointsForRead()}

    def getModelName(self):
        return self._loadedModel.getModelName()
    
    def getManufacturer(self):
        return self._loadedModel.getManufacturer()

    @staticmethod
    def translateToModel(model, deviceNumber, slaveDeviceNumber, slaveDeviceModel) -> Callable:
        if model == 2010:
            if deviceNumber == 79265:
                return GenvexNabtoOptima270
        if model == 2020:
            if deviceNumber == 79280:
                return GenvexNabtoOptima314
        if model == 1040:
            if slaveDeviceNumber == 70810:
                if slaveDeviceModel == 26:
                    return GenvexNabtoOptima260
            if slaveDeviceNumber == 79250:
                if slaveDeviceModel == 9:
                    return GenvexNabtoOptima312
                if slaveDeviceModel == 8:
                    return GenvexNabtoOptima251
                if slaveDeviceModel == 5:
                    return GenvexNabtoOptima301
                if slaveDeviceModel == 1:
                    return GenvexNabtoOptima250
        if model == 1140 or model == 1141:
            if slaveDeviceNumber == 72270:
                if slaveDeviceModel == 1:
                    return GenvexNabtoCTS400
            if slaveDeviceNumber == 2763306:
                if slaveDeviceModel == 2:
                    return GenvexNabtoCTS602Light
                return GenvexNabtoCTS602
            
        return None

    @staticmethod
    def providesModel(model, deviceNumber, slaveDeviceNumber, slaveDeviceModel):
        if GenvexNabtoModelAdapter.translateToModel(model, deviceNumber, slaveDeviceNumber, slaveDeviceModel) is not None:
            return True
        return False
    
    def providesValue(self, key: GenvexNabtoSetpointKey|GenvexNabtoDatapointKey):
        if self._loadedModel.modelProvidesDatapoint(key) or self._loadedModel.modelProvidesSetpoint(key):
            return True 
        return False

    def hasValue(self, key: GenvexNabtoSetpointKey|GenvexNabtoDatapointKey) -> bool:
        return key in self._values
    
    def getValue(self, key: GenvexNabtoSetpointKey|GenvexNabtoDatapointKey):
        return self._values.get(key)
    
    def getMinValue(self, key: GenvexNabtoSetpointKey):
        if self._loadedModel.modelProvidesSetpoint(key): 
            return self.parseValue(fromModbus=True, point=self._loadedModel._setpoints[key], value=self._loadedModel._setpoints[key]['min'])
        return None
    
    def getMaxValue(self, key: GenvexNabtoSetpointKey):
        if self._loadedModel.modelProvidesSetpoint(key): 
            return self.parseValue(fromModbus=True, point=self._loadedModel._setpoints[key], value=self._loadedModel._setpoints[key]['max'])
        return None
    
    def getUnitOfMeasure(self, key: GenvexNabtoSetpointKey|GenvexNabtoDatapointKey):
        return self._loadedModel.getUnitOfMeasure(key)
    
    def getSetpointStep(self, key: GenvexNabtoSetpointKey):
        if self._loadedModel.modelProvidesSetpoint(key):
            if "step" in self._loadedModel._setpoints[key]:             
                return self._loadedModel._setpoints[key]['step'] / self._loadedModel._setpoints[key]['divider']
        return 1
    
    def registerUpdateHandler(self, key: GenvexNabtoSetpointKey|GenvexNabtoDatapointKey, updateMethod: Callable[[int, int], None]):
        if key not in self._update_handlers:
            self._update_handlers[key] = []
        self._update_handlers[key].append(updateMethod)

    def notifyAllUpdateHandlers(self):
        for key in self._update_handlers:
            for method in self._update_handlers[key]:
                method(-1, self._values[key])

    def getDatapointRequestList(self, sequenceId):
        if sequenceId not in self._currentDatapointList:
            return None
        returnList = []
        for key in self._currentDatapointList[sequenceId]:
            returnList.append(self._loadedModel._datapoints[key])
        return returnList
    
    def getSetpointRequestList(self, sequenceId):
        if sequenceId not in self._currentSetpointList:
            return None
        returnList = []
        for key in self._currentSetpointList[sequenceId]:
            returnList.append(self._loadedModel._setpoints[key])
        return returnList
    
    def parseDataResponse(self, responseSeq, responsePayload):
        print(f"Got dataresponse with sequence id: {responseSeq}")
        if responseSeq in self._currentDatapointList:
            print(f"Is a datapoint response")
            return self.parseDatapointResponse(responseSeq, responsePayload)
        if responseSeq in self._currentSetpointList:
            print(f"Is a setpoint response")
            return self.parseSetpointResponse(responseSeq, responsePayload)

    def parseDatapointResponse(self, responseSeq, responsePayload):
        if responseSeq not in self._currentDatapointList:
            return None
        decodingKeys = self._currentDatapointList[responseSeq]
        print(decodingKeys)
        responseLength = int.from_bytes(responsePayload[0:2])
        for position in range(responseLength):
            valueKey = decodingKeys[position]
            payloadSlice = responsePayload[2+position*2:4+position*2]
            oldValue = -1
            if valueKey in self._values:
                oldValue = self._values[valueKey]
            point = self._loadedModel._datapoints[valueKey]
            signed = False if "signed" not in point else point["signed"]
            self._values[valueKey] = self.parseValue(fromModbus=True, point=point, value=int.from_bytes(payloadSlice, 'big', signed=signed))
            if oldValue != self._values[valueKey]:
                if valueKey in self._update_handlers:
                    for method in self._update_handlers[valueKey]:
                        method(oldValue, self._values[valueKey])
     
     
    def parseSetpointResponse(self, responseSeq, responsePayload):
        if responseSeq not in self._currentSetpointList:
            return None
        decodingKeys = self._currentSetpointList[responseSeq]
        responseLength = int.from_bytes(responsePayload[1:3])
        for position in range(responseLength):
            valueKey = decodingKeys[position]
            payloadSlice = responsePayload[3+position*2:5+position*2]
            oldValue = -1
            if valueKey in self._values:
                oldValue = self._values[valueKey]
            point = self._loadedModel._setpoints[valueKey]
            signed = False if "signed" not in point else point["signed"]
            self._values[valueKey] = self.parseValue(fromModbus=True, point=point, value=int.from_bytes(payloadSlice, 'big', signed=signed))
            if oldValue != self._values[valueKey]:
                if valueKey in self._update_handlers:
                    for method in self._update_handlers[valueKey]:
                        method(oldValue, self._values[valueKey])


    def parseValue(self, fromModbus:bool, point:GenvexNabtoDatapoint|GenvexNabtoSetpoint, value):
        if value is None: return None
        invert_from = None
        divider = 1
        offset = None
        if "invert_from" in point: invert_from = point["invert_from"]
        if "divider" in point: divider = point["divider"]
        if "offset" in point: offset = point["offset"]
        # divider = 1 if "divider" not in point else point['divider']
        # offset = None if "offset" not in point else point['offset']
        if fromModbus == True:
            if invert_from is not None: value = invert_from - value
            if offset is not None: value += offset 
            if divider > 1: value /= divider
        else: 
            if divider > 1: value *= divider
            if offset is not None: value -= offset 
            if invert_from is not None: value = invert_from - value
        return value