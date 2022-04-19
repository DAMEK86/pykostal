#!/usr/bin/env python3
from kostal.DxsApi import DxsEntry


class StatisticTotal:
    YIELD = 251658753
    OPERATING_TIME = 251658496
    HOME_CONSUMPTION = 251659009
    SELF_CONSUMPTION = 251659265
    SELF_CONSUMPTION_RATE = 251659280
    AUTONOMY_DEGREE = 251659281

    def __init__(self, inverter) -> None:
        self.__inverter = inverter

    async def total_yield(self) -> DxsEntry:
        return (await self.__inverter.fetch_props(self.YIELD)) \
            .get_entry_by_id(self.YIELD)

    async def total_home_consumption(self) -> DxsEntry:
        return (await self.__inverter.fetch_props(self.HOME_CONSUMPTION)) \
            .get_entry_by_id(self.HOME_CONSUMPTION)

    async def total_self_consumption(self) -> DxsEntry:
        return (await self.__inverter.fetch_props(self.SELF_CONSUMPTION)) \
            .get_entry_by_id(self.SELF_CONSUMPTION)

    async def total_self_consumption_rate(self) -> DxsEntry:
        return (await self.__inverter.fetch_props(self.SELF_CONSUMPTION_RATE)) \
            .get_entry_by_id(self.SELF_CONSUMPTION_RATE)

    async def total_autonomy_degree(self) -> DxsEntry:
        return (await self.__inverter.fetch_props(self.AUTONOMY_DEGREE)) \
            .get_entry_by_id(self.AUTONOMY_DEGREE)

    async def total_operating_time(self) -> DxsEntry:
        return (await self.__inverter.fetch_props(self.OPERATING_TIME)) \
            .get_entry_by_id(self.OPERATING_TIME)
