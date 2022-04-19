#!/usr/bin/env python3
from kostal.DxsApi import DxsEntry


class ActualAnalogInputs:
    ANALOG1 = 167772417
    ANALOG2 = 167772673
    ANALOG3 = 167772929
    ANALOG4 = 167773185

    def __init__(self, inverter) -> None:
        self.__inverter = inverter

    async def analog_1(self) -> DxsEntry:
        return (await self.__inverter.fetch_props(self.ANALOG1)) \
            .get_entry_by_id(self.ANALOG1)

    async def analog_2(self) -> DxsEntry:
        return (await self.__inverter.fetch_props(self.ANALOG2)) \
            .get_entry_by_id(self.ANALOG2)

    async def analog_3(self) -> DxsEntry:
        return (await self.__inverter.fetch_props(self.ANALOG3)) \
            .get_entry_by_id(self.ANALOG3)

    async def analog_4(self) -> DxsEntry:
        return (await self.__inverter.fetch_props(self.ANALOG4)) \
            .get_entry_by_id(self.ANALOG4)
