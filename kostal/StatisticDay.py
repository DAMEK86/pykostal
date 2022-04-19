#!/usr/bin/env python3
from kostal.DxsApi import DxsEntry


class StatisticDay:
    YIELD = 251658754
    HOME_CONSUMPTION = 251659010
    SELF_CONSUMPTION = 251659266
    SELF_CONSUMPTION_RATE = 251659278
    AUTONOMY_DEGREE = 251659279

    def __init__(self, inverter) -> None:
        self.__inverter = inverter

    async def day_yield(self) -> DxsEntry:
        return (await self.__inverter.fetch_props(self.YIELD)) \
            .get_entry_by_id(self.YIELD)

    async def day_home_consumption(self) -> DxsEntry:
        return (await self.__inverter.fetch_props(self.HOME_CONSUMPTION)) \
            .get_entry_by_id(self.HOME_CONSUMPTION)

    async def day_self_consumption(self) -> DxsEntry:
        return (await self.__inverter.fetch_props(self.SELF_CONSUMPTION)) \
            .get_entry_by_id(self.SELF_CONSUMPTION)

    async def day_self_consumption_rate(self) -> DxsEntry:
        return (await self.__inverter.fetch_props(self.SELF_CONSUMPTION_RATE)) \
            .get_entry_by_id(self.SELF_CONSUMPTION_RATE)

    async def day_autonomy_degree(self) -> DxsEntry:
        return (await self.__inverter.fetch_props(self.AUTONOMY_DEGREE)) \
            .get_entry_by_id(self.AUTONOMY_DEGREE)
