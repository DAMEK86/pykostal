#!/usr/bin/env python3
from kostal.DxsApi import DxsEntry


class ActualBattery:
    VOLTAGE = 33556226
    CHARGE = 33556229
    CURRENT = 33556238
    CURRENT_DIR = 33556230
    CHARGE_CYCLES = 33556228
    TEMPERATURE = 33556227

    def __init__(self, inverter) -> None:
        self.__inverter = inverter

    async def battery_voltage(self) -> DxsEntry:
        return (await self.__inverter.fetch_props(self.VOLTAGE)) \
            .get_entry_by_id(self.VOLTAGE)

    async def battery_charge(self) -> DxsEntry:
        return (await self.__inverter.fetch_props(self.CHARGE)) \
            .get_entry_by_id(self.CHARGE)

    async def battery_current(self) -> DxsEntry:
        return (await self.__inverter.fetch_props(self.CURRENT)) \
            .get_entry_by_id(self.CURRENT)

    async def battery_current_dir(self) -> DxsEntry:
        return (await self.__inverter.fetch_props(self.CURRENT_DIR)) \
            .get_entry_by_id(self.CURRENT_DIR)

    async def battery_charge_cycles(self) -> DxsEntry:
        return (await self.__inverter.fetch_props(self.CHARGE_CYCLES)) \
            .get_entry_by_id(self.CHARGE_CYCLES)

    async def battery_temp(self) -> DxsEntry:
        return (await self.__inverter.fetch_props(self.TEMPERATURE)) \
            .get_entry_by_id(self.TEMPERATURE)
