#!/usr/bin/env python3
from kostal.DxsApi import DxsEntry


class InfoVersions:
    VERSION_UI = 16779267
    VERSION_FW = 16779265
    VERSION_HW = 16779266
    VERSION_PAR = 16779268
    SERIAL_NUMBER = 16777728
    ARTICLE_NUMBER = 16777472
    COUNTRY_SETTINGS_NAME = 16779522
    COUNTRY_SETTINGS_VERSION = 16779521

    def __init__(self, inverter) -> None:
        self.__inverter = inverter

    async def version_ui(self) -> DxsEntry:
        return (await self.__inverter.fetch_props(self.VERSION_UI)) \
            .get_entry_by_id(self.VERSION_UI)

    async def version_fw(self) -> DxsEntry:
        return (await self.__inverter.fetch_props(self.VERSION_FW)) \
            .get_entry_by_id(self.VERSION_FW)

    async def version_hw(self) -> DxsEntry:
        return (await self.__inverter.fetch_props(self.VERSION_HW)) \
            .get_entry_by_id(self.VERSION_HW)

    async def version_par(self) -> DxsEntry:
        return (await self.__inverter.fetch_props(self.VERSION_PAR)) \
            .get_entry_by_id(self.VERSION_PAR)

    async def serial_nr(self) -> DxsEntry:
        return (await self.__inverter.fetch_props(self.SERIAL_NUMBER)) \
            .get_entry_by_id(self.SERIAL_NUMBER)

    async def article_nr(self) -> DxsEntry:
        return (await self.__inverter.fetch_props(self.ARTICLE_NUMBER)) \
            .get_entry_by_id(self.ARTICLE_NUMBER)

    async def country_settings_name(self) -> DxsEntry:
        return (await self.__inverter.fetch_props(self.COUNTRY_SETTINGS_NAME)) \
            .get_entry_by_id(self.COUNTRY_SETTINGS_NAME)

    async def country_settings_version(self) -> DxsEntry:
        return (await self.__inverter.fetch_props(self.COUNTRY_SETTINGS_VERSION)) \
            .get_entry_by_id(self.COUNTRY_SETTINGS_VERSION)
