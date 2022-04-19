#!/usr/bin/env python3
from kostal.DxsApi import DxsEntry


class SettingsGeneral:
    INVERTER_NAME = 16777984
    INVERTER_MAKE = 16780544

    def __init__(self, inverter) -> None:
        self.__inverter = inverter

    async def inverter_name(self) -> DxsEntry:
        return (await self.__inverter.fetch_props(self.INVERTER_NAME)) \
            .get_entry_by_id(self.INVERTER_NAME)

    async def inverter_make(self) -> DxsEntry:
        return (await self.__inverter.fetch_props(self.INVERTER_MAKE)) \
            .get_entry_by_id(self.INVERTER_MAKE)
