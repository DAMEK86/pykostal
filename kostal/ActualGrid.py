#!/usr/bin/env python3
from kostal.DxsApi import DxsEntry


class ActualGrid:
    GRID_OUTPUT_POWER = 67109120
    GRID_FREQ = 67110400
    GRID_COS_PHI = 67110656
    GRID_LIMITATION = 67110144
    GRID_VOLTAGE_L1 = 67109378
    GRID_CURRENT_L1 = 67109377
    GRID_POWER_L1 = 67109379
    GRID_VOLTAGE_L2 = 67109634
    GRID_CURRENT_L2 = 67109633
    GRID_POWER_L2 = 67109635
    GRID_VOLTAGE_L3 = 67109890
    GRID_CURRENT_L3 = 67109889
    GRID_POWER_L3 = 67109891

    def __init__(self, inverter) -> None:
        self.__inverter = inverter

    async def grid_output_power(self) -> DxsEntry:
        return (await self.__inverter.fetch_props(self.GRID_OUTPUT_POWER)) \
            .get_entry_by_id(self.GRID_OUTPUT_POWER)

    async def grid_frequency(self) -> DxsEntry:
        return (await self.__inverter.fetch_props(self.GRID_FREQ)) \
            .get_entry_by_id(self.GRID_FREQ)

    async def grid_cos_phi(self) -> DxsEntry:
        return (await self.__inverter.fetch_props(self.GRID_COS_PHI)) \
            .get_entry_by_id(self.GRID_COS_PHI)

    async def grid_limitation(self) -> DxsEntry:
        return (await self.__inverter.fetch_props(self.GRID_LIMITATION)) \
            .get_entry_by_id(self.GRID_LIMITATION)

    async def grid_voltage_l1(self) -> DxsEntry:
        return (await self.__inverter.fetch_props(self.GRID_VOLTAGE_L1)) \
            .get_entry_by_id(self.GRID_VOLTAGE_L1)

    async def grid_current_l1(self) -> DxsEntry:
        return (await self.__inverter.fetch_props(self.GRID_CURRENT_L1)) \
            .get_entry_by_id(self.GRID_CURRENT_L1)

    async def grid_power_l1(self) -> DxsEntry:
        return (await self.__inverter.fetch_props(self.GRID_POWER_L1)) \
            .get_entry_by_id(self.GRID_POWER_L1)

    async def grid_voltage_l2(self) -> DxsEntry:
        return (await self.__inverter.fetch_props(self.GRID_VOLTAGE_L2)) \
            .get_entry_by_id(self.GRID_VOLTAGE_L2)

    async def grid_current_l2(self) -> DxsEntry:
        return (await self.__inverter.fetch_props(self.GRID_CURRENT_L2)) \
            .get_entry_by_id(self.GRID_CURRENT_L2)

    async def grid_power_l2(self) -> DxsEntry:
        return (await self.__inverter.fetch_props(self.GRID_POWER_L2)) \
            .get_entry_by_id(self.GRID_POWER_L2)

    async def grid_voltage_l3(self) -> DxsEntry:
        return (await self.__inverter.fetch_props(self.GRID_VOLTAGE_L3)) \
            .get_entry_by_id(self.GRID_VOLTAGE_L3)

    async def grid_current_l3(self) -> DxsEntry:
        return (await self.__inverter.fetch_props(self.GRID_CURRENT_L3)) \
            .get_entry_by_id(self.GRID_CURRENT_L3)

    async def grid_power_l3(self) -> DxsEntry:
        return (await self.__inverter.fetch_props(self.GRID_POWER_L3)) \
            .get_entry_by_id(self.GRID_POWER_L3)
