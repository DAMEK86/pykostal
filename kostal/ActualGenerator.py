#!/usr/bin/env python3
from kostal.DxsApi import DxsEntry


class ActualGenerator:
    DC_1_VOLTAGE = 33555202
    DC_1_CURRENT = 33555201
    DC_1_POWER = 33555203
    DC_2_VOLTAGE = 33555458
    DC_2_CURRENT = 33555457
    DC_2_POWER = 33555459
    DC_3_VOLTAGE = 33555714
    DC_3_CURRENT = 33555713
    DC_3_POWER = 33555715

    def __init__(self, inverter) -> None:
        self.__inverter = inverter

    async def generator_dc_1_voltage(self) -> DxsEntry:
        return (await self.__inverter.fetch_props(self.DC_1_VOLTAGE)) \
            .get_entry_by_id(self.DC_1_VOLTAGE)

    async def generator_dc_1_current(self) -> DxsEntry:
        return (await self.__inverter.fetch_props(self.DC_1_CURRENT)) \
            .get_entry_by_id(self.DC_1_CURRENT)

    async def generator_dc_1_power(self) -> DxsEntry:
        return (await self.__inverter.fetch_props(self.DC_1_POWER)) \
            .get_entry_by_id(self.DC_1_POWER)

    async def generator_dc_2_voltage(self) -> DxsEntry:
        return (await self.__inverter.fetch_props(self.DC_2_VOLTAGE)) \
            .get_entry_by_id(self.DC_2_VOLTAGE)

    async def generator_dc_2_current(self) -> DxsEntry:
        return (await self.__inverter.fetch_props(self.DC_2_CURRENT)) \
            .get_entry_by_id(self.DC_2_CURRENT)

    async def generator_dc_2_power(self) -> DxsEntry:
        return (await self.__inverter.fetch_props(self.DC_2_POWER)) \
            .get_entry_by_id(self.DC_2_POWER)

    async def generator_dc_3_voltage(self) -> DxsEntry:
        return (await self.__inverter.fetch_props(self.DC_3_VOLTAGE)) \
            .get_entry_by_id(self.DC_3_VOLTAGE)

    async def generator_dc_3_current(self) -> DxsEntry:
        return (await self.__inverter.fetch_props(self.DC_3_CURRENT)) \
            .get_entry_by_id(self.DC_3_CURRENT)

    async def generator_dc_3_power(self) -> DxsEntry:
        return (await self.__inverter.fetch_props(self.DC_3_POWER)) \
            .get_entry_by_id(self.DC_3_POWER)
