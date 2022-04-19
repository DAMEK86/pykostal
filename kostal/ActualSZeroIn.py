#!/usr/bin/env python3
from kostal.DxsApi import DxsEntry


class ActualSZeroIn:
    S0_IN_PULSE_COUNT = 184549632
    LOG_INTERVAL = 150995968

    def __init__(self, inverter) -> None:
        self.__inverter = inverter

    async def s0_in_pulse_count(self) -> DxsEntry:
        return (await self.__inverter.fetch_props(self.S0_IN_PULSE_COUNT)) \
            .get_entry_by_id(self.S0_IN_PULSE_COUNT)

    async def s0_in_log_interval(self) -> DxsEntry:
        return (await self.__inverter.fetch_props(self.LOG_INTERVAL)) \
            .get_entry_by_id(self.LOG_INTERVAL)
