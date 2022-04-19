#!/usr/bin/env python3
from kostal.DxsApi import DxsEntry


class ActualHome:
    ACT_HOME_CONSUMPTION_SOLAR = 83886336
    ACT_HOME_CONSUMPTION_BATTERY = 83886592
    ACT_HOME_CONSUMPTION_GRID = 83886848
    PHASE_SELECTIVE_CONSUMPTION_L1 = 83887106
    PHASE_SELECTIVE_CONSUMPTION_L2 = 83887362
    PHASE_SELECTIVE_CONSUMPTION_L3 = 83887618

    def __init__(self, inverter) -> None:
        self.__inverter = inverter

    async def home_consumption_solar(self) -> DxsEntry:
        return (await self.__inverter.fetch_props(self.ACT_HOME_CONSUMPTION_SOLAR)) \
            .get_entry_by_id(self.ACT_HOME_CONSUMPTION_SOLAR)

    async def home_consumption_battery(self) -> DxsEntry:
        return (await self.__inverter.fetch_props(self.ACT_HOME_CONSUMPTION_BATTERY)) \
            .get_entry_by_id(self.ACT_HOME_CONSUMPTION_BATTERY)

    async def home_consumption_grid(self) -> DxsEntry:
        return (await self.__inverter.fetch_props(self.ACT_HOME_CONSUMPTION_GRID)) \
            .get_entry_by_id(self.ACT_HOME_CONSUMPTION_GRID)

    async def home_phase_consumption_l1(self) -> DxsEntry:
        return (await self.__inverter.fetch_props(self.PHASE_SELECTIVE_CONSUMPTION_L1)) \
            .get_entry_by_id(self.PHASE_SELECTIVE_CONSUMPTION_L1)

    async def home_phase_consumption_l2(self) -> DxsEntry:
        return (await self.__inverter.fetch_props(self.PHASE_SELECTIVE_CONSUMPTION_L2)) \
            .get_entry_by_id(self.PHASE_SELECTIVE_CONSUMPTION_L2)

    async def home_phase_consumption_l3(self) -> DxsEntry:
        return (await self.__inverter.fetch_props(self.PHASE_SELECTIVE_CONSUMPTION_L3)) \
            .get_entry_by_id(self.PHASE_SELECTIVE_CONSUMPTION_L3)
